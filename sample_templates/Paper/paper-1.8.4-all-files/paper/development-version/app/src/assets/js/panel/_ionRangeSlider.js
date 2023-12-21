require('ion-rangeslider');
jQuery(function ($) {
    "use strict";
    init_rangeSlider();
});

var init_rangeSlider = function () {
    let element = $(".range-slider");
    element.each(function () {
        var $this = $(this);
        var options = getDataOptions($this);
        $this.ionRangeSlider(options);
    });
};



