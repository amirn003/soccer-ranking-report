#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pandas as pd
import numpy as np
import jinja2
import os

def generateReport(df, content, count, today, report):
    ''' 
    Generate Report

    Parameters
    ----------
    df : dataframe   
    content : feature content  
    count : number of panel
    today: date
    
    '''

    '''
    def color_negative_red(val):
        color = 'red' if val < 0 else 'black'
        return f'color: {color}'

    styler = df.style.applymap(color_negative_red)
    '''

    styler = df.style

    # Template handling
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath=''))
    template = env.get_template('template/template.html')
    html = template.render(my_table=styler.render())

    # Write the HTML file
    with open(f'{report}/{content}_report.html', 'w') as f:
        f.write(f"<h1>Gene Panel Report: {content}</h1>")
        f.write(html)
        f.write(f"<h3>League number: {count}</h3><br>")

