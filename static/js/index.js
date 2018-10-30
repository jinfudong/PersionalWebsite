$(function () {
    window.onscroll = function () {
        var a = document.documentElement.scrollTop || document.body.scrollTop;//滚动条y轴上的距离
        // var b = document.documentElement.clientHeight || document.body.clientHeight;//可视区域的高度
        // var c = document.documentElement.scrollHeight || document.body.scrollHeight;//可视化的高度与溢出的距离（总高度）
        if(a !== 0){
            $(".header_top").css("background", "rgba(0,0,0,1)");
        }else{
            $(".header_top").css("background", "rgba(0,0,0,0)");
        }
    }
});
