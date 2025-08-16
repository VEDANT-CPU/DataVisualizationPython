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

week_def = '''
{
  "title": {
    "text": "U.S Solar Employment Growth",
    "align": "left"
  },
  "subtitle": {
    "text": "By Job Category. Source: IREC.",
    "align": "left"
  },
  "yAxis": {
    "title": {
      "text": "Number of Employees"
    }
  },
  "xAxis": {
    "accessibility": {
      "rangeDescription": "Range: 2010 to 2022"
    }
  },
  "legend": {
    "layout": "vertical",
    "align": "right",
    "verticalAlign": "middle"
  },
  "plotOptions": {
    "series": {
      "label": {
        "connectorAllowed": false
      },
      "pointStart": 2010
    }
  },
  "series": [
    {
      "name": "Installation & Developers",
      "data": [
        43934, 48656, 65165, 81827, 112143, 142383,
        171533, 165174, 155157, 161454, 154610, 168960, 171558
      ]
    },
    {
      "name": "Manufacturing",
      "data": [
        24916, 37941, 29742, 29851, 32490, 30282,
        38121, 36885, 33726, 34243, 31050, 33099, 33473
      ]
    },
    {
      "name": "Sales & Distribution",
      "data": [
        11744, 30000, 16005, 19771, 20185, 24377,
        32147, 30912, 29243, 29213, 25663, 28978, 30618
      ]
    },
    {
      "name": "Operations & Maintenance",
      "data": [
        null, null, null, null, null, null, null,
        null, 11164, 11218, 10077, 12530, 16585
      ]
    },
    {
      "name": "Other",
      "data": [
        21908, 5548, 8105, 11248, 8989, 11816, 18274,
        17300, 13053, 11906, 10073, 11471, 11648
      ]
    }
  ],
  "responsive": {
    "rules": [
      {
        "condition": {
          "maxWidth": 500
        },
        "chartOptions": {
          "legend": {
            "layout": "horizontal",
            "align": "center",
            "verticalAlign": "bottom"
          }
        }
      }
    ]
  }
}
'''
week_def_dict = json.loads(week_def)

def quazar1():
    wp = jp.QuasarPage() # we create QuasarPage(class) object
    #QDiv components of the web app.
    head1 = jp.QDiv(a=wp, text="This is a weekly avg plot", classes="text-h1 text-center q-pt-xs")
    para1 = jp.QDiv(a=wp, text="This graph presents ratings of courses")

    hc = jp.HighCharts(a = wp, options = week_def_dict)
    return wp

#Now, we need a function call to create and access the quasar page.
jp.justpy(quazar1) # Expects a function which returns a qausar page as its input.