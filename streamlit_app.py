import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title("My Mom's new Healthy Dinner")
" BreakFast Favourites"
" BreakFast Favourites"
" BreakFast Favourites"" BreakFast Favourites"" BreakFast Favourites"" BreakFast Favourites"" BreakFast Favourites"

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
filter_data = data.loc[filter_fruit]
# Display the table on the page.
streamlit.dataframe(filter_data)


streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("The Fruit Load List Contains")
streamlit.dataframe(my_data_row)

streamlit.text("What food you like to have ?")
add_my_fruit = streamlit.text_input("What fruit would you like to have?")

