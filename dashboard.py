import streamlit as st
import os
import config

st.title("TempSched+ Dashboard")

st.write("Device Storage:")
st.write(os.listdir(config.DEVICE))

st.write("Edge Storage:")
st.write(os.listdir(config.EDGE))

st.write("Cloud Storage:")
st.write(os.listdir(config.CLOUD))

st.write("Compressed:")
st.write(os.listdir(config.COMPRESSED))

st.write("Encrypted:")
st.write(os.listdir(config.ENCRYPTED))
