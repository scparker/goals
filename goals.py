import matplotlib.pyplot as plt
import numpy as np
import pymongo
import streamlit as st

import socket.
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
st.write("Your Computer Name is:"+hostname)
st.write("Your Computer IP Address is:"+IPAddr)

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pymongo.MongoClient(**st.secrets["mongo"])

client = init_connection()

# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def get_data():
    db = client.mydb
    items = db.mycollection.find()
    items = list(items)  # make hashable for st.cache_data
    return items

items = get_data()

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
