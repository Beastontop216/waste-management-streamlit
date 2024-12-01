import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Waste_Management_Dataset_200_Rows.csv")

# Streamlit code goes here
st.title("Waste Management and Recycling Dashboard")
