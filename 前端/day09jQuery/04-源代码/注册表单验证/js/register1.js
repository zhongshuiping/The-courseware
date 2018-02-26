$(function () {
    // 1.获取相应的标签
    var $UserName = $('#user_name'),   	// 用户名输入框
        $Pwd = $('#pwd'), 					// 密码
        $Cpwd = $('#cpwd'),					// 确认密码
        $Email = $('#email'),				// 邮箱
        $Allow = $('#allow'),				// 同意协议
        $Sub = $('#sub'),					// 注册按钮
        $Form = $('.reg_form form'),		// 表单
        bIsUser = false, bIsPwd = false, bIsCpwd = false, bIsEmail = false, bIsAllow = true;



    // 2.判断用户名
    /* 		$UserName.blur(function () {
                // 2.1获取文本输入框中的内容
                var sCon = $(this).val();
                // 2.2 判断是否为空
                if (sCon == '') {
                    $(this).next().show().html('用户名不能为空!');
                } else if (/^\w{6,20}$/.test(sCon) == false){  // 匹配正则
                    $(this).next().show().html('用户名只能是6到20位字母数字,还包含"_"!');
                }
            }) */

    // 2.用户名验证
    $UserName.blur(function () {

        bIsUser = fnJudgeMethod(this, '用户名', /^\w{6,20}$/, '用户名只能是6到20位字母数字,还包含"_"!');
    })

    // 3.密码验证
    $Pwd.blur(function () {

        bIsPwd = fnJudgeMethod(this, '密码', /^[\w!@#$%^&*]{6,20}$/, '密码只能是6到20位字母数字,还包含"_!@#$%^&*"字符!');
    })


    // 4.确认密码验证
    $Cpwd.blur(function () {
        // 4.1获取文本输入框中的内容
        var sCon = $(this).val(), // 确认密码
            sPwd = $Pwd.val();       // 密码框

        // 4.2.两次密码是否一致
        if (sCon == sPwd) {
            bIsCpwd = true;
        } else {
            $(this).next().show().html('两次密码不一致!');
            bIsCpwd = false;
        }

    })

    // 5.邮箱验证
    $Email.blur(function () {

        bIsEmail = fnJudgeMethod(this, '邮箱', /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i, '你输入的邮箱格式不正确');
    })

    

    // 6.判断是否勾选同意协议
    $Allow.click(function () {
        // this.checked == true 原生js的判断方式

        // alert(this.checked);
        // console.log($(this).is(':checked'));
        if ($(this).is(':checked') == true) { // 勾选了
            $(this).next().next().hide()
            bIsAllow = true;
        } else { // 没勾选
            $(this).next().next().show().html('请勾选!');
            bIsAllow = false;
        }
    })



    // 7.判断表单是否提交
    $Form.submit(function () {

        // 如果全部验证通过就返回true可以提前
        if (bIsUser && bIsPwd && bIsCpwd && bIsUser && bIsAllow) {
            return true;
        } else {
            // 阻止提交
            return false;
        }
    })



    // 公共的判断函数
    // 参数1: 文本输入框标签对象
    // 参数2: 谁不能为空
    // 参数3: 正则
    // 参数4: 正则的提示
    function fnJudgeMethod(obj, nilInfo, reStr, reErrorInfo) {
        // 2.1获取文本输入框中的内容
        var sCon = $(obj).val();
        // 2.2 判断是否为空
        if (sCon == '') {
            $(obj).next().show().html(nilInfo + '不能为空!');
            return false;
        } else if (reStr.test(sCon) == false) {  // 匹配正则
            $(obj).next().show().html(reErrorInfo);
            return false;
        }

        // 如果走到这里说明验证成功
        return true;

    }


    // 当输入框只要成为焦点就隐藏提示信息
    // alert($('.reg_form input').not('#allow,#sub').length);
    $('.reg_form input').not('#allow,#sub').click(function () {
        $(this).next().hide();
    })
})