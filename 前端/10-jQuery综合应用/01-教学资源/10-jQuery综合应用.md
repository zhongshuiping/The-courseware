##10-jQuery综合应用



###00- 知识点预习
-	1.幻灯片的制作
-	2.json数据格式及ajax

###01- 轮播图-获取相关元素
```
 var $slide = $('.slide'), // 轮播区域的div
        $slideList = $('.slide_list'), // 轮播列表
        $lis = $('.slide_list li'),// 轮播中的四个li
        $prevBtn = $('.prev'), // 上一张按钮
        $nextBtn = $('.next'), // 下一张按钮
        $pointsList = $('.points');// 小圆点列表
```


###02- 轮播图-添加小圆点
```
   // 1.根据图片张数动态添加小圆点
    for (var i = 0; i < iPicCount; i++) {
        $pointsList.append('<li></li>');
    }
    // 1.1 默认第0个小点高亮
    $pointsList.children(':first').addClass('active');

```

###03- 轮播图-监听小圆点事件 - 下一张
```
    // 2.动画前的准备除了第一张 其它 都放到760的位置
    $lis.not(':first').css({ 'left': 760 });

    var iNowIndex = 0; // 即将要上显示的这一张
    var iPreviousIndex = 0; // 上一张,也是要让位置的这一张

    // 2.1 点击小圆点进行图片移动动画
    $pointsList.delegate('li', 'click', function () {

        // 记录即将要显示的图片索引
        iNowIndex = $(this).index();
        // 动画移动
        fnMoveAnmation();
    });
    
    // 公共函数
    function fnMoveAnmation() {
      	// 小圆点高亮处理
      	$pointsList.children().eq(iNowIndex).addClass('active').siblings().removeClass('active');
        // 显示下一张
        if (iNowIndex > iPreviousIndex) {

        
            // 让当前显示的图片从0移动到左边-760为要出现的让位置
            $lis.eq(iPreviousIndex).animate({ 'left': -760 });
            // 让要出现的图片从原本的760位置移动到0的位置
            $lis.eq(iNowIndex).animate({ 'left': 0 });

            // 记录这一次显示的索引 作为下一次动画时要让位置的索引
            iPreviousIndex = iNowIndex;
        } 
        
    }
```

###04- 轮播图-小圆点事件 - 上一张
```
else { // 显示上一张

            // 动画从左边向右移动的准备
            $lis.eq(iNowIndex).css({ 'left': -760 });
            // 让当前显示的图片从0移动到右边760位置
            $lis.eq(iPreviousIndex).animate({ 'left': 760 });
            // 让要显示的图片从原本-760的位置移动到0的位置
            $lis.eq(iNowIndex).animate({ 'left': 0 });

            // 记录这一次显示的索引 作为下一次动画时要让位置的索引
            iPreviousIndex = iNowIndex;
        }
```

###05- 轮播图-跨越式点击的BUG解决
-	重复点击同一个小点时bug

```
 function fnMoveAnmation() {
        // 如果重复点击小点什么也不做
        if (iNowIndex == iPreviousIndex) return;
```

```
从右向左边滑动时
//解决跨越式点击BUG :抢先一步 将要出现的图片 丢到他该出现的位置 760
$lis.eq(iNowIndex).css({"left":760}) 

从左向右边滑动时
//解决跨越式点击BUG :抢先一步 将要出现的图片 丢到他该出现的位置 -760
$lis.eq(iNowIndex).css({"left":-760}) 
```

###06- 轮播图-监听左边按钮的点击
```
    // 3.点击左边上一张按钮
    $prevBtn.click(function () {
       
        iNowIndex--;
        fnMoveAnmation();
    })

```

###07- 轮播图-右侧按钮的点击
```
   // 4.点击右边下一张按钮
    $nextBtn.click(function () {
     
        iNowIndex++;
        fnMoveAnmation();
    })
```


###08- fnMoveAnmation函数的调整
```
 // 如果最后一张后继续点击右边按钮,应该向左移动的方式来显示第0张
        if (iNowIndex > iPicCount - 1) {
            // 下一张时:最后一张的下一张是第0张
            iNowIndex = 0;
            // 动画从右边向左移动的准备
            $lis.eq(iNowIndex).css({ 'left': 760 });
            // 让当前显示的图片从0移动到左边-760为要出现的让位置
            $lis.eq(iPreviousIndex).animate({ 'left': -760 });
            
        } else if (iNowIndex < 0) { // 如果是第0张时继续点击左边上一张按钮
        
            // 上一张时:第0张的上一第应该是最后一张
            iNowIndex = iPicCount - 1;
            // 动画从左边向右移动的准备
            $lis.eq(iNowIndex).css({ 'left': -760 });
            // 让当前显示的图片从0移动到右边760位置
            $lis.eq(iPreviousIndex).animate({ 'left': 760 });
		} else {
		// 把正常情况下的左右滚动代码放在else里面
		}
```

###09- 轮播图- 左右按钮快速点击的bug
- 动画还没有执行完，点击左右按钮什么事件也不做
-  bIsAnmation = false; // 是否正在动画中
-  左右按钮点击事件中加入如果动画中直接返回
-  进入fnMoveAnmation里时把bIsAnmation改为true
-  最后的动画执行完成的回调中把bIsAnmation再改回为false;

###10- 轮播图-自动播放
```
    // 自动滚动
    function fnAutoMove() {
        iNowIndex++;
        fnMoveAnmation();
    }

    // 5.定时器自动滚动
    var oTimer = setInterval(fnAutoMove, 3000);
```

###11- 轮播图-鼠标事件
```
//6.鼠标的事件
    $slide.mouseenter(function () {
        clearInterval(oTimer);
    });

    $slide.mouseleave(function () {
        oTimer = setInterval(fnAutoMove, 3000);
    })

```




###12- JSON概述和书写格式
- JSON是 JavaScript Object Notation 的首字母缩写，单词的意思是JavaScript对象表示法，这里说的JSON指的是类似于JavaScript对象的一种数据格式，目前这种数据格式比较流行，逐渐替换掉了传统的XML数据格式。

- JSON格式的数据：

```
{
    "name":"tom",
    "age":18
}
```
- 与JavaScript对象不同的是，JSON数据格式的属性名称和字符串值需要用双引号引起来，用单引号或者不用引号会导致读取数据错误。
- 最后一个属性后面不要逗号
- JSON里面也不要写注释,有可能会加载出错!
- JSON的另外一个数据格式是数组，和JavaScript中的数组字面量相同。

```
["tom",18,"programmer"]
```
###13- ajax加载JSON数据

- $.ajax使用方法
- 常用参数：
	-	1、url 请求地址
	-	2、type 请求方式，默认是'GET'，常用的还有'POST'
	-	3、dataType 设置返回的数据格式，常用的是'json'格式，也可以设置为'html'
	-	4、data 设置发送给服务器的数据
	-	5、success 设置请求成功后的回调函数
	-	6、error 设置请求失败后的回调函数
	-	7、async 设置是否异步，默认值是'true'，表示异步


- 以前的写法：

```
	$.ajax({
		url: 'js/data.json',
		type: 'GET',
		dataType: 'json',
		data:{'aa':1}
		success:function(data){
		alert(data.name);
	},
		error:function(){
		alert('服务器超时，请重试！');
		}
	});

```

- 新的写法(推荐)：

```
	
	$.ajax({
		url: 'js/data.json',
		type: 'GET',
		dataType: 'json',
		data:{'aa':1}
	})
	.done(function(data) {
		alert(data.name);
	})
	.fail(function() {
		alert('服务器超时，请重试！');
	});
		
	// data.json里面的数据： {"name":"tom","age":18}
```

###14- ajax天天生鲜局部刷新
-	准备好要请求的JSON数据
- 请求后先验证数据，再写功能代码

###15- jsonp的原理
- ajax只能请求同一个域下的数据或资源，有时候需要跨域请求数据，就需要用到jsonp技术，jsonp可以跨域请求数据，它的原理主要是利用了script标签可以跨域链接资源的特性。jsonp和ajax原理完全不一样，不过jQuery将它们封装成同一个函数。

###16- jsonp跨域请求
```
$.ajax({
    url:'js/data.js',
    type:'get',
    dataType:'jsonp',
    jsonpCallback:'fnBack'
})
.done(function(data){
    alert(data.name);
})
.fail(function() {
    alert('服务器超时，请重试！');
});

// data.js里面的数据： fnBack({"name":"tom","age":18});
```
###17- 仿360搜索
```
 $(function(){
    $('#txt01').keyup(function(){
        var sVal = $(this).val();
        $.ajax({
            url:'https://sug.so.360.cn/suggest',
            type:'get',
            dataType:'jsonp',
            //给服务器传递参数
            data: {word: sVal}
        })
        .done(function(data){
            var aData = data.s;
            $('.list').empty();
            for(var i=0;i<aData.length;i++)
            {
                var $li = $('<li>'+ aData[i] +'</li>');
                $li.appendTo($('.list'));
            }
        })        
    })
})
```



