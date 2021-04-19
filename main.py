"""
Created on Mon Apr 19 14:56:36 2021

@author: winnyyip
"""


import pandas as pd
import plotly_clab as pc

# data preparation

data = pd.DataFrame({'region':['Asia','North America','South America', 'Middle East', 'South East Asia', 'Europe', 'Africa'],
                     'value':[10,40,50,60,30,25,46]})

data2 = pd.DataFrame({'Quarter': ['2020-Q2','2020-Q3','2020-Q4','2021-Q1'],
 'Purpose':	[70,66,65,64],
 'Support':	[58,53,51,52],
 'Self':  	[50,47,46,48,],
 'Balance':  [41,42,41,41]})

data3 = pd.read_excel('scores.xlsx')


# horizontal bar plot
bar_div  = pc.plot_bar_horizontal(data, 'region', 'value', 'Engagement Score by Region')


# line plot
line_div = pc.plot_line(data2, 'Quarter', ['Purpose','Support','Self','Balance'], "text+name", "Wellbeing scores by Quarter")


# scatter plot
scatter_div = pc.plot_scatter(data3, 'eng_1', 'eng_5', 'size', 'bm_industry', 'Correlation of Eng 1 to Eng 5 by Industry')


# prepare html to insert graphs
plotlyjs = """
<head>
  <link rel="stylesheet" href="https://d1vmr11cgrgrrj.cloudfront.net/7834392/css/fonts.css">
  <link rel="stylesheet" type="text/css" href="style.css">
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <script>
  function myFunction(elementid) {
      var x = document.getElementById(elementid);
      if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
  }
  </script>
</head>"""  

html = plotlyjs 
html += "{}{}{}".format(bar_div, line_div, scatter_div) 

n = open("graphs.html", "w")
n.write(html)
n.close()