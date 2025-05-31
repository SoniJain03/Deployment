import streamlit as st
import pandas as pd

st.title("Doing streamlit")
st.header("HI")
st.write("Hello Learners")



df=pd.DataFrame({
    'Name':['John','Adam','Bob','Mary'],
    'Marks':[78,92,61,85]
})
st.write(df)

st.write("Description of the dataframe")
st.write(df.describe())

st.write("Visualisation")
st.line_chart(df['Marks'])