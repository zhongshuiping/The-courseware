##01-HTML和CSS入门

###前端阶段课程介绍
-	1 ~ 4  :	**HTML及CSS**
-	5 ~ 6  :	**JavaScript**
-	7 ~ 10	: **jQuery**


###00-知识点预习
-	1、HTML基本结构
- 2、HTML的常用标签
- 3、HTML布局入门
- 4、CSS概述
- 5、CSS书写方式
- 6、CSS常用选择器
- 7、CSS常用属性


###01-什么是HTML？
-	HTML 是用来描述网页的一种语言。
	-	HTML 指的是超文本标记语言: HyperText Markup Language
	-	HTML 不是一种编程语言，而是一种标记语言
	-	标记语言是一套标记标签 (markup tag)
	-	HTML 使用标记标签来描述网页
	-	HTML 文档包含了HTML 标签及文本内容
	-	HTML文档也叫做 web 页面


###02-VSCode基本使用
- Web前端常用开发工具
	- Visual Studio Code  微软出品 Microsoft
	- Sublime Text
	- WebStorm 和PyCharm出自同一个公司
-	VSCode操作面板
- 创建文件的两种方式
	- 创建文件，手动保存文件，不推荐
	- 打开本地文件夹后，再去创建文件，会自动保存而且在创建时就可以修改文件名称及后缀

###03-HTML文档基本结构
```
<!DOCTYPE html> 文档声明类型，声明帮助浏览器正确地显示网页
<html> html文档的根标签

	<head>  网页头部信息，用来做网页的基本配置
		<meta charset="utf-8"> 网页字符编码
		<title>html的基本结构</title> 网页在浏览器窗口中显示的标题
	</head>
	
<body>此标签中写网页中显示的内容</body>
</html>
```
###04-HTML文档创建的快捷方式
```
!+tab键
html5+tab键
```
###05-常用标签01
-	h1~h6  header 标签
- img标签 
	- src:图片路径 
	- alt: 图片加载失败时显示，数据分析及搜索引擎收录图片
	- title:光标放在图片上提示

-	a 标签 界面跳转 

```
	href = "地址/网址 http://"
	
	target: 目标 "_self" "_blank"
	
	<a>更多</a> 标签中的文字会显示出来，链接不会显示，但此文字会有跳转功能
```
###06-绝对和相对路径
- 绝对路径
	-	Windows系统下的文件绝对路径:
		- C:\Program Files\feiq\RecvFace\xxx.png
	- 	Mac系统下的文件绝对路径:
		-  /Users/chao/Desktop/xxx.png

-	相对路径 推荐使用
 -	./ 当前目录路径 可以省略
 -	../ 当前文件的上一级路径
 -	../../最多用两个不要多写
 

###07-常用标签02
- p 段落标签 
- br 换行标签
- 字符实体

```
&nbsp;   空格
&lt;  <  小于号
&gt;  >  大于号
&amp;  &字符实体
```
- div块标签
- span标签

###08-常用标签小结
```
<h1~h6> 标题
a标签 链接
img  图片标签  scr  alt  title
p  标签
br  换行
div 块标签
span 圈住一块文字
&lt;  <
&gt;  >
&nbsp;  空格
&amp;   &
```
###09-今日头条界面内容展示
- 用div细分模块方便界面布局 样式设置及调整
![今日头条](./笔记中的图片/今日头条内容.png)

###10-什么是CSS？
-	CSS 指层叠样式表 (Cascading Style Sheets)
-	样式定义如何显示 HTML 元素
-	把样式添加到 HTML 4.0 中，是为了解决内容与表现分离的问题
-	外部样式表可以极大提高工作效率

###11-行内式

```
<div sytle="background-color:red">

```
###12-嵌入式
```
<head>

	<style>
	p{
	background-color:red;
	}
	</style>

</head>
```
###13-外链式
```
<head>

<link rel="stylesheets" herf:"./css/main.css">

</head>
```
###14-CSS书写方式小结
-	临时设置某一个标签的样式，或测试等可以选择行内式
-	网站首页用嵌入式，优点加载快，网页显示快
-	工作中常用外链式，其他界面，实现HTML和CSS的分离和复用

###15-CSS常用选择器01
-	标签选择器
-	类选择器
-	层级选择器

###16-CSS常用属性
-	文本属性
	- font-size 字体大小
	- color  文字颜色
	- font-family 字体 'Microsoft YaHei'
	- line-height 行高 可以让文字在指定高度垂直居中效果
- width 宽度
- height 高度
- border 边框
	- solid 实线
- background-color 背景色
- margin 顺序上右下左 外边距
- padding 上右下左   内边距


###17-今日头条界面样式处理
![今日头条](./笔记中的图片/今日头条效果.png)

###18-常用插件
-	HTML Snippets 代码提示插件
-	Path Autocomplete 路径提示插件
	-	 插件提示路径时后缀也自动带上
	-	"path-autocomplete.extensionOnImport": true,
-	open in browser  用快捷键的方式打浏览器打到.html文件 
-	ctrl+B 在电脑默认浏览器打开
	-	Set default browser 设置默认打开浏览器
    "open-in-browser.default": "chrome",
-	ctrl + shift + B 在指定浏览器打开
