import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config('Plotting ')
st.title('Analytics')
new_df = pd.read_csv('new_df.csv')

new_df['Latitude'] = new_df['Latitude'].str.replace('° N', '')
new_df['Longitude'] = new_df['Longitude'].str.replace('° E', '')
new_df['Latitude'] = new_df['Latitude'].astype('float')
new_df['Longitude'] = new_df['Longitude'].astype('float')
new_df = new_df.groupby('sector')[['price', 'Built_Up_Area', 'Latitude', 'Longitude']].mean()

st.subheader('Map of Gurgaon')

fig = px.scatter_mapbox(new_df, lat="Latitude", lon="Longitude", color="price", size="Built_Up_Area",
                        color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10,
                        mapbox_style="open-street-map", text=new_df.index, height=600)
st.plotly_chart(fig, use_container_width=True)

df = pd.read_csv('new_df.csv')
st.subheader('Area vs Price')
fig2 = px.scatter(df, x='Built_Up_Area', y='price', color='bedRoom')
st.plotly_chart(fig2, use_container_width=True)
st.subheader('BHK Wise percentage')
l = df['sector'].unique().tolist()
l.insert(0, 'Overall')
selected = st.selectbox('Select Sector', l)
if selected == 'Overall':
    fig3 = px.pie(df, names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)
else:
    fig3 = px.pie(df.query('sector == @selected'), names='bedRoom')
    st.plotly_chart(fig3, use_container_width=True)

st.subheader('BHK price comparison')
fig = px.box(df, x='bedRoom', y='price')
st.plotly_chart(fig, use_container_width=True)
