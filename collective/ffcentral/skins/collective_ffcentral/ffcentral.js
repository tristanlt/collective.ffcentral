$(document).ready( function () {
	$("#ffc_navigation ul.subMenu").hide();
	$("#ffc_navigation li.toggleSubMenu span").each( function () {
		var TexteSpan = $(this).text();
        $(this).replaceWith('<a href="" title="Afficher le sous-menu">' + TexteSpan + '<\/a>') ;
    	} ) ;
    $("#ffc_navigation li.toggleSubMenu > a").click( function () {
        if ($(this).next("ul.subMenu:visible").length != 0) {
            $(this).next("ul.subMenu").slideUp("normal");
        }
        else {
            $("#ffc_navigation ul.subMenu").slideUp("normal");
            $(this).next("ul.subMenu").slideDown("normal");
        }
    return false;
    });
} ) ;