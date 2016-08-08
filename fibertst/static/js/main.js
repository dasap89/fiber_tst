(function($) {
    "use strict";

    /*----------------------------
     	jQuery MeanMenu
    ------------------------------ */
    jQuery('nav#dropdown').meanmenu();

    /*----------------------------
     	wow js active
    ------------------------------ */
    new WOW().init();

    /*----------------------------
    	Populer Courses Container
    ------------------------------ */
    $(".populer-courses-container").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: true,
        navigation: false,
        items: 1,
        /* transitionStyle : "fade", */
        /* [This code for animation ] */
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 2],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });

    /*----------------------------
    	Testimonial Container
    ------------------------------ */
    $(".testimonial-container").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        navigation: true,
        items: 1,
        transitionStyle: "backSlide",
        /* [This code for animation ] */
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsMobile: [479, 1]
    });

    /*----------------------------
    	Brand List v1
    ------------------------------ */
    $(".brand-list").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: false,
        navigation: false,
        loop: true,
        items: 6
    });

    /*----------------------------
    	Online Shop List
    ------------------------------ */
    $(".online-shop-list").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: true,
        navigation: false,
        items: 4,
        /*transitionStyle : "backSlide",  */
        /* [This code for animation ] */
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
    });

    /*----------------------------
    	Latest Blog Area
    ------------------------------ */
    $(".blog-list").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: true,
        navigation: false,
        items: 3,
        /*transitionStyle : "backSlide",  */
        /* [This code for animation ] */
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });
    /*----------------------------
    	related-course-container
    ------------------------------ */
    $(".related-course-container").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: true,
        navigation: false,
        items: 4,
        /*transitionStyle : "backSlide",  */
        /* [This code for animation ] */
        navigationText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
        itemsDesktop: [1199, 3],
        itemsDesktopSmall: [980, 3],
        itemsTablet: [768, 2],
        itemsMobile: [479, 1],
    });
    /*----------------------------
    	testimonials-list v3
    ------------------------------ */
    $(".testimonials-list").owlCarousel({
        autoPlay: true,
        slideSpeed: 2000,
        pagination: false,
        navigation: false,
        items: 1,
        transitionStyle: "backSlide",
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsMobile: [479, 1],
    });

    /*----------------------------
    	brand-logo-area-v3
    ------------------------------ */
    $(".brand-logo-area-v3").owlCarousel({
        autoPlay: false,
        slideSpeed: 2000,
        pagination: true,
        navigation: false,
        items: 1,
        transitionStyle: "backSlide",
        itemsDesktop: [1199, 1],
        itemsDesktopSmall: [980, 1],
        itemsTablet: [768, 1],
        itemsMobile: [479, 1],
    });

    /*----------------------------
    	tab-carosual-list
     ------------------------------ */
    $('.tab-carosual-list').bxSlider({
        slideWidth: 100,
        minSlides: 2,
        maxSlides: 3,
        slideMargin: 10,
        controls: true,
        prevText: ["<i class='fa fa-angle-left'></i>"],
        nextText: ["<i class='fa fa-angle-right'></i>"],
        pager: false,
    });


    /*-------------------------------
    	mixItUp
    ------------------------------- */
    $('.online-shop-list').mixItUp();


    /*------------------------------
     price-slider active
    ------------------------------ */
    $("#slider-range").slider({
        range: true,
        min: 40,
        max: 600,
        values: [60, 570],
        slide: function(event, ui) {
            $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
        }
    });
    $("#amount").val("$" + $("#slider-range").slider("values", 0) +
        " - $" + $("#slider-range").slider("values", 1));

    /*--------------------------
     scrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });

    /*--------------------------
     counter
    ---------------------------- */
    $('.counter').counterUp({
        delay: 10,
        time: 2000
    });


    /*--------------------------
     counter
    ---------------------------- */
    $('.masonry-active').masonry({
        // options
        itemSelector: '.col-md-4',
        columnWidth: 1
    });
    /*--------------------------
     sliphover
    ---------------------------- */
    $(".blog-flickr").sliphover();

    /*--------------------------
     Select Option
    ---------------------------- */
    $('.selectpicker').selectpicker({
        style: 'btn-info',
        size: 4
    });
    /*---------------------
    	Category menu
    --------------------- */
    $('#categorymenu li.active').addClass('open').children('ul').show();
    $('#categorymenu li.has-sub>a').on('click', function() {
        $(this).removeAttr('href');
        var element = $(this).parent('li');
        if (element.hasClass('open')) {
            element.removeClass('open');
            element.find('li').removeClass('open');
            element.find('ul').slideUp(400);
        } else {
            element.addClass('open');
            element.children('ul').slideDown(400);
            element.siblings('li').children('ul').slideUp(400);
            element.siblings('li').removeClass('open');
            element.siblings('li').find('li').removeClass('open');
            element.siblings('li').find('ul').slideUp(400);
        }
    });

    // coming soon template
    $('[data-countdown]').each(function() {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function(event) {
            $this.html(event.strftime('<span class="estut-count days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="estut-count hour"><span class="time-count">%-H</span> <p>Hours</p></span> <span class="estut-count minutes"><span class="time-count">%M</span> <p>Minutes</p></span> <span class="estut-count second"> <span><span class="time-count">%S</span> <p>Seconds</p></span>'));
        });
    });

    /*---------------------
    	Mobile menu
    --------------------- */
    $('nav#mobile-menu').meanmenu();




})(jQuery);