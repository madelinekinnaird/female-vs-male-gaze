from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np

## pull from spreadsheet to plot overall view
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os


import mysql.connector

#def init_connection():
#    return mysql.connector.connect(host='us-cdbr-east-05.cleardb.net', user = "b0a17d470a43c4", password = os.environ['PASSWORD_KEY'], database = "heroku_6b9bc07d291168b")
    #return psycopg2.connect(host = "localhost",port = 5432,database = "gaze_database",user = "postgres", password = os.environ['PASSWORD_KEY'])

#conn = init_connection()


#def run_query(query):
#    with conn.cursor() as cur:
#        cur.execute(query)
#        return cur.fetchall()

#def stretch_to_graph(sqlQuery,axis):
#    array = [float(int(val)) for val in  list(sqlQuery[axis][1:])]
#    return array

def getImage(path):
     return OffsetImage(plt.imread(path))

def app(df, rating1,rating2,rating3,rating4,rating5,rating6,rating7,rating8,rating9,rating10,rating11,rating12,rating13):
    femaleNum = len(df[df['ggt'] == 'female'])
    maleNum = len(df[df['ggt'] == 'male'])
    ## old sql query logic df[1][0]
    st.write("This plot shows the average response from", femaleNum,"girls/gays/theys (represented on the 'female gaze' axis) and from", maleNum, "people who listed 'other' (represented on the 'male gaze axis).")
    ## add title directly with grpah, relative average response
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
    #y = stretch_to_graph(df,1)
    #x = stretch_to_graph(df,0)

    x = list(df[df['ggt'] == 'female'].drop(['Unnamed: 0'],axis=1).mean())
    y = list(df[df['ggt'] == 'male'].drop(['Unnamed: 0'],axis=1).mean())


    fig, ax = plt.subplots(figsize = (10,9))
    plt.margins(x=0.25, y=0.25, tight=False)


    xmean = np.asarray(x).mean()
    ymean = np.asarray(y).mean()

    xrange= max(x)-min(x)
    yrange= max(y)-min(y)

    plt.axvline(xmean, c='#1077f4', ls='-',  linewidth=5) #male
    plt.text(xmean, ymean+(yrange*0.371), "Male Gaze", rotation=-90, verticalalignment='center', fontsize= 30, color = '#1077f4')

    plt.axhline(ymean, c='#f745a8', ls='-', linewidth=5) #female
    plt.text(xmean+(xrange*0.133), ymean+(yrange*.0428), "Female Gaze", rotation=0, verticalalignment='center', fontsize= 30, color = '#f745a8')

    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)
    #plt.axis('off')
    ax.scatter(x, y)
    for x0, y0, path in zip(x, y, paths):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)
    st.write(fig)
