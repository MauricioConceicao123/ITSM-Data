import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
from sqlalchemy import create_engine
import matplotlib.ticker as mtick
import matplotlib.ticker as mticker
import datetime as dt
import numpy as np

st.title("ITSM Data Dashboard")
#choices for dropdown menu
options = ["Causes for Ticket Creation", "Impact & Urgency","Ticket Resolution Time", "Bananas(PLACEHOLDER)", "Horses(PLACEHOLDER)"]
st.sidebar.markdown("## Options")
st.sidebar.markdown("Please select a topic from the dropdown menu.")
choice = st.sidebar.selectbox("", options)
if choice == "Causes for Ticket Creation":
    df=pd.read_csv('ITSM_data.csv')
    proportions = df['Closure_Code'].value_counts(normalize=True)
    colors = sns.color_palette('coolwarm', n_colors=3)
    
    fig, ax = plt.subplots()
    fig, axes = plt.subplots (figsize=(12,6))
    ax=proportions.head(6).plot(kind='bar')
    st.write('From the data we extracted we were able to identify, post-resolution, the major sources for ticket creation')
    plt.title ('Major Causes of Ticket Creation')
    plt.xlabel('')
    plt.xticks(rotation=0)
    plt.ylabel('')
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1))
    st.pyplot(fig)
    st.write('The biggest share of tickets received by the incident management team do not have, currently, a particular source ("Other" with approximately 35.69%). Overall, we could observe that most tickets were created by software issues (approximately 28.23%)  than by the users themselves (approximately 7.70%), followed up by hardware and data-related issues')