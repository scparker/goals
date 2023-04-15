import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Goals!!!!!")

st.write("Set Goals")

st.write("Record Goals")

st.checkbox('Are you feeling swole today?')

lifts = [200, 170, 210, 160, 150]

fig, ax = plt.subplots()
ax.plot(lifts)

st.pyplot(fig)
