import justpy as jp
import json

import pandas
from datetime import datetime #For performing time based filtering
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("reviews.csv",parse_dates=['Timestamp']) #Pass parse_dates to instruct python which column is to be read as datetime.
my_data['Month'] = my_data['Timestamp'].dt.strftime("%Y %m")
month_avg = my_data.groupby(['Month']).mean(numeric_only=True)

chart_def = '''
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
'''
chart_dict = json.loads(chart_def)

def myquasar():
    wp = jp.QuasarPage()
    hed = jp.QDiv(a=wp, text="Monthly Avg Rating", classes="text-h2 text-weigth-light")
    para = jp.QDiv(a=wp, text="Below is the plot of monthly ratings")
    hc = jp.HighCharts(a=wp, options=chart_dict)
    hc.options.xAxis.categories = list()

    return wp