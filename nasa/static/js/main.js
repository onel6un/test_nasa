$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    fade: true,
    asNavFor: '.slider-nav',
    variableWidth: true
});
$('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 22,
    asNavFor: '.slider-for',
    dots: true,
    centerMode: true,
    focusOnSelect: true,
    variableWidth: true
});