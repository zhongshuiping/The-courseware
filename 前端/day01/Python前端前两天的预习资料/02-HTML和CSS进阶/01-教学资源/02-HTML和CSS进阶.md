##02-HTML和CSS进阶


###00- 知识点预习
-	1.列表
- 	2.选择器
-  3.CSS的文本样式属性
-  4.元素溢出
-  5.盒子模型
-  6.margin负值技巧
-  7.垂直外边距合并
-  8.margin-top塌陷问题


###01- 列表
- 无序列表 ul>li    unorder list
- 清除列表前面的标识 list-sytle:none;
- 列表默认有外边框和内边距

###02- CSS选择器02

```
    /* 1.ID选择器  id是唯一的; 配合js来操作*/
    #three{
        color:blue;
    }
    

   /* 2. strong标签 重要的内容  默认加粗*/
   /* 并集选择器 组选择器 */
   span,strong{
      color:green; 
   }

   /* 3.伪类选择器 '作用在标签身上 改变状态'
   鼠标悬浮: hover
   a:hover{
      color:orange; 
   }

	/* 伪元素  作用在元素'内容身上'*/
   a::before{
        content: "前面增加的内容";
   }

   a::after{
       content: "后面增加";
   }
```

###03- CSS常用属性

```
/* 1.文本对齐 left  center right*/
    text-align: left;

    /* 2.首行缩进  默认大小16px*/
    /* text-indent: 32px; */
    /* em 文字的倍数 */
    text-indent: 2em;

    /* 3.是否斜体   normal*/
    /* font-style: italic; */

    /* 4.是否加粗  normal*/
    font-weight: bold;
    font-size:10px;
    line-height: 20px;
    font-family: "microsoft yahei";


    /* 连写  一定规则*/
        /* 加粗       斜体  字体大小/行高  字体 */
    font:normal italic 10px/20px "microsoft yahei";


```
###04- 元素溢出
-	**overflow:**
	-  visible  默认 超出可视 
	- 	hidden  超出隐藏 裁剪
	-  scroll	  可滚动 不推荐使用
	-  auto  自动
	

###05-  盒子模型真实宽高

	真实的宽 = 左边框'border-left' + 右边框'border-right' + 内容宽'width' + 左边内边距'padding-left' + 右边内边距'padding-right';
	真实的高 = 上边框'border-top' + 下边框'border-right' + 内容高'height' + 顶部内边距'padding-top' + 底部内边距'padding-bottom';
	
	
###06-  margin-使用技巧
	-	margin-top:负值 合并边框

###07-  垂直外边距合并
 -	垂直外边距  取上边元素的底部外边距和下边元素顶部外边距的最大值来当两个元素得垂直间距,而不是累加

###08-  margin-top塌陷问题
-	当设置子元素的margin-top时,没有作用到子元素自己身上,反而影响了父元素
- 解决塌陷问题的方式:
	- 1.父元素设置边框 border
	- 2.父元素设置内边距 padding
	- 3.设置元素溢出 overflow:hidden
	- 4.通过伪元素 

```
.clearfix:before{
	content:"";
	display:table;
}
```




