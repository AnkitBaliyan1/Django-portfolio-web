require('smartwizard');
jQuery(function ($) {
    "use strict";
    init_stepper();
});
var init_stepper = function () {
    let element = $(".stepper");
    element.each(function () {
        var $this = $(this);
        var options = getDataOptions($this);
        $this.smartWizard(options);
    });
};
