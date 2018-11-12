$(function () {
    isStr = "yellow" + location.href.split("/")[4];
    var $span = $(document.getElementById((isStr)));
    $span.addClass("yellow");


    //点击全部分类、总和排序
    $("#typeBtn").bind("click",function () {
        $("#typeDiv").toggle();
        $("#sortDiv").hide()
    });
    $("#sortBtn").bind("click",function () {
        $("#sortDiv").toggle();
        $("#typeDiv").hide()
    });
    function func() {
        $(this).hide()
    }
    $("#typeDiv").bind("click",func);
    $("#sortDiv").bind("click",func);

    //给类型加背景颜色
    var typeSpanStr = "type" + location.href.split("/")[5];


});