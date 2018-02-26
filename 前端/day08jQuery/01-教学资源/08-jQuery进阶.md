##08-jQuery进阶

###00- 知识点预习
-	1.jQuery特殊效果
-	2.链式调用
-	3.属性操作
-	4.jQuery循环
-	5.jQuery事件

###01- jQuery的特殊效果

```
//1. 淡入淡出 fade
// $(".box").fadeIn(); 
// $(".box").fadeOut();
// $(".box").fadeToggle();
    
//2. 显示隐藏
// $(".box").hide();
// $(".box").show();
// $(".box").toggle();

//3.卷开 卷起
// $(".box").slideDown();
// $(".box").slideUp();
// $(".box").slideToggle();
```
###02- jQuery链式调用
-	jQuery对象的方法会在执行完后返回这个jQuery对象，所有jQuery对象的方法可以连起来写

###03- 层级菜单案例
```
//1.点击分类的 '水果' 下面的ul 打开
var $next =  $(this).next().slideToggle();

// 2.  每次 只打开一个 ,其他的关闭 siblings()
// 2.1 $next 对象 是你选中的 a 标签下面的 ul列表
// 2.2 $next 需要获取 父元素 parent() li标签
// 2.3 通过li标签 获取 其他的同级 元素siblings()
// 2.4 获取同级元素 li 下面的 子元素 children()
// 2.5 li 子元素有两个  过滤下 childer("ul")
// 2.6 slideup()
   
$next.parent().siblings().children("ul").slideUp();
```

###04- jQuery操作属性
- prop() 获取和设置标签属性
	- 读取的时候用双引号包裹属性即可
	- 设置属性时，要用{}包裹属性
-	val() 获取及设置value属性
	-	input标签的值获取及设置
- html() 获取和修改标签包裹的内容


###05- 对话框案例
- val() 获取input标签的value

###06- jQuery的循环遍历
- each
- 遍历的函数内 this表示当前遍历出来的元素 表示一个元素动态类型

###07- 手风琴效果
- 更改当前点击li标签前面和后面的元素left值
-  去到右边的位置：

```
    第 4 个到右边的位置：727 — 21
    第 3 个到右边的位置：727 - 21*2
    第 2 个到右边的位置：727 - 21*3
    第 1 个到右边的位置：727 - 21*4
    到右边的位置的公式：727-21*(5-$(this).index())
```

###08- 焦点事件
- focus() 让文本输入框自动获取焦点，
- blur() 失去焦点


###09- 鼠标事件
- 进入子元素 会触发事件
	- mouseover() 鼠标进入（进入子元素也触发）
	- mouseout() 鼠标离开（离开子元素也触发）

- 进入子元素 不会触发事件 -- 建议使用
 	- mouseenter() 鼠标进入（进入子元素不触发）
 	- mouseleave() 鼠标离开（离开子元素不触发）

 	- hover() 同时为mouseenter和mouseleave事件指定处理函数
 	
```
$div01.hover(function (event) {
     $(this).animate({'margin-top':event.type == 'mouseenter' ? 100 : 50});
})
```
