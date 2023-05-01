import streamlit as st

st.title('Hello World!')

name = 'Jungu Lee'
st.text(f'Your name is {name}')

st.markdown('This is **markdown**')
st.json(
    {'key1':'value1',
     'key2':'value2'}
)

import pandas as pd
st.subheader('IRIS data')
df = pd.read_csv('data/iris.csv')
st.dataframe(df)