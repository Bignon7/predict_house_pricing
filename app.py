import streamlit as st

st.set_page_config(page_title="To-do list", page_icon=":house:")

st.markdown(":blue[Texte en bleu] et :red[texte en rouge]")
st.markdown(":green-background[Texte avec fond vert]")

st.title(
        ":orange[:material/home:] My HOME PAGE",
        width="content",
        anchor=False,
    )

st.title("Hello, this is my first page")

st.toggle("Toggle me")

st.checkbox("Check me")

st.toast("This is a toast message")

locations = (
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
)

st.selectbox("Select a location", options=locations)

st.text_input("Enter your name")
st.text_area("Enter your address")