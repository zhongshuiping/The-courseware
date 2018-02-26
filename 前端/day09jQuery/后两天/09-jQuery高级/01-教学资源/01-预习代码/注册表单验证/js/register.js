$(function () {
	var $name = $('#user_name'),
		$pwd = $('#pwd'),
		$cpwd = $('#cpwd'),
		$email = $('#email'),
		$allow = $('#allow');

	var bName = false, bPwd = false, bCpwd = false, bEmail = false, bAllow = true;

	// 用户名
	$name.blur(function () {
		bName = fnJudgeMethod($(this), '用户名', /^\w{6,20}$/, '用户名只能是6到20位字母数字,还包含"_"');
	});
	// 密码
	$pwd.blur(function () {
		bPwd = fnJudgeMethod($(this), '密码', /^[\w!@#$%^&*]{6,20}$/, '密码只能是6到20位字母数字,还包含"_!@#$%^&*"字符');
	});
	// 确认密码
	$cpwd.blur(function () {
		var sPass = $pwd.val();
		var sCpass = $(this).val();
		if (sCpass != sPass) {
			$(this).next().html('两次输入的密码不一致!').show();
			bCpwd = false;
		} else {
			bCpwd = true;
		}
	})
	// 邮箱
	$email.blur(function () {
		bEmail = fnJudgeMethod($(this), '邮箱', /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/i, '你输入的邮箱格式不正确');
	});

	// 协议
	$allow.click(function () {
		// this.checked == true
		if ($(this).is(':checked') == true) {
			$(this).nextAll('span').hide();

			bAllow = true;
		} else {
			$(this).nextAll('span').html('请勾选!').show();

			bAllow = false;
		}


	})


	// 点击所有输入框时不显示提示
	$('.reg_form input').not('#allow,#sub').click(function () {
		$(this).next().hide();
	});


	// 是否提交
	$('.reg_form form').submit(function () {
		// 都验证通过才能提交
		if (bName && bPwd && bCpwd && bEmail && bAllow) {
			return true;
		} else {
			return false;
		}
	})

	// 验证函数 参数1:验证input对象,
	// 参数2:为空时的提示
	// 参数3:正则表达式
	// 参数4.正则不匹配时的提示
	function fnJudgeMethod(oObjc, sNull, reValue, sRegInfo) {
		var sCon = oObjc.val();
		// 是否为空
		if (sCon == '') {
			
			oObjc.next().html(sNull + '不能为空!').show();
			return false;

		} else if (reValue.test(sCon) == false) {// 是否匹配成功

			oObjc.next().html(sRegInfo).show();
			return false;
		}
		// 成功
		return true;

	}

})