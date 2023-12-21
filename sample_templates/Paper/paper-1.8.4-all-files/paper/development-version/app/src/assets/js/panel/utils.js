

$(document).ready(function() {

    //CheckBox List
    $("#checkedAll").change(function(){
        if(this.checked){
            $(".checkSingle").each(function(){
                this.checked=true;
            })
        }else{
            $(".checkSingle").each(function(){
                this.checked=false;
            })
        }
    });
    $(".checkSingle").click(function () {
        if ($(this).is(":checked")){
            var isAllChecked = 0;
            $(".checkSingle").each(function(){
                if(!this.checked)
                    isAllChecked = 1;
            })
            if(isAllChecked == 0){ $("#checkedAll").prop("checked", true); }
        }else {
            $("#checkedAll").prop("checked", false);
        }
    });


    // switch toggle
    $("input[type=checkbox]").click(function(event) {

        var checkBox = $(this);
        $('someSwitchOptionDefault').prop( "checked", true );
        console.log($('someSwitchOptionDefault').is(":checked"));

        // if (checkBox.is(":checked")){
        //     checkBox.prop("checked", false);
        // }else{
        //     checkBox.prop("checked", true);
        // }
    });
    //tabs hash
    //
    // var hash = window.location.hash;
    // hash && $('ul.nav a[href="' + hash + '"]').tab('show');
    //
    // $('.sidebar-menu .nav-tabs a').click(function (e) {
    //     $(this).tab('show');
    //     var scrollmem = $('body').scrollTop();
    //     window.location.hash = this.hash;
    //     $('html,body').scrollTop(scrollmem);
    // });
});