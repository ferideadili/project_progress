 var drawStaticChart = (function(datas,selected_option,container){
            $("#"+container).empty();
            var series_data = [];
              if (selected_option=="stock" || option=="healthcare") {
                  var drilldown_series = [];
              }
            if (selected_option==""){
                selected_option="customer_satisfaction";
            }
            $(datas[option][0][selected_option]).each(function(index,item){

                var serie={};
                serie['y']=item['percentage'];
                serie['name']=item['period'];
                serie['drilldown']=item['period'];// first level
                series_data.push(serie);

                if (selected_option=="stock" || option=="healthcare"){

                    var drilldown_serie_regions = {
                        "name": item['period'],
                        "id": item["period"],
                        "data": []
                    };
                    $(item['region']).each(function(index_region,item_region) {
                        drilldown_serie_regions['data'].push({
                            "name": item_region['city'],
                            "y": item_region['amount'],
                            "drilldown": item_region['city']
                        });//second level

                         if (selected_option == "customer_satisfaction" && option == "healthcare"){
                            var drilldown_serie_hospitals = {
                                "name": item_region['city'],
                                "id": item_region["city"],
                                "data": []
                            };
                            $(item_region['hospitals']).each(function (index_hospital, item_hospital) {
                                drilldown_serie_hospitals['data'].push({
                                    "name": item_hospital['hospital'],
                                    "y": item_hospital['amount']
                                });
                            });
                            drilldown_series.push(drilldown_serie_hospitals);
                        }
                    });
                     drilldown_series.push(drilldown_serie_regions);
                }
            });

            var chart = $('#'+container).highcharts({
             chart: {
                    plotBackgroundColor: null,
                    plotBorderWidth: null,
                    plotShadow: false,
                    type: "column"
                },
                xAxis: {
                    type: 'category'
                },
                title: {
                    text: ""
                },
                tooltip: {
                    backgroundColor: "rgba(255,255,255,1)",
                    style: {
                        fontSize: '10pt'
                    },

                },
                series: [{
                    showInLegend: true,
                    colorByPoint: true,
                    data: series_data
                }],
                drilldown: {
                    drillUpButton: {
                        position: {
                            align: 'right'
                        }
                    },
                    series: drilldown_series
                }
            });
            return chart;
        });