from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np

## pull from spreadsheet to plot overall view
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox




def app(df, rating1,rating2,rating3,rating4, rating5, rating6, rating7, rating8, rating9,rating10, rating11, rating12, rating13):


    def getImage(path):
         return OffsetImage(plt.imread(path))

    paths = [
    'images/adam_driver.png',
    'images/ryan_reynolds.png',
    'images/dev_patel.png',
    'images/pete_davidson.png',
    'images/robert_pattinson.png',
    'images/michael_cera.png',
    'images/donald_glover.png',
    'images/harry_styles.png',
    'images/chris_hemsworth.png',
    'images/benedict_cumberbatch.png',
    'images/john_krasinski.png',
    'images/timothee_chalamet.png',
    'images/michael_b_jordan.png']

    # logic to map points to graph
    x = [rating1,rating2,rating3,rating4,rating5,rating6,rating7,rating8,rating9,rating10,rating11,rating12,rating13]
    y = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    fig, ax = plt.subplots(figsize = (10,6))
    plt.margins(x=0.01, y=0.01, tight=False)
    plt.axhline(0, c='gray', ls='-')
    plt.axis('off')
    ax.scatter(x, y)
    for x0, y0, path in zip(x, y, paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)
    st.write(fig)
