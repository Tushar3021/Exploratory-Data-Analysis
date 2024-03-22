import streamlit as st

from runeda import RunEDA
from main import eda

st.set_page_config("Exploraory Data Analysis")

app = RunEDA()

app.add_app("EDA", eda.app)
app.run()
