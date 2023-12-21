
require('bootstrap-tagsinput');
jQuery(function ($) {
    "use strict";
    init_tagsInput();
});
var init_tagsInput = function () {
    let element = $(".tags-input");
    element.each(function () {
        var $this = $(this);
        var options = getDataOptions($this);
        $this.tagsinput(options);
    });
};
