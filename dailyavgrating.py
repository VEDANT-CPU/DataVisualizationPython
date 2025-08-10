import justpy as jp

graph_def = """
{
    chart: {
        type: 'spline',
        inverted: true
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""
#Above javascript code is in json format.

def quazar1():
    wp = jp.QuasarPage() # we create QuasarPage(class) object
    #QDiv components of the web app.
    head1 = jp.QDiv(a=wp, text="This is a simple web app", classes="text-h1 text-center q-pt-xs")
    para1 = jp.QDiv(a=wp, text="This graph presents ratings of courses")
    #Adding Hichart components
    high_chart_component = jp.HighCharts(a=wp, options=graph_def) #justpy will convert json format
    #To dictionary then python can now manipulate and read this object.
    return wp

#Now, we need a function call to create and access the quasar page.
jp.justpy(quazar1) # Expects a function which returns a qausar page as its input.