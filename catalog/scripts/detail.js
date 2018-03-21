$(function(){
    $('.imgThumbs').on('mouseenter', function() {
        var thumbSrc = $('#mainImage');
        thumbSrc[0].innerHTML = this.innerHTML;
    });
});


