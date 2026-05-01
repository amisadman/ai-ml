import streamlit as st

st.title("My first streamlit web app", anchor= False)
st.header("Content(Header)", divider=True)
st.subheader("this is a subheader")
st.text("thhis is text")
st.markdown("**bold** *italic*")
st.markdown(":red[red] :orange[orange] :green[green]")
st.markdown(":red-background[This text has text background]")
st.markdown("world map emogi - :world_map:")
a= 10
b = 20
st.write(a,b)