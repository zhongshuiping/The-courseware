$(function(){
	
	var $li = $('.slide_pics li');
	var len = $li.length;
	var $prev = $('.prev');
	var $next = $('.next');


	//将要运动过来的li
	var nowli = 0;

	//当前要离开的li
	var prevli = 0;

	var timer = null;



	$li.not(':first').css({left:760});

	$li.each(function(index){

		var $sli = $('<li>');

		if(index==0)
		{
			$sli.addClass('active');
		}

		$sli.appendTo('.points')

	})

	$points = $('.points li');


	$points.click(function(){
		nowli = $(this).index();

		if(nowli==prevli){
			return;
		}

		move();
		$(this).addClass('active').siblings().removeClass('active');
	});


	$prev.click(function(){
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');	

	})

	$next.click(function(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');	

	})

	$('.slide').mouseenter(function() {
		clearInterval(timer);
	});

	$('.slide').mouseleave(function() {
		timer = setInterval(autoplay,4000);
	});



	timer = setInterval(autoplay,4000);

	function autoplay(){
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	}


	function move(){

		if(nowli<0)
		{
			nowli = len-1;
			prevli = 0;
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
			$li.eq(nowli).stop().animate({left:0});
			prevli=nowli;
			return;
		}

		if(nowli>len-1)
		{
			nowli = 0;
			prevli = len-1;
			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});
			$li.eq(nowli).stop().animate({left:0});
			prevli=nowli;
			return;
		}



		if(nowli>prevli){

			$li.eq(nowli).css({left:760});
			$li.eq(prevli).stop().animate({left:-760});			
		}
		else
		{
			$li.eq(nowli).css({left:-760});
			$li.eq(prevli).stop().animate({left:760});
					
		}

		$li.eq(nowli).stop().animate({left:0});
		prevli=nowli;	



	}







})