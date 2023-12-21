require('bootstrap-colorpicker');
jQuery(function ($) {
    "use strict";
    var picker = $(".color-picker");
    picker.each(function () {
        var $this = $(this);
        var options = getDataOptions($this);
        console.log(options);
        $this.colorpicker(options);
    });
});
