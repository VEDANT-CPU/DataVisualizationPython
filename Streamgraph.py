import justpy as jp
import json

import pandas
from datetime import datetime #For performing time based filtering
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("C:\\Users\\VEDANT\\Desktop\\DataVisualization\\reviews.csv",parse_dates=['Timestamp'])
my_data['Month'] = my_data['Timestamp'].dt.strftime("%Y-%m")
month_course_avg = my_data.groupby(['Month','Course Name']).mean(numeric_only=True).unstack()

chart_def = """
{
  "chart": {
    "type": "streamgraph",
    "marginBottom": 30,
    "zooming": { "type": "x" },
    "title": {
      "floating": true,
      "align": "left",
      "text": "Winter Olympic Medal Wins"
    },
    "subtitle": {
      "floating": true,
      "align": "left",
      "y": 30,
      "text": "Source: olympedia.org"
    },
    "yAxis": {
      "visible": false,
      "startOnTick": false,
      "endOnTick": false,
      "minPadding": 0.1,
      "maxPadding": 0.15
    },
    "legend": { 
      "enabled": false,
      "layout": "horizontal",
      "align": "center",
      "verticalAlign": "bottom"
    },
    "annotations": [{
      "labels": [
        {
          "point": { "x": 5.5, "xAxis": 0, "y": 30, "yAxis": 0 },
          "text": "CancelledduringWorld War II"
        },
        {
          "point": { "x": 18, "xAxis": 0, "y": 90, "yAxis": 0 },
          "text": "Soviet Union fell,Germany united"
        },
        {
          "point": { "x": 24.25, "xAxis": 0, "y": 140, "yAxis": 0 },
          "text": "Russia banned fromthe Olympic Games in 2017"
        }
      ],
      "labelOptions": {
        "backgroundColor": "rgba(255,255,255,0.5)",
        "borderColor": "silver"
      }
    }],
    "plotOptions": {
      "series": {
        "label": {
          "minFontSize": 5,
          "maxFontSize": 15,
          "style": { "color": "rgba(255,255,255,0.75)" }
        },
        "accessibility": { "exposeAsGroupOnly": true }
      }
    },
    "series": [
      { "name": "Finland", "data": [0,11,4,3,6,0,0,6,9,7,8,10,5,5,7,9,13,7,7,6,12,7,9,5,5,6,8] },
      { "name": "Austria", "data": [0,3,4,2,4,0,0,8,8,11,6,12,11,5,6,7,1,10,21,9,17,17,23,16,17,14,18] },
      { "name": "Sweden", "data": [0,2,5,3,7,0,0,10,4,10,7,7,8,4,2,4,8,6,4,3,3,7,14,11,15,14,18] },
      { "name": "Norway", "data": [0,17,15,10,15,0,0,10,16,4,6,15,14,12,7,10,9,5,20,26,25,25,19,23,26,39,37] },
      { "name": "U.S.", "data": [0,4,6,12,4,0,0,9,11,7,10,7,7,8,10,12,8,6,11,13,13,34,25,37,28,23,25] }
    ],
    "exporting": {
      "sourceWidth": 800,
      "sourceHeight": 600
    }
  }
}
"""

chart_dict = json.loads(chart_def)

def graphquasar():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="This graph represents course reviews analysis")

    hc = jp.HighCharts(a=wp, options= chart_dict)
    hc.options.xAxis.categories = list(month_course_avg.index)
    hc_data = [{"name" : v1, "data" : [v2 for v2 in month_course_avg['Rating'][v1]]} for v1 in month_course_avg['Rating']]
    hc.options.series = hc_data

    return wp

jp.justpy(graphquasar)