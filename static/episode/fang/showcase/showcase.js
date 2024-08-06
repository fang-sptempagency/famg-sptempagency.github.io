$(function () {

            var showClass = 'show';

            contents = $('.mask').children();
            console.log(contents);

            contents.each(function (i, elem) {
                console.log(elem);
                $(window).on('load scroll resize', function () {
                    var winHeight = $(window).height();
                    var scrollTop = $(window).scrollTop();
                    var contentsPOS = $(elem).offset().top;

                    if (scrollTop >= contentsPOS - winHeight + 200) {
                        $(elem).addClass('show');
                    } else {
                        $(elem).removeClass('show');
                    }

                })
            });
        });