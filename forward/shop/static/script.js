 $(document).ready(function(){
                $('.your-class').slick({
                    autoplay: true,
                    autoplaySpeed: 2000,
                });
            });

            $(document).ready(function(){
                $('.slider-detail').slick();
            });
            
                $('.block_basket').hover(
                    function(){
                        $('.block_basket-mini').addClass('hover_opacity');
                    },
                    function(){
                        $('.block_basket-mini').removeClass('hover_opacity');
                    }
                );

                $('.block_basket-mini').hover(
                    function(){
                        $('.block_basket-mini').addClass('hover_opacity');
                    },
                    function(){
                        $('.block_basket-mini').removeClass('hover_opacity');
                    }
                )

                $('.hover_subProduct').hover(
                    function(){
                        $(this).find('.aside-menu-inserted').addClass('hover_displayTrue');
                    },
                    function(){
                        $(this).find('.aside-menu-inserted').removeClass('hover_displayTrue');
                    }
                );

                $('.aside-menu-inserted').hover(
                    function(){
                        $(this).find('.aside-menu-inserted').addClass('hover_displayTrue');
                    },
                    function(){
                        $(this).find('.aside-menu-inserted').removeClass('hover_displayTrue');
                    }
                )

                $('.hoverCatalogArenda').hover(
                    function(){
                        $(this).find('.aside-menu-insertedd').addClass('hover_displayTrue')
                    },
                    function(){
                        $(this).find('.aside-menu-insertedd').removeClass('hover_displayTrue')
                    }
                );
                $('.aside-menu-insertedd').hover(
                    function(){
                        $(this).find('.aside-menu-insertedd').addClass('hover_displayTrue');
                    },
                    function(){
                        $(this).find('.aside-menu-insertedd').removeClass('hover_displayTrue');
                    }
                )

                jQuery(function($){
                $(document).mouseup(function (e){ 
                    var div = $("#subheader"); 
                    if (!div.is(e.target) 
                        && div.has(e.target).length === 0) { 
                    $('.subheader_nav-mobile').removeClass('mobileMenuVis'); 
                    }
                });
                $('#subheader').click(
                    function(){
                        if($('.subheader_nav-mobile').hasClass('mobileMenuVis')){
                            $('.subheader_nav-mobile').removeClass('mobileMenuVis')
                            
                        }else {
                            $('.subheader_nav-mobile').addClass('mobileMenuVis')
                            
                        }
                       
                    },
                )
                });
                var Menu = {
  
                    el: {
                        ham: $('.menu'),
                        menuTop: $('.menu-top'),
                        menuMiddle: $('.menu-middle'),
                        menuBottom: $('.menu-bottom'),
                        activator: $('.button-catalogLaptop')
                    },
                    
                    init: function() {
                        Menu.bindUIactions();
                    },
                    
                    bindUIactions: function() {
                        Menu.el.activator
                            .on(
                            'click',
                            function(event) {
                            Menu.activateMenu(event);
                            event.preventDefault();
                        }
                        );
                    },
                    
                    activateMenu: function() {
                        Menu.el.menuTop.toggleClass('menu-top-click');
                        Menu.el.menuMiddle.toggleClass('menu-middle-click');
                        Menu.el.menuBottom.toggleClass('menu-bottom-click'); 
                    }
                    };

                    Menu.init();


                jQuery(function($){
                $(document).mouseup(function (e){ 
                    var div = $(".button-catalogLaptop"); 
                    if (!div.is(e.target) 
                        && div.has(e.target).length === 0) { 
                    $('.sidebarTablet').removeClass('active');
                    $('.menu-top').removeClass('menu-top-click');
                    $('.menu-middle').removeClass('menu-middle-click');
                    $('.menu-bottom').removeClass('menu-bottom-click');
                    }
                });    
                $('.button-catalogLaptop').click(
                    function(){
                        if($('.sidebarTablet').hasClass('active')){
                            $('.sidebarTablet').removeClass('active')
                        } else {
                            $('.sidebarTablet').addClass('active')
                        }
                    },
                )
                });

                $('.button_catalog').click(
                    function(){
                        if($('.sidebarMobile .sidebarMobile-catalog ul').hasClass('mobileMenuVis')){
                            $('.sidebarMobile .sidebarMobile-catalog ul').removeClass('mobileMenuVis')
                            $('body').removeClass('disable_scroll')
                        }else {
                            $('.sidebarMobile .sidebarMobile-catalog ul').addClass('mobileMenuVis')
                            $('.sidebarMobile .sidebarMobile-rent ul').removeClass('mobileMenuVis')
                            $('body').addClass('disable_scroll')
                        }
                       
                    },
                )

                $('.disable_catalog').click(
                    function(){
                        $('.sidebarMobile .sidebarMobile-catalog ul').removeClass('mobileMenuVis')
                        $('body').removeClass('disable_scroll')
                    }
                )

                // var script = document.createElement('script');
                // script.onload = function() {
                //     $('.popup-keepBuying').addClass('active');
                // };
                // script.src = "../../static/script.js";
                // document.getElementsByTagName('head')[0].appendChild(script);

                // $('#addCardSub').click(function() {
                //     if($(window).bind){
                //         $('.popup-keepBuying').addClass('active');
                //     }
                // })

                $('.close_form-success').click(function(){
                    $('.popup-keepBuying').removeClass('active');
                })

                $('.close_form-success_text').click(function(){
                    $('.popup-keepBuying').removeClass('active');
                })


                $('.button_rent').click(
                    function(){
                        if($('.sidebarMobile .sidebarMobile-rent ul').hasClass('mobileMenuVis')){
                            $('.sidebarMobile .sidebarMobile-rent ul').removeClass('mobileMenuVis')
                            $('body').removeClass('disable_scroll')
                        }else {
                            $('.sidebarMobile .sidebarMobile-rent ul').addClass('mobileMenuVis')
                            $('.sidebarMobile .sidebarMobile-catalog ul').removeClass('mobileMenuVis')
                            $('body').addClass('disable_scroll')
                        }
                       
                    },
                )

                $('.disable_rent').click(
                    function(){
                        $('.sidebarMobile .sidebarMobile-rent ul').removeClass('mobileMenuVis')
                        $('body').removeClass('disable_scroll')
                    }
                )
                


                $('.header_contact-button').click(
                    function(){
                        $('.block_mini-form').addClass('mini_form-block');
                    },  
                )
                $('.close_form-mini').click(
                     function(){
                        $('.block_mini-form').removeClass('mini_form-block');
                    }
                )
                $('.close_form-message').click(
                    function(){
                        $('.block_true').addClass('block_true-dis')
                    }
                )





                // BLOCK FAQ
                jQuery(document).ready(function($){

	var MqM= 768,
		MqL = 1024;

	var faqsSections = $('.faq-group'),
		faqTrigger = $('.trigger'),
		faqsContainer = $('.faq-items'),
		faqsCategoriesContainer = $('.categories'),
		faqsCategories = faqsCategoriesContainer.find('a'),
		closeFaqsContainer = $('.cd-close-panel');
	
	//select a faq section 
	faqsCategories.on('click', function(event){
		event.preventDefault();
		var selectedHref = $(this).attr('href'),
			target= $(selectedHref);
		if( $(window).width() < MqM) {
			faqsContainer.scrollTop(0).addClass('slide-in').children('ul').removeClass('selected').end().children(selectedHref).addClass('selected');
			closeFaqsContainer.addClass('move-left');
			$('body').addClass('cd-overlay');
		} else {
	        $('body,html').animate({ 'scrollTop': target.offset().top - 19}, 200); 
		}
	});

	//close faq lateral panel - mobile only
	$('body').bind('click touchstart', function(event){
		if( $(event.target).is('body.cd-overlay') || $(event.target).is('.cd-close-panel')) { 
			closePanel(event);
		}
	});
	faqsContainer.on('swiperight', function(event){
		closePanel(event);
	});


	faqTrigger.on('click', function(event){
		event.preventDefault();
		$(this).next('.faq-content').slideToggle(200).end().parent('li').toggleClass('content-visible');
	});

	$(window).on('scroll', function(){
		if ( $(window).width() > MqL ) {
			(!window.requestAnimationFrame) ? updateCategory() : window.requestAnimationFrame(updateCategory); 
		}
	});

	$(window).on('resize', function(){
		if($(window).width() <= MqL) {
			faqsCategoriesContainer.removeClass('is-fixed').css({
				'-moz-transform': 'translateY(0)',
			    '-webkit-transform': 'translateY(0)',
				'-ms-transform': 'translateY(0)',
				'-o-transform': 'translateY(0)',
				'transform': 'translateY(0)',
			});
		}	
		if( faqsCategoriesContainer.hasClass('is-fixed') ) {
			faqsCategoriesContainer.css({
				'left': faqsContainer.offset().left,
			});
		}
	});

	function closePanel(e) {
		e.preventDefault();
		faqsContainer.removeClass('slide-in').find('li').show();
		closeFaqsContainer.removeClass('move-left');
		$('body').removeClass('cd-overlay');
	}

	function updateCategory(){
		updateCategoryPosition();
		updateSelectedCategory();
	}

	function updateCategoryPosition() {
		var top = $('.faq').offset().top,
			height = jQuery('.faq').height() - jQuery('.categories').height(),
			margin = 20;
		if( top - margin <= $(window).scrollTop() && top - margin + height > $(window).scrollTop() ) {
			var leftValue = faqsCategoriesContainer.offset().left,
				widthValue = faqsCategoriesContainer.width();
			faqsCategoriesContainer.addClass('is-fixed').css({
				'left': leftValue,
				'top': margin,
				'-moz-transform': 'translateZ(0)',
			    '-webkit-transform': 'translateZ(0)',
				'-ms-transform': 'translateZ(0)',
				'-o-transform': 'translateZ(0)',
				'transform': 'translateZ(0)',
			});
		} else if( top - margin + height <= $(window).scrollTop()) {
			var delta = top - margin + height - $(window).scrollTop();
			faqsCategoriesContainer.css({
				'-moz-transform': 'translateZ(0) translateY('+delta+'px)',
			    '-webkit-transform': 'translateZ(0) translateY('+delta+'px)',
				'-ms-transform': 'translateZ(0) translateY('+delta+'px)',
				'-o-transform': 'translateZ(0) translateY('+delta+'px)',
				'transform': 'translateZ(0) translateY('+delta+'px)',
			});
		} else { 
			faqsCategoriesContainer.removeClass('is-fixed').css({
				'left': 0,
				'top': 0,
			});
		}
	}

	function updateSelectedCategory() {
		faqsSections.each(function(){
			var actual = $(this),
				margin = parseInt($('.faq-title').eq(1).css('marginTop').replace('px', '')),
				activeCategory = $('.categories a[href="#'+actual.attr('id')+'"]'),
				topSection = (activeCategory.parent('li').is(':first-child')) ? 0 : Math.round(actual.offset().top);
			
			if ( ( topSection - 20 <= $(window).scrollTop() ) && ( Math.round(actual.offset().top) + actual.height() + margin - 20 > $(window).scrollTop() ) ) {
				activeCategory.addClass('selected');
			}else {
				activeCategory.removeClass('selected');
			}
		});
	}
});