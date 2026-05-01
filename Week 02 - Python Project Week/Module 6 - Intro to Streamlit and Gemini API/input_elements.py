import streamlit as st

st.title("Input your info", anchor=False)
st.divider()
name = st.text_input("Enter an input: ")
st.divider()
st.write("Your name is: ", name)
age = st.number_input("Enter your age: ", value=None, placeholder="eg. 23")
st.write("Your age is: ",age)
st.divider()

password = st.text_input("Enter You password", type="password")

selectd = st.selectbox("Choose Your Profession", 
             ("Student", "Employee","Bussinessman"),index=None,accept_new_options=True)

print(type(selectd))
st.write("You selected: ",selectd)

pressed = st.button("Enter to confirm",type="primary")

if pressed:
    st.write(f"Your name is: {name}, age: {age}")