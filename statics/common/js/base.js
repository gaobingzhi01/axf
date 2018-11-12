$(function () {
    document.documentElement.style.fontSize = innerWidth / 10 + "px";



    //  http://47.93.232.225:8000/home/
    urlStr = location.href;
    var idStr = urlStr.split("/")[3];
    var $span = $(document.getElementById(idStr));
    $span.css("background", "url(/static/common/img/"+idStr+"1.png)");
    $span.css("background-size", "0.8rem");


});

