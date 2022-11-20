import streamlit
import pandas as pd

streamlit.title("My Mom's new Healthy Dinner")


streamlit.header(" BreakFast Favourites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket Smmothie")
streamlit.text("🐔 Hard Boiled Free-Ranged eggs")
streamlit.text("🥑🍞 Avacado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

data = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
data = data.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
filter_fruit = streamlit.multiselect("Pick some fruits:", list(data.index), ["Avocado","Strawberries"])
filter_data = filter_data.loc[filter_fruit]
# Display the table on the page.
streamlit.dataframe(filter_data)





