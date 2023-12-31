import streamlit

streamlit.title('Streamlit Diner Menu Test')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado On Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
v_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# set the index as the fruit name
v_fruit_list = v_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include (preselects Avocado and Strawberries)
# streamlit.multiselect("Pick some fruits:", list(v_fruit_list.index),['Avocado','Strawberries']) 
# the above works as is, but we can assign to a variable to load the selected values into it:
v_fruits_selected = streamlit.multiselect("Pick some fruits:", list(v_fruit_list.index),['Avocado','Strawberries'])
# loc: used to access a group of rows and columns by label(s) or a boolean array.
v_fruits_to_show = v_fruit_list.loc[v_fruits_selected]

# Display the table on the page
# streamlit.dataframe(v_fruit_list)

# Display the selected fruits only
streamlit.dataframe(v_fruits_to_show)

# new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
# display an input box, with Kiwi defaulted in
fruit_choice = streamlit.text_input('What fruite would you like information about?','Kiwi')
streamlit.write('The user entered',fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json()) # just writes the data to the screen

# take the json version of the response and normalise it using a pandas funciton
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the normalised text on the page
# streamlit.text(fruityvice_normalized)
# display the normalised text on the page in a dataframe
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(user="gandreou",
                                     password="Availability00",
                                     account="https://tvlwfar-ax70117.snowflakecomputing.com"
                                    )
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
