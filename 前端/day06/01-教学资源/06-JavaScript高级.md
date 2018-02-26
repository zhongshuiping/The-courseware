##06-JavaScript高级

###00- 知识点预习
-	1.数组定义及常用操作方法
- 2.js循环语句
- 3.数组去重
- 4.数组数据放入到界面
- 5.字符串常用方法
- 6.js调试程序方法
- 7.全局变量和局部变量
- 8.js中的定时器及实现动画

###01-数组的定义
```
// 1.实例化对象
var aOneArray = new Array(1,2,3,"a","b");
    
//2.快捷创建
var aTwoArray = [1,2,3,"d","f"];
   
//3.多维数组
var aThreeArray = [[1,2,3],["a","b","c"]];
```

###02-数组的操作
-	push() 在数组后面增加单个或多个元素
- pop()删除数组中最后一个元素
- aOneArray[4] = "ggg"; 修改数组下标为4的元素
- var sStr = aOneArray[4]; 获取数组中角标为4的元素
- splice() 删除或增加

```
//第一个4表示 开始的角标包含4   2表示 删除的个数
aOneArray.splice(4,2);
// 1是开始角标  2是删除个数 剩下的都是新增元素
aOneArray.splice(1,2,"g","h","i");
```

- reverse() 反转 颠倒数组中的元素
- join() 将数组中元素 合并成字符串

```
aOneArray.join()  有逗号连接
aOneArray.join('') 没有逗号
aOneArray.join('_') 下划线连接
```
- length 获取数组的元素个数
- indexOf()  元素在数组中第一次出现的角标
	- -1表示元素不存在

###03-循环语句
```
var iNum = 0;
// 条件成立就一直循环
while (iNum < 5) {
    iNum++;
    console.log(iNum);
}

var oList = [1,2,3,4,5];     
// for循环
for (var i = 0; i < 5; i++) {
    console.log(oList[i]);
}
```

###04-数组去重
-	遍历数组有序的取出每一个元素，然后再取出元素在数组中第一次出现的角标，
- 判断当前遍历的个数索引和元素在数组中的第一次出现的角标是否一样，相同就是第一次出现，然后添加到新的数组
- 不相同就不添加说明是重复的

###05-列表加载数组数据
-	遍历数组取出数组中的每一个元素，把内容拼接到li标签中，
- 再把所有的li标签包裹在ul标签中


###06-类型转换
- parseInt转换为整形
- parseFloat浮点型
-  -  * /  == 隐式转换  系统自动判断 并转换类型

###07-字符串操作
-	字符串拼接 + 
-  类型转换
	-  	parseInt 将字符串转换成整数 number类型
	-   parseFloat 转换为float 浮点型

-	substring(); 截取字符串

```
// 角标开始位置 结束位置(不包含)
var sTwoNew =  sTwo.substring(1,4); 
//从1开始截取到最后
sTwoNew = sTwo.substring(1);
```
- split("") 字符串拆分成数组

```
sTwoNew.split()  整个字符串拆分成数组的一个元素
sTwoNew.split('') 把字符串中的每个字符拆分成一个元素
sTwoNew.split('_') 以'_'字符来拆分字符串
```
- indexOf() 查找字符在字符串中的角标
	- 如果查找的字符在字符串中不存在 返回 -1

	
###08-倒置字符串
- split("") 字符串拆分成数组
-	reverse() 数组中的元素倒置/颠倒
- join("") 数组转换成字符串/把数组中的元素连接成字符串



###09-调试方法
- alert 可以阻止程序的运行
- console.log 控制器输出
- document.title = 更改网页窗口上的标题
-  document.write("AAAAA"); body中直接写入内容

###10- 全局变量和局部变量
-	正常情况局部变量的优先级比全局的高
- 但在js中如果全局和局部变量重名时，局部变量定义的 大{}中 会直接屏蔽全局变量，所以在定义局部变量之前使用会出现undefined;
- 尽量避免全局变量和局部变量同名



###11-定时器
- 只执行一次的定时器
	- setTimeout(功能,时间(毫秒));
	- clearTimeout(timer); 销毁定时器 清除

- 重复执行的定时器
	- setInterval(功能,时间(毫秒));
	- clearInterval(repeatTimer); 销毁重复执行的定时器


###12-js实现左右移动无限动画
-	注意赋值时不要少了单位


###13-无缝滚动
- onmouseover 鼠标停留
- onmouseout 鼠标离开



