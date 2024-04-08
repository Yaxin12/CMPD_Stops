import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data #Add the caching decorator
def load_data(csv):
   df = pd.read_csv(csv)
   return df


stops = load_data("data/Officer_Traffic_Stops.csv")

alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=60)),  #,bin=True
    y='count()',
    tooltip = alt.Tooltip(['Driver_Age','count()'])
)

st.dataframe(stops)


