import justpy as jp
import json

import pandas
from datetime import datetime #For performing time based filtering
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("C:\\Users\\VEDANT\\Desktop\\DataVisualization\\reviews.csv",parse_dates=['Timestamp'])
my_data['DayofWeek'] = my_data['Timestamp'].dt.strftime("%A")
my_data['Daynum'] = my_data['Timestamp'].dt.strftime('%w')
week_day_avg = my_data.groupby(['DayofWeek', 'Daynum']).mean(numeric_only=True)
week_day_avg = week_day_avg.sort_values('Daynum')

chart_def = """
{
  "chart": {
    "type": "spline",
    "inverted": false
  },
  "title": {
    "text": "Aggregated Average Ratings by Day of the Week"
  },
  "subtitle": {
    "text": "According to the Course reviews dataset"
  },
  "xAxis": {
    "reversed": false,
    "title": {
      "enabled": true,
      "text": "Day"
    },
    "labels": {
      "format": "{value}"
    },
    "accessibility": {
      "rangeDescription": "Range: 0 to 5 km."
    },
    "maxPadding": 0.05,
    "showLastLabel": true
  },
  "yAxis": {
    "title": {
      "text": "Rating"
    },
    "labels": {
      "format": "{value}"
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
chart_dict = json.loads(chart_def)

def quasar3():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="This graph represents course reviews analysis")
    hc = jp.HighCharts(a=wp, options=chart_dict)

    hc.options.xAxis.categories = list(week_day_avg.index.get_level_values(0))
    hc.options.series[0].data = list(week_day_avg['Rating'])

    return wp

jp.justpy(quasar3)
    