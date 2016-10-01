
$(function(){
    // 代码高亮 + 代码行号
    $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);

        var lines = $(this).text().split('\n').length;
        var $numbering = $('<ul/>').addClass('pre-numbering');
        $(this)
            .addClass('has-numbering')
            .parent()
            .append($numbering);
        for(i=1;i<=lines;i++){
            $numbering.append($('<li/>').text(i));
        }
    });

    // 给表格加边界
    var $tables = $('table');
    if($tables.length){
        $tables.each(function(index, el) {
            $(this)
                .addClass('table table-bordered table-hover')
                .wrap('<div class="table-responsive"></div>');
        });
    }
})
$(function(){
    if($(window).width()<992){
        $('#myScrollspy').hide();
    }else{
        // 初始化，使myScrollspy与footer不重合
        var $footer = $('#footer');
        $('#myScrollspy').css('bottom', $footer.height() + 200 + 'px');

        // 根据h3生成目录导航
        var lis = '';
        $('.blog-text h3').each(function(i, el){
            var id = 'h3-id-' + i;
            $(this).attr('id', id);
            lis = lis + '<li><a href="#'+id+'">'+$(this).text()+'</a></li>';
        });

        if (!$('.blog-text h3').length) {
            $('#myScrollspy').hide();
        }
        $('#sidernav').append(lis);

        // 目录滚动监听设置
        $('body').scrollspy({ target: '#myScrollspy', offset: 200});
    }

});