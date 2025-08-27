import justpy as jp
import json

import pandas
from datetime import datetime #For performing time based filtering
import matplotlib.pyplot as plt #To plot information and data.
my_data=pandas.read_csv("C:\\Users\\VEDANT\\Desktop\\DataVisualization\\reviews.csv",parse_dates=['Timestamp'])

def graphquasar():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="This graph represents course reviews analysis")

    hc = jp.HighCharts(a=wp)