import streamlit as st
import pickle
import pandas as pd
import numpy as np

st.set_page_config(page_title='Demo')

with open('df.pkl', 'rb') as file:
    df = pickle.load(file)

with open('pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.header('Enter your inputs for the desired flat')
bedroom = float(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
bathroom = float(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
balcony = float(st.selectbox('Number of Balconies', sorted(df['balcony'].unique().tolist())))
floor = float(st.selectbox('Floor Number', sorted(df['floorNum'].unique().tolist())))
age = st.selectbox('Flat Age', sorted(df['agePossession'].unique().tolist()))
sector = st.selectbox('Sector', sorted(df['Location'].unique().tolist()))
area = float(st.number_input('Built Up Area'))
servant = (st.selectbox('Servant_Room', ['Yes', 'No']))
if servant == 'Yes':
    servant = 1
else:
    servant = 0
furnishing = (st.selectbox('Furnishing type', sorted(df['furnishing_type'].unique().tolist())))
luxury = (st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist())))

if st.button('Predict Price'):
    data = [[bedroom,bathroom,balcony,floor,age,sector,servant,area,furnishing,luxury]]
    columns = ['bedRoom','bathroom','balcony','floorNum','agePossession','Location','Servant_Room','Built_Up_Area','furnishing_type','luxury_category']
    df = pd.DataFrame(data,columns=columns)
    transformed_data = pipeline.named_steps['transformer'].transform(df)
    base_price = pipeline.predict(df)[0]
    low = round(base_price - 15)
    high = round(base_price + 15)
    st.text("Price of flat is between {} Lac and {} Lac".format(low,high))
