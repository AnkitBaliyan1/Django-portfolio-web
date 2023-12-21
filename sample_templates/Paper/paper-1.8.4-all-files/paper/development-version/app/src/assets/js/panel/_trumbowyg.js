require('trumbowyg');
jQuery(function ($) {
    "use strict";
    var element = $("textarea.editor");
    var newdata =  {"autogrow": true, svgPath: 'assets/img/icon/icons.svg' };
    var options = {};
    element.each(function () {
        var $this = $(this);
        if(getDataOptions($this)){
            options = getDataOptions($this);
        }
        $.extend(true, options, newdata);
        console.log(options);
        $this.trumbowyg(options);
    }).on('tbwinit', function () {
        $('.trumbowyg-box').addClass('p-0 m-0 form-control');
    });
});
