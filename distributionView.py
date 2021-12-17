from collections import namedtuple
import math
import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image

## pull from spreadsheet to plot overall view
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

import mysql.connector
import os
import psycopg2

def init_connection():
   return mysql.connector.connect(host='127.0.0.1',port = 3306, user = "monty", password = "Bdflmnptv1!", database = "gazes")
    #return psycopg2.connect(host = "localhost",port = 5432,database = "gaze_database",user = "postgres", password = os.environ['PASSWORD_KEY'])

conn = init_connection()

def run_query(query):

    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()



def plot_distribution(col, man, rating, jitterpoints):
    raw_code = '''SELECT {0}, ggt FROM gaze_database'''.format(col)
    df = pd.read_sql(raw_code, conn)

    test_image = 'images_original/' + man +'.png'
    # plot it
    fig, (a0, a2, a1) = plt.subplots(1, 3, gridspec_kw={'width_ratios': [1, 4, 4]}, figsize = (10,2))
    img = plt.imread(test_image)
    a0.imshow(img)
    a0.spines['right'].set_visible(False)
    a0.spines['top'].set_visible(False)
    a0.spines['left'].set_visible(False)
    a0.spines['bottom'].set_visible(False)
    a0.axes.xaxis.set_ticks([])
    a0.axes.yaxis.set_ticks([])
    man_name = man.replace('_', ' ').title()
    a0.set_xlabel(man_name)

    x1 = df[df['ggt'] == 'female'][col]
    x2 = df[df['ggt'] == 'male'][col]
    y1 = jitterpoints[0:len(x1)]
    y2 = jitterpoints[0:len(x2)]

    a1.scatter(x1, y1, s = 100, alpha = .4, color = '#f745a8') #female
    a1.set_xlim([0, 100])
    a1.set_ylim([0, 40])
    a1.spines['right'].set_visible(False)
    a1.spines['top'].set_visible(False)
    a1.spines['left'].set_visible(False)
    a1.spines['bottom'].set_color('gray')
    a1.tick_params(axis='x', colors='gray')
    a1.axes.yaxis.set_ticks([])
    ## your rating
    a1.scatter(rating,20, s= 300, alpha = 0.4, color = '#282828')
    a1.text(rating,20,'Your Rating',horizontalalignment='center')

    a2.scatter(x2, y2, s = 100, alpha = 0.4, color = '#1077f4') #male
    a2.set_xlim([0, 100])
    a2.set_ylim([0, 40])
    a2.spines['right'].set_visible(False)
    a2.spines['top'].set_visible(False)
    a2.spines['left'].set_visible(False)
    a2.spines['bottom'].set_color('gray')
    a2.tick_params(axis='x', colors='gray')
    a2.axes.yaxis.set_ticks([])
    ## your rating
    a2.scatter(rating, 20, s= 300, alpha = .4, color = '#282828')
    a2.text(rating, 20,'Your Rating',horizontalalignment='center')

    st.write(fig)


def app(df, rating1,rating2,rating3,rating4,rating5,rating6,rating7,rating8,rating9,rating10,rating11,rating12,rating13):
    import matplotlib.pyplot as plt
    import numpy as np

    my_file = open("jitterpoints.txt", "r")
    content = my_file.read()
    results = content.split(",")
    jitterpoints = list(map(int, results))

    #random data for category A, B, with B "taller"
    plot_distribution('man1', 'adam_driver', rating1, jitterpoints)
    plot_distribution('man2', 'ryan_reynolds', rating2, jitterpoints)
    plot_distribution('man3', 'dev_patel', rating3, jitterpoints)
    plot_distribution('man4', 'pete_davidson', rating4, jitterpoints)
    plot_distribution('man5', 'robert_pattinson', rating5, jitterpoints)
    plot_distribution('man6', 'michael_cera', rating6, jitterpoints)
    plot_distribution('man7', 'donald_glover', rating6, jitterpoints)
    plot_distribution('man8', 'harry_styles', rating6, jitterpoints)
    plot_distribution('man7', 'chris_hemsworth', rating6, jitterpoints)
    plot_distribution('man8', 'benedict_cumberbatch', rating6, jitterpoints)
    plot_distribution('man8', 'john_krasinski', rating6, jitterpoints)
    plot_distribution('man8', 'timothee_chalamet', rating6, jitterpoints)
    plot_distribution('man9', 'michael_b_jordan', rating6, jitterpoints)
