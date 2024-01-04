import streamlit
import streamlit as st

# This is to show different type of headings
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Streamlit uses pandas 
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
filter = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruit_to_show=my_fruit_list.loc[filter]
print(fruit_to_show)

# pandas show table streamlit.dataframe
streamlit.dataframe(fruit_to_show)



st.dataframe(my_fruit_list)
st.table(my_fruit_list.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric('My metric', 42, 2)

