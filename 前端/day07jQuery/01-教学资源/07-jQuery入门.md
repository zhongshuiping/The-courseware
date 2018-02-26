##07天-jQuery入门

###00- 知识点预习
-	1.jQuery的加载
- 	2.jQuery选择器
- 	3.jQuery的click事件
-	4.jQuery的样式操作
-	5.jQuery动画

###01- 封闭函数
- 作用:避免在修改他人代码时出现 方法同名替换的情况
-	想让一个函数直接执行用封闭函数
- 避免同名函数覆盖
- 避免同名变量覆盖


###02- jQuery的简介
-	**jQuery**是一个快速、简洁的JavaScript框架，是继Prototype之后又一个优秀的JavaScript代码库（或JavaScript框架）。jQuery设计的宗旨是**“write Less，Do More”**，即倡导写更少的代码，做更多的事情。它封装JavaScript常用的功能代码，提供一种简便的JavaScript设计模式，优化HTML文档操作、事件处理、动画设计和Ajax交互。
-	**jQuery**的核心特性可以总结为：具有独特的链式语法和短小清晰的多功能接口；具有高效灵活的CSS选择器，并且可对CSS选择器进行扩展；拥有便捷的插件扩展机制和丰富的插件。jQuery兼容各种主流浏览器，如IE 6.0+、FF 1.5+、Safari 2.0+、Opera 9.0+等



###03- jQuery的基本使用
- 	1、http://jquery.com/ 官方网站
-	2、https://code.jquery.com/ 版本下载

```
导入CSSq
<script src="js/jquery-1.12.4.min.js"></script>
```
- 为了兼容低版本的浏览器建议使用1.x版本jQuery


###04- jQuery和原生的对比
- Write Less, Do More
-	写的少，做的多，运行速度快
- 原生js只能获取CSS行内式中的属性
- jQuery可以直接设置或获取CSS中属性

###05- jQuery的CSS属性操作
- 原生js中操作样式用style属性
- jQuery中操作CSS函数
	- 数字类型可以不加单位，如果加了单位要用双引号
	- 属性用双引号
	- 属性名可以用js写法也可以用CSS的写法
	- 属性之间用逗号连接
-	jQuery中获取CSS属性时只用双引号包着属性即可
-  jQuery中设置CSS属性时要用大括号{}把属性和值括起来,类似字典格式

###06- jQuery的选择器

- 常用选择器

```
//1.标签
var $element = $("div");

//2.类
$element = $(".para");

//3.ID
$element = $("#spa");

//4.层级选择器
$element = $(".box div");

//5.属性选择器
$element = $("div[class=box3]");

```

###07- jQuery选择集的过滤
- has() 选中后代包含xx的标签
- not() 选中除了xx的标签
- eq(角标)  选中选择集中指定索引的标签 从0开始

```
// 1.has 获取包含有x元素的 x元素
//  获取嵌套有p标签的div标签
var $element = $("div").has("p");

// 2. not ：除了 X 的标签 外的 div标签
//  选择 除了类名叫 box2以外的所有div标签
$element = $("div").not(".box2");

// 3.eq(角标) 等于
var $eq = $(".list li");
$eq.eq(6).CSS({"color":"red"});
```

###08- jQuery选择器的转移
- 找上面相邻的标签
	- prev() 上一个
	- prevAll() 上面所有

- 找下面相邻的标签
	- next();
	- nextAll();
- siblings();除了自己 选中平级的所有标签
- parent()父标签
- children()获取所有直接子标签
- find()查找里面的后代元素

```
// 1.选择器转移
var $div = $(".box4");

// 1.1找上面相信的元素
// 上一个
var $element = $div.prev();

// 上面所有
$element = $div.prevAll();

// 1.2 找下面的相邻元素
// 下一个
$element = $div.next();

// 下面所有
$element = $div.nextAll();

// 1.3 除了自己，别的平级元素都选中
$element = $div.siblings();

// 2.父子关系

// 父元素
$element = $div.parent();

// 子元素 获取的所有直接子元素
$element = $div.children();

// 查找里面的后代元素
$element = $div.find(".grandson");
```

###09- length判断元素是否有无
- length 如果为0说明没有此标签
- 获取当前标签的个数

###10- click事件
- click 点击事件
- this 当前触发事件的标签对象
- index() 获取元素的角标

###11- 操作类样式类名称
```         
// 1.给一个标签 添加类名称
$("div").addClass("green");

//  box green
// 2.删除标签 绑定的 类名称
$("div").removeClass("green");

// 3.切换 类名称
// 如果有这个类名 删除
// 如果 没有这个类名  添加
$("div").toggleClass("green");
```

###12- 选项卡案例
- 给当前点击的按钮添加class,其它按钮删除class，没有class就不会有黄色背景
- 通过点击的按钮索引来查找对应索引的div标签，然后给它添加class，同时删除其它div标签的class


###13- jQuery的动画
- animate
- jQuery 是尺寸相关的动画  颜色不会动画
- 如果要颜色方面的动画要关联jQuery.color库
- 想要实现连续动画可以在动画完成之后执行的函数中继续写动画代码





