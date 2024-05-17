$(document).ready(function() {
    $('#id_model').autocomplete({
        source: function(request, response) {
            $.ajax({
                method: 'GET',
                url: 'https://api.api-ninjas.com/v1/cars?model=' + request.term,
                headers: { 'X-Api-Key': 'ZGFv6p+JoxwKPcoGvhZmvQ==Cftj0BRA00cDhFJV' },
                contentType: 'application/json',
                success: function(result) {
                    response(result.map(function(car) {
                        return {
                            label: car.make + ' ' + car.model,
                            value: car.make + ' ' + car.model
                        };
                    }));
                },
                error: function ajaxError(jqXHR) {
                    console.error('Error: ', jqXHR.responseText);
                }
            });
        },
        minLength: 2,
        open: function() {
            // Custom styles when menu is opened
            $(".ui-autocomplete").css({
                "background-color": "white",
                "border": "1px solid #ddd",
                "max-height": "400px",
                "overflow-y": "auto",
                "overflow-x": "hidden",
                "z-index": "1000"
            });
            $(".ui-menu-item").css({
                "padding": "10px",
                "font-size": "14px",
                "cursor": "pointer"
            });
            $(".ui-menu-item:hover").css({
                "background-color": "#f0f0f0"
            });
        }
    });
});
