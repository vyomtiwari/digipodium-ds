import streamlit as st


import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

# title of the app
st.title('Data Analysis App')

st.cache_data()
def load_data(a):
    df  = pd.read_csv(f'/Users/vyom/Downloads/seaborn-data-master/{a}.csv')
    return df
with st.spinner('Loading data....'):
    df = load_data('titanic')
    st.write('👍🏾👍🏾👍🏾👍🏾')
