var dropzone =require('dropzone');

dropzone.options.fileUpload = {
    url: 'blackHole.php',
    addRemoveLinks: true,
    accept: function(file) {
        let fileReader = new FileReader();
        fileReader.readAsDataURL(file);
        fileReader.onloadend = function() {
            let content = fileReader.result;
            $('#file').val(content);
            file.previewElement.classList.add("dz-success");
        };
        file.previewElement.classList.add("dz-complete");
    }
};
jQuery(function ($) {
    "use strict";
    $(".dropzone").dropzone({ url: "#" });
});