//返回顶部/start
function b() {
	h = $(window).height(),
	t = $(document).scrollTop(),
	t > '1000' ? $("#moquu_top").show() : $("#moquu_top").hide()
}
//大于1000px显示按钮
$(window).scroll(function() {
	b()
});
//动态到顶部
$(document).ready(function() {
	b(),  //到顶部消失
	$("#moquu_top").click(function() {
		$("html,body").animate({
			scrollTop: 0}, 500);
			return false;
	})
})
//返回顶部/end