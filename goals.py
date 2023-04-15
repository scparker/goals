import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.title("Goals!!!!!")

st.write("Set Goals")

st.write("Record Goals")

lifts = np.array([200, 170, 210, 160, 150])

if st.checkbox('Are you feeling swole today?'):
    lifts = lifts * 2

fig, ax = plt.subplots()
ax.plot(lifts)
ax.set_title("Lift History")
ax.set_xlabel("Day")
ax.set_ylabel("Pounds")

st.pyplot(fig)
