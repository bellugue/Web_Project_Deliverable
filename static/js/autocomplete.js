$(document).ready(function() {
    $("#model").autocomplete({
        source: function( request, response ) {
            $.ajax({
                url: "/api/explore/v2.1/catalog/datasets/all-vehicles-model/records?select=make",
                dataType: "jsonp",
                data: {
                    featureClass: "make",
                    type: "json",
                    maxRows: 10,
                    name_startsWith: request.term,
                },
                success: function( data ) {
                    response( $.map( data.make, function( item ) {
                        return {
                            label: item.make,
                            value: item.make
                        }
                    }));
                }
            });
        },
        minLength: 2,
        select: function( event, ui ) {
            if (ui.item) {
                $("#model").val(ui.item.make);
            }
        }
    });
});