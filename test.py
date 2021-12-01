from collections import namedtuple
import altair as alt
import math
import pandas as pd
import plotly.express as px
import streamlit as st

## put it on the internet
# https://towardsdatascience.com/show-your-ml-project-to-the-internet-in-minutes-2a7bc3167bd0

## plotly events
# https://github.com/null-jones/streamlit-plotly-events/blob/master/README.md

## google sheets
#https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550
# https://stackoverflow.com/questions/61484573/how-can-one-write-to-a-publicly-available-google-sheet-without-authorization-i


"""
# Welcome to Streamlit!
Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
In the meantime, below is an example of what you can do with just a few lines of code:
"""
test = """
<iframe src="https://docs.google.com/forms/d/e/1FAIpQLSegpZENRtp3OGe2_aVJmRGy7vupRpiwH4A9fqxKw3Y7KolMPA/viewform?embedded=true" width="640" height="446" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
"""




st.markdown(test, unsafe_allow_html = True)

## plot for each dude
import streamlit as st
from streamlit_plotly_events import plotly_events

# Writes a component similar to st.write()
fig = px.scatter(x=[1,2,3], y=[1,2,3]).add_layout_image(
        dict(
            source="https://images.plot.ly/language-icons/api-home/python-logo.png",
            xref="x",
            yref="y",
            x=0,
            y=3,
            sizex=2,
            sizey=2,
            sizing="stretch",
            opacity=0.5,
            layer="below")
)
selected_points = plotly_events(fig)


## do a thing for selected point
st.write(selected_points)



## pull from spreadsheet to plot overall view
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
    return OffsetImage(plt.imread(path))

paths = [
    'images/ryan_reynolds.png',
    'images/dev_patel.png',
    'images/michael_b_jordan.png',
    'images/harry_styles.png']

x = [200,1400,1200,1350]
y = [550,1000,500,1250]


img = plt.imread("gaze_background.png")
fig, ax = plt.subplots(figsize=(9, 10))
ax.imshow(img)
ax.scatter(x, y)


for x0, y0, path in zip(x, y, paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    ax.add_artist(ab)


if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
