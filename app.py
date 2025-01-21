import streamlit as st
import pandas as pd

# Streamlit App
st.title("POS Daily Record and Calculations")
st.write("This app automates your daily POS calculations based on your input.")

# Input Fields
st.subheader("Enter Your Daily Data:")
initial_cash = st.number_input("Initial Cash:", value=0)
total_payout = st.number_input("Total Payout:", value=0)
terminal_cash_before = st.number_input("Terminal Cash (Before):", value=0)
terminal_cash_after = st.number_input("Terminal Cash (After):", value=0)
card_data = st.number_input("Card Data:", value=0)
cash_deposit = st.number_input("Cash Deposit:", value=0)
charges_in_cash = st.number_input("Charges in Cash:", value=0)

# Perform Calculations
remaining_cash = initial_cash - total_payout
net_cash = terminal_cash_after - terminal_cash_before
overall_cash = card_data + cash_deposit + charges_in_cash + net_cash
result = overall_cash - total_payout

# Create a DataFrame for Calculated Results Only
calculated_data = pd.DataFrame({
    'Remaining_Cash': [remaining_cash],
    'Net_Cash': [net_cash],
    'Overall_Cash': [overall_cash],
    'Result': [result]
})

# Display the Calculated Data
st.subheader("Calculated Results (Excluding Entered Data):")
st.dataframe(calculated_data)


