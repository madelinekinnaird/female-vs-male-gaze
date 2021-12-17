from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np

## pull from spreadsheet to plot overall view
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os
import psycopg2


import mysql.connector

def init_connection():
    return mysql.connector.connect(host='127.0.0.1',port = 3306, user = "monty", password = "Bdflmnptv1!", database = "gazes")
    #return psycopg2.connect(host = "localhost",port = 5432,database = "gaze_database",user = "postgres", password = os.environ['PASSWORD_KEY'])

conn = init_connection()


def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

def stretch_to_graph(sqlQuery,axis):
    array = [float(int(val)) for val in  list(sqlQuery[axis][1:])]
    #multiplier = float(1000/(max(queryList) - min(queryList)))
    #array = np.asarray(queryList)*multiplier
    #array = [val - 50.0 for val in queryList]

    return array

def getImage(path):
     return OffsetImage(plt.imread(path))

def app(df, rating1,rating2,rating3,rating4,rating5,rating6,rating7,rating8,rating9,rating10,rating11,rating12,rating13):

    st.write("This plot shows the average response from", df[0][0],"girls/gays/theys (represented on the 'female gaze' axis) and from", df[1][0], "people who listed 'other' (represented on the 'male gaze axis).")
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

    #raw_code = '''SELECT count(*), AVG(man1) man1, AVG(man2) man2, AVG(man3) man3, AVG(man4) man4, AVG(man5) man5, AVG(man6) man6, AVG(man7) man7, AVG(man8) man8, AVG(man9) man9, AVG(man10) man10, AVG(man11) man11, AVG(man12) man12, AVG(man13) man13 FROM gaze_database GROUP BY ggt'''
    #df = run_query(raw_code)
    # logic to map points to graph
    y = stretch_to_graph(df,1)
    x = stretch_to_graph(df,0)


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
