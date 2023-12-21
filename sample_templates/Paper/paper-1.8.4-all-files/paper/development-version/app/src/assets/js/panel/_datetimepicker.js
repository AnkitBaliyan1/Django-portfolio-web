require('jquery-datetimepicker');
jQuery(function ($) {
    "use strict";
    init_DateTimePicker();
});

var init_DateTimePicker = function () {
    let element = $(".date-time-picker");
    element.each(function () {
        var $this = $(this);
        var options = getDataOptions($this);
        $this.datetimepicker(options);
    });
};
