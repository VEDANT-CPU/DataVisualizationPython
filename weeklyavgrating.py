import justpy as jp
import json
#Code from BuildingPlot.ipnyb. To load the dataframe.
import pandas
from datetime import datetime #For performing time based filtering
from pytz import utc #To set utc as timezone in my datetime() calls
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("C:\\Users\\VEDANT\\Desktop\\DataVisualization\\reviews.csv",parse_dates=['Timestamp']) #Pass parse_dates to instruct python which column is to be read as datetime.
my_data['Week']=my_data['Timestamp'].dt.strftime('%Y %U')
week_avg=my_data.groupby(['Week']).mean(numeric_only=True)
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
  "legend": {
    "layout": "vertical",
    "align": "right",
    "verticalAlign": "middle"
  },
  "plotOptions": {
    "series": {
      "label": {
        "connectorAllowed": false
      }
    }
  },
  "series": [
    {
      "name": "Avg course rating of week",
      "data": [
        43934, 48656, 65165, 81827, 112143, 142383,
        171533, 165174, 155157, 161454, 154610, 168960, 171558
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
    #Now we acces the keys of hc.options daictionary through dot notation.
    hc.options.title.text = 'Weekly average course rating plot'
    #hc.options.subtitle.text = 'weekly'
    hc.options.yAxis.title.text = 'Ratings'
    #hc.options.xaxis.accessibility.rangeDescription = 'Range: 2018 to 2021'
    #hc.options.plotOptions.pointStart = 2018
    hc.options.xAxis.categories = list(week_avg.index)
    #remove the xAxis block from json variable because you have set xAxis through categories.
    #Also remove pointStart from plotOptions in the json variable.
    hc.options.series[0].data = list(week_avg['Rating'])

    return wp

#Now, we need a function call to create and access the quasar page.
jp.justpy(quazar1) # Expects a function which returns a qausar page as its input.