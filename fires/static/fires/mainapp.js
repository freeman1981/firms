/**
 * Created by freeman on 06.09.15.
 */
//"use strict";
var url='fires';

$(function (){

    var map = L.map("map").setView([0, 0], 4);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6IjZjNmRjNzk3ZmE2MTcwOTEwMGY0MzU3YjUzOWFmNWZhIn0.Y8bhBaUMqFiPrDRW9hieoQ', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
            '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="http://mapbox.com">Mapbox</a>',
        id: 'mapbox.light'
    }).addTo(map);
    var gl;


    $('#from_date').datepicker();
    $('#to_date').datepicker();
    $('#go').click(function () {
        $.ajax({
            url: url,
            type: 'GET',
            data: {
                from_date: $('#from_date').val(),
                to_date: $('#to_date').val()
            },
            success: function (result, status, xhr) {
                var count = result.features.length;
                $('#count').html(count);
                if (gl != undefined) L.removeLayer(gl);
                gl = L.geoJson(result);
                gl.addTo(map);
            }
        });
    });

});