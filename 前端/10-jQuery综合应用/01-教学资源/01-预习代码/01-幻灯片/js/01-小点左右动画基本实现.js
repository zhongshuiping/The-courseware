$(function () {
    var $slide = $('.slide'), // 轮播区域的div
        $slideList = $('.slide_list'), // 轮播列表
        $lis = $('.slide_list li'),// 轮播中的四个li
        $prevBtn = $('.prev'), // 上一张按钮
        $nextBtn = $('.next'), // 下一张按钮
        $pointsList = $('.points'); // 小圆点列表


    // 获取广告图片个数
    var iPicCount = $lis.length;
    // 1.根据图片张数动态添加小圆点
    for (var i = 0; i < iPicCount; i++) {
        $pointsList.append('<li></li>');
    }
     // 1.1 默认第0个小点高亮
     $pointsList.children(':first').addClass('active');


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

    function fnMoveAnmation() {
        // 如果重复点击小点什么也不做
        if (iNowIndex == iPreviousIndex) return;

        $pointsList.children().eq(iNowIndex).addClass('active').siblings().removeClass('active');
        // 显示下一张
        if (iNowIndex > iPreviousIndex) {

            // 动画从右边向左移动的准备
            $lis.eq(iNowIndex).css({ 'left': 760 });
            // 让当前显示的图片从0移动到左边-760为要出现的让位置
            $lis.eq(iPreviousIndex).animate({ 'left': -760 });
            // 让要出现的图片从原本的760位置移动到0的位置
            $lis.eq(iNowIndex).animate({ 'left': 0 });

            // 记录这一次显示的索引 作为下一次动画时要让位置的索引
            iPreviousIndex = iNowIndex;
        } else { // 显示上一张

            // 动画从左边向右移动的准备
            $lis.eq(iNowIndex).css({ 'left': -760 });
            // 让当前显示的图片从0移动到右边760位置
            $lis.eq(iPreviousIndex).animate({ 'left': 760 });
            // 让要显示的图片从原本-760的位置移动到0的位置
            $lis.eq(iNowIndex).animate({ 'left': 0 });

            // 记录这一次显示的索引 作为下一次动画时要让位置的索引
            iPreviousIndex = iNowIndex;
        }
    }


})