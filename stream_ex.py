# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 09:57:51 2022

@author: mdhami
"""

import streamlit as st

import pandas as pd

def main():

    st.header('Wind farm')
    st.sidebar.header('WisualizeWind',)
    with st.sidebar:
        add_radio = st.radio(
            "File select options",
            ("Choose a trigger file","Last received trigger file")
        )
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "76%", "4%")
    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = pd.read_csv('Advantech.csv')
    #data = np.random.randn(10, 1)
    
    tab1.subheader("A tab with a temperature chart")
    tab1.line_chart(data['AI_0 Evt'])
    
    tab2.subheader("A tab with the data")
    tab2.write(data)
    
if __name__ == "__main__":
    main()
