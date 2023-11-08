import streamlit as st
import pandas as pd

data = pd.read_csv('H:\내 드라이브\Inventory_Order_update\inv_data\OUTRE_StockAvailability.csv', sep='\t', encoding='utf_16', on_bad_lines='warn', skiprows=[1], skipfooter=1)

st.write(data)