import justpy as jp
import json
#Code from BuildingPlot.ipnyb. To load the dataframe.
import pandas
from datetime import datetime #For performing time based filtering
from pytz import utc #To set utc as timezone in my datetime() calls
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("C:\\Users\\VEDANT\\Desktop\\DataVisualization\\reviews.csv",parse_dates=['Timestamp']) #Pass parse_dates to instruct python which column is to be read as datetime.
my_data['Day']=my_data['Timestamp'].dt.date
day_avg=my_data.groupby(['Day']).mean(numeric_only=True)
#End of code from BuildingPlot.ipnyb

graph_def = """
{
  "chart": {
    "type": "spline",
    "inverted": false
  },
  "title": {
    "text": "Daily Average Rating"
  },
  "subtitle": {
    "text": "According to reviews.csv"
  },
  "xAxis": {
    "reversed": false,
    "title": {
      "enabled": true,
      "text": "Day"
    },
    "labels": {
      "format": "{value} km"
    },
    "accessibility": {
      "rangeDescription": "Range: 0 to 80 km."
    },
    "maxPadding": 0.05,
    "showLastLabel": true
  },
  "yAxis": {
    "title": {
      "text": "Rating"
    },
    "labels": {
      "format": "{value}°"
    },
    "accessibility": {
      "rangeDescription": "Range: 0 to 5."
    },
    "lineWidth": 2
  },
  "legend": {
    "enabled": false
  },
  "tooltip": {
    "headerFormat": "<b>{series.name}</b><br/>",
    "pointFormat": "{point.x} {point.y}"
  },
  "plotOptions": {
    "spline": {
      "marker": {
        "enable": false
      }
    }
  },
  "series": [
    {
      "name": "Temperature",
      "data": [
        [0, 15],
        [10, -50],
        [20, -56.5],
        [30, -46.5],
        [40, -22.1],
        [50, -2.5],
        [60, -27.7],
        [70, -55.7],
        [80, -76.5]
      ]
    }
  ]
}
"""
#Above javascript code is in json format.

def quazar1():
    wp = jp.QuasarPage() # we create QuasarPage(class) object
    #QDiv components of the web app.
    head1 = jp.QDiv(a=wp, text="This is a simple web app", classes="text-h1 text-center q-pt-xs")
    para1 = jp.QDiv(a=wp, text="This graph presents ratings of courses")
    #Adding Hichart components
    graph_def_dict = json.loads(graph_def)

    high_chart_component = jp.HighCharts(a=wp, options=graph_def_dict) #justpy will convert json format
    #To dictionary then python can now manipulate and read this object.
    #high_chart_component.options is a special kind of dictionary as it allows
    #to access its keys through dot notation.
    high_chart_component.options.title.text = "Average rating by day"
    #Changing data of the plot.
    #Taking data from a table store it in 2 array then graph it
    high_chart_component.options.xAxis.categories = list(day_avg.index)
    high_chart_component.options.series[0].data = list(day_avg['Rating'])
    print(high_chart_component.options)

    return wp

#Now, we need a function call to create and access the quasar page.
jp.justpy(quazar1) # Expects a function which returns a qausar page as its input.