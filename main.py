import streamlit  as st
import lang_helper
st.title("Restaurant name Generator")


cusine = st.sidebar.selectbox("Pick a cuisine", ["Indian", "Chinese", "Italian", "Mexican", "American"])




if cusine:
   response = lang_helper.generate_restaurant_name_and_items(cusine)
   st.header(response['restaurant_name'].strip())
   st.subheader("Menu Items")
   menu_items = response['menu_items'].strip().split(',')
   for item in menu_items:
      st.write('-', item)