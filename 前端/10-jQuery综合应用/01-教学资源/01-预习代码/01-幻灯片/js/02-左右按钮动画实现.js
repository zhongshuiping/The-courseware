$(function () {
    var $slide = $('.slide'), // 轮播区域的div
        $slideList = $('.slide_list'), // 轮播列表
        $lis = $('.slide_list li'),// 轮播中的四个li
        $prevBtn = $('.prev'), // 上一张按钮
        $nextBtn = $('.next'), // 下一张按钮
        $pointsList = $('.points'), // 小圆点列表
        iPicCount = $lis.length, // 获取广告图片个数
        iNowIndex = 0, // 即将要上显示的这一张
        iPreviousIndex = 0,// 上一张,也是要让位置的这一张
        bIsAnmation = false; // 是否正在动画中

    // 1.根据图片张数动态添加小圆点
    for (var i = 0; i < iPicCount; i++) {
        $pointsList.append('<li></li>');
    }
    // 1.1 默认第0个小点高亮
    $pointsList.children(':first').addClass('active');


    // 2.动画前的准备除了第一张 其它 都放到760的位置
    $lis.not(':first').css({ 'left': 760 });


    // 2.1 点击小圆点进行图片移动动画
    $pointsList.delegate('li', 'click', function () {
        // 记录马上要显示的图片索引
        iNowIndex = $(this).index();

        fnMoveAnmation();
    });


    // 3.点击左边上一张按钮
    $prevBtn.click(function () {
        // 如果正在动画点击按钮什么也不做
        if (bIsAnmation == true) return;
        iNowIndex--;
        fnMoveAnmation();
    })

    // 4.点击右边下一张按钮
    $nextBtn.click(function () {
        // 如果正在动画点击按钮什么也不做
        if (bIsAnmation == true) return;
        iNowIndex++;
        fnMoveAnmation();
    })


    // 公用的切换图片函数
    function fnMoveAnmation() {
        // 如果重复点击小点什么也不做
        if (iNowIndex == iPreviousIndex) return;
        // 走到这一步说明要开始动画了
        bIsAnmation = true;

        // 如果最后一张后继续点击右边按钮,应该向左移动的方式来显示第0张
        if (iNowIndex > iPicCount - 1) {
            // 下一张时:最后一张的下一张是第0张
            iNowIndex = 0;
            // 动画从右边向左移动的准备
            $lis.eq(iNowIndex).css({ 'left': 760 });
            // 让当前显示的图片从0移动到左边-760为要出现的让位置
            $lis.eq(iPreviousIndex).animate({ 'left': -760 });
        } else if (iNowIndex < 0) {
            // 上一张时:第0张的上一第应该是最后一张
            iNowIndex = iPicCount - 1;
            // 动画从左边向右移动的准备
            $lis.eq(iNowIndex).css({ 'left': -760 });
            // 让当前显示的图片从0移动到右边760位置
            $lis.eq(iPreviousIndex).animate({ 'left': 760 });
        } else {
            // 显示下一张
            if (iNowIndex > iPreviousIndex) {

                // 动画从右边向左移动的准备
                $lis.eq(iNowIndex).css({ 'left': 760 });
                // 让当前显示的图片从0移动到左边-760为要出现的让位置
                $lis.eq(iPreviousIndex).animate({ 'left': -760 });

            } else { // 显示上一张

                // 动画从左边向右移动的准备
                $lis.eq(iNowIndex).css({ 'left': -760 });
                // 让当前显示的图片从0移动到右边760位置
                $lis.eq(iPreviousIndex).animate({ 'left': 760 });

            }

        }

        // 更改当前高亮的小点
        $pointsList.children().eq(iNowIndex).addClass('active').siblings().removeClass('active');
        // 让要图片移动到0的位置
        $lis.eq(iNowIndex).animate({ 'left': 0 }, function () {
            bIsAnmation = false; // 动画完完成
        });
        // 记录这一次显示的索引 作为下一次动画时要让位置的图片索引
        iPreviousIndex = iNowIndex;
    }


})