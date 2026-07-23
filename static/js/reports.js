var document = window.document;
$(document).ready(function(){

    var $reportvar=$("#report");
    var $sortbyvar=$("#sortby");
    var $orderbyvar=$("#orderby");

    var $sortbyoptions=$sortbyvar.find('option');
    var $orderbyoptions=$orderbyvar.find('option');

    $sortbyvar.html($sortbyoptions.filter('[value=""]'));

    $reportvar.on('change',function(){
        $sortbyvar.html($sortbyoptions.filter('[parent="'+this.value+'"],[value=""]'));
        $('#sortby option[value=""]').prop('selected', true);
        $orderbyvar.html($orderbyoptions.filter('[parent="'+this.value+'"],[value=""]'));
        $('#orderby option[value=""]').prop('selected', true);

    });
});