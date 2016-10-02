$(function(){

    new WOW().init();

    $(window).bind('scroll', function() {
        var navHeight = $(window).height() - 550;
        if ($(window).scrollTop() > navHeight) {
            $('#menu').addClass('on');
        } else {
            $('#menu').removeClass('on');
        }
    });
});