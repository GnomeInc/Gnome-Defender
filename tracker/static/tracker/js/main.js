/**
 * Created by eric.kuha on 3/4/2016.
 * Copyright GnomeInc, Some Rights Reserved
 *
 */

jQuery(document).ready(function($){
    $(".clickable-row").click(function(){
       window.document.location = $(this).data("href");
    });
});