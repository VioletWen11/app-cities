import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('world cities by Violet')
df = pd.read_csv('worldcities.csv')
st.map(df)

st.write(df)

#total pop
fig, ax = plt.subplots()
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax = ax)
st.pyplot(fig)

# add a slider
pop_filter = st.sidebar.slider('select minimal population', 0.0, 40.0, 4.0)
#show the slider
st.map(df)

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# add a capital multi select
capital_filter = st.sidebar.multiselect('capital select',  df.capital.unique(), ['primary'])

# filter by population
df = df[df.population >= pop_filter]

# fiter by capital
df = df[df.population.isin(capital_filter)]

# filter by country
if country_filter!='ALL':
    df = df[df.country == country_filter]

# show
st.map(df)
 



