#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 19:03:03 2020

@author: raphaele
"""

# code for viz app to view the ict_data
# ICT data in Europe 2010-2020
# Employed persons with ICT education by sex [isoc_ski_itsex]
# Source: http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=isoc_ski_itsex&lang=en


import streamlit as st
import pandas as pd
import plotly.express as px

# import and cache the data
@st.cache(persist=True, suppress_st_warning=True)
def load_data():
    df = pd.read_csv('ict_data.csv')
    return df

# main function
def main():
    df_data = load_data()
    st.image("image.png")
    '''
    Gender (percentage) of employed people with ICT (Information 
    and Communication Technology) education in European countries from 2010 to 2019. Only 
    female and male genders are represented as per data available in the 
    [Eurostat database](http://appsso.eurostat.ec.europa.eu/nui/show.do?dataset=isoc_ski_itsex&lang=en).
    You can select a year and add or remove countries with the options in the
    left side bar. "All Europe" shows the general proportions for all European
    countries.
    '''
    sel_year = st.sidebar.slider('Select a year', min_value=2010, max_value=2019, value=2019, step=1)
    all_countries = list(df_data['geo'].unique())
    countries = st.sidebar.multiselect('Add or remove countries', list(df_data['geo'].unique()), default = all_countries)
    # new data set filtered as per user selection
    new_df = df_data[(df_data['year'] == sel_year) & (df_data['geo'].isin(countries)) ]
    # bar chart
    fig = px.bar(new_df, 
                 x ='geo',
                 y='value', 
                 color = 'gender', 
                 color_discrete_sequence = ['#BEC7BD', '#CDB7CD'],
                 labels={
                     'value': '',
                     'geo': '',
                     'gender': 'Gender'},
                 width = 800,
                 height = 350)
    fig.update_layout(yaxis_tickformat = '%',
                      margin=dict(l=0, r=0, t=0, b=0, pad=0))
    # display the chart
    st.plotly_chart(fig)

# call main function       
if __name__ == "__main__":
    main()
    
    
    