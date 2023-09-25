import streamlit as st

import native

st.title("Hello World")
st.write(native.sum_as_string(1, 2))
