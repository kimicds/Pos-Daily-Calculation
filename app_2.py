import streamlit as st
import pandas as pd

# Streamlit App Title
st.title("POS Business Daily Calculator")

# Input Fields
st.header("Enter Daily Transaction Details")

# Input Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Before Values")
   # initial = st.number_input("Initial Cash", value=0.0, step=0.01)
   # total_payout = st.number_input("Total Payout", value=0.0, step=0.01)
    opay_before = st.number_input("Opay Before", value=0.0, step=0.01)
    opay_business_before = st.number_input("Opay Business Before", value=0.0, step=0.01)
    mp2_before = st.number_input("MP_2 Before", value=0.0, step=0.01)
    mp1_before = st.number_input("MP_1 Before", value=0.0, step=0.01)
    polaris_before = st.number_input("Polaris Before", value=0.0, step=0.01)
    dashboard_before = st.number_input("Dashboard Before", value=0.0, step=0.01)

with col2:
    st.subheader("After Values")
    opay_after = st.number_input("Opay After", value=0.0, step=0.01)
    opay_business_after = st.number_input("Opay Business After", value=0.0, step=0.01)
    mp2_after = st.number_input("MP_2 After", value=0.0, step=0.01)
    mp1_after = st.number_input("MP_1 After", value=0.0, step=0.01)
    polaris_after = st.number_input("Polaris After", value=0.0, step=0.01)
    dashboard_after = st.number_input("Dashboard After", value=0.0, step=0.01)

# Additional Input Fields
initial = st.number_input("Initial Cash", value=0.0, step=0.01)
total_payout = st.number_input("Total Payout", value=0.0, step=0.01)
expenses = st.number_input("Expenses", value=0.0, step=0.01)
data_card = st.number_input("Data Card", value=0.0, step=0.01)
charges_in_cash = st.number_input("Charges in Cash", value=0.0, step=0.01)
cash_deposited = st.number_input("Cash Deposited", value=0.0, step=0.01)

# Perform Calculations
remaining_cash = initial - total_payout
terminal_before = opay_before + opay_business_before + mp2_before + mp1_before + polaris_before
terminal_after = opay_after + opay_business_after + mp2_after + mp1_after + polaris_after
dashboard_used = dashboard_before - dashboard_after
data_benefit = data_card - dashboard_used
net_cash_terminal = terminal_after - terminal_before
overall_cash = net_cash_terminal + data_benefit + cash_deposited + charges_in_cash
gain = overall_cash - total_payout - expenses

# Display Results
st.subheader("Calculated Results")
st.write("Remaining Cash:", remaining_cash)
st.write("Terminal Before:", terminal_before)
st.write("Terminal After:", terminal_after)
st.write("Data Used:", dashboard_used)
st.write("Data Benefit:", data_benefit)
st.write("Net Cash In Terminal:", net_cash_terminal)
st.write("Overall Cash:", overall_cash)
st.write("Gain:", gain)
