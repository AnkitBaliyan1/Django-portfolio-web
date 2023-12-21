/* SPARKLINES */
require('jqvmap');
require('jqvmap/dist/maps/jquery.vmap.world');
require('jqvmap/dist/maps/jquery.vmap.usa');
const sample_data = require('jqvmap/examples/js/jquery.vmap.sampledata');
jQuery(function ($) {
    "use strict";
    var map = $(".jqv-map");
    map.each(function () {
        var $this = $(this);
        var options = getDataOptions( $this ? $this.data('options') : null );
        console.log(options);
        $this.vectorMap(options);
    });
});


