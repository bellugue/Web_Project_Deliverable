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
                                return car.make + ' ' + car.model;
                            }));
                        },
                        error: function ajaxError(jqXHR) {
                            console.error('Error: ', jqXHR.responseText);
                        }
                    });
                },
                minLength: 2, // Mínim de caràcters per activar l'autocompletat
            });
        });