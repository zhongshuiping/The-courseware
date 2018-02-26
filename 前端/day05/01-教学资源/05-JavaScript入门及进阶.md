##05-JavaScript入门及进阶


###00-知识点预习
-	1、js基本使用
- 	2、js变量定义及类型
-  3、js函数定义及预解析
-  4、js获取标签
-  5、js读写标签属性

###00-JavaScript简介
- JavaScript是运行在浏览器端的脚步语言，JavaScript主要解决的是前端与用户交互的问题，包括使用交互与数据交互。 JavaScript是浏览器解释执行的，前端脚本语言还有JScript（微软，IE独有），ActionScript( Adobe公司，需要插件)等。

-	**前端三大块:**
	-	1、HTML：页面结构
	-	2、CSS：页面表现：元素大小、颜色、位置、隐藏或显示、部分动画效果
	-	3、JavaScript：页面行为：部分动画效果、页面与用户的交互、页面功能
	
###01-js的三中书写方式
-	行内式
- 嵌入式
- 外链式
	- 注意点：如果一个 script标签 链接了一个 js文件, 这个script 就不能再做其他事情

###02-变量的定义
-	变量可以单个定义，也可以一次定义多个，但要用逗号隔开

```
//1.定义一个
var iNumber = 100;
//2.定义多个
var iOne = 200,sTwo = "abc",iThree = 300;

```

###03-变量的类型
-	基本数据类型
	- 数字类型 int float
	- 字符串 string 
	- 布尔类型 true false
	- 未定义 undefined 变量未赋值就是undefined
	- 空类型 null 

-	复合类型 object

```
var oObj = {
    name:"张三",
    age:16,
}
```
-	typeof 获取对象类型

###04-变量和函数的命名规范
-	 1、严格区分大小写
-	2、 首字符 : 字母 下划线(_) $
-	3、除了首字符之外的其他字符: 数字 字母 下划线  $

- **匈牙利命名风格：**
	-	对象o Object 比如：oDiv
	-	数组a Array 比如：aItems
	-	字符串s String 比如：sUserName
	-	整数i Integer 比如：iItemCount
	-	布尔值b Boolean 比如：bIsComplete
	-	浮点数f Float 比如：fPrice
	-	函数fn Function 比如：fnHandler
	-	正则表达式re RegExp 比如：reEmailCheck

###05-js的语句和注释
-	每条语句 结尾以  英文的分号结尾
- 变量 属性 函数 名称尽量见名知意 

- 单行注释 
	- win系统:	ctrl + / 
	- Mac系统: command + /
- 多行注释 
	- win系统:  alt + shift + a 
	- mac系统: option + shift + a

###06-js函数的定义
-	无参数的函数

```
function fnTest() {
    alert('hello');
}

// 函数调用/执行
fnTest();
```
- 有参数的函数

```
function fnResult(a,b) {
    return a + b;
}
var result = fnResult(1,2);

```
- **return**关键字的作用:
	-  1.返回函数中的值或对象
	-  2.结束函数的运行

###07-函数的预解析
- 变量的预解析:
	- 如果前面先使用变量,后面写变量的声明,此时变量值为undefined
- 函数的预解析:
	- 如果前面先写执行,后面写函数定义,系统会在执行的 检查代码,能正常调用



###08-条件语句
-	"==" js中会默认转换数据类型,将数据类型转换成统一类型后再比较
-	"===" 不会转换数据类型,如果类型不一样就是不相等了
- 	"&&" 一假则假,只要有一个条件不成立那就不成立
-  "||" 一真则真,只要有一个条件成立那就为真
-  "!" 取反 真变假  假变真

```
if (条件1) {
    
} else if (条件2){
    
} else {

}
   
```

###09-获取元素标签
```
//1.等window 窗口加载完毕的时候 才能获取到标签  
window.onload =  function () {
    //    1.1获取id为div1的 标签
    var oDiv = document.getElementById("div1");
    //验证
    alert(oDiv);
```

###10-读写元素标签的属性
-	js中使用css样式属性是，把属性中间的 - 去掉 后面的单词首字母大写

```
通过 点语法去读写属性
class属性在js中要写成 className
css中的background-color 在js中要写成 backgroundColor

```
-  属性的值是什么类型，可以把光标放在属性上 看提示

###11-标签包裹的内容
	- innerHTML 修改标签中的内容

###12-匿名函数
- 如果此函数只用一次,而且还是触发事件后才执行的函数就可以简化为匿名函数'没有名字的函数'
	- 单独的匿名函数 报错
	- 匿名函数必须要赋值给变量或属性
	- onclick 监听按钮点击事件，当按钮点击时调用方法



###13-网页换肤案例
```
    <link rel="stylesheet" href="./css/skin01.css" id="link01">
    <script>
        window.onload = function () {
            var oLink = document.getElementById('link01'),
            oBtn01 = document.getElementById('btn01'),
            oBtn02 = document.getElementById('btn02');

            oBtn01.onclick = function () {
            // 修改link标签的href属性
                oLink.href = 'css/skin01.css';
            }

            oBtn02.onclick = function () {
                oLink.href = 'css/skin02.css';
            }
        }
    </script>
```

###14-打印名片
```
if (oInput01.value == '' || oInput02.value == '' || oInput03.value == '' || oInput04.value == '' || oInput05.value == '' || oInput06.value == '') {
    alert("请输入内容!");
    return;
}

// 更换class来修改样式
<!-- + 可以运行也可以用来拼接字符串 如果要运算必须保证两边都是数字类型不然就是拼接字符串了-->
var sClassName = 'idcard0' + (parseInt(oInput07.value) + 1);
oCard_wrap.className = sClassName;

```


