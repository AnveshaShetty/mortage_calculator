import streamlit as st
import pandas as pd

st.title("Mortgage Calculator")
col1, col2 = st.columns(2)

with col1:
    loan_amount = st.number_input("Enter the loan amount:", min_value=0.0, step=1000.0)
    interest = st.number_input("Enter the annual interest rate (in %):", min_value=0.0, step=0.1)

with col2:
    loan_term = st.number_input("Enter the loan term (in years):", min_value=1, step=1)
    downpayment = st.number_input("Enter the down payment amount:", min_value=0.0, step=1000.0)

if st.button("Calculate"):
    monthly_interest = (interest/100) / 12
    number_of_payments = loan_term * 12
    loan_amount_after_downpayment = loan_amount - downpayment

    mortgage = (loan_amount_after_downpayment * monthly_interest * (1 + monthly_interest) ** number_of_payments) / ((1 + monthly_interest) ** number_of_payments - 1)
    total_amount = mortgage * number_of_payments
    total_interest = total_amount - loan_amount_after_downpayment

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Mortgage Amount", f"{mortgage:.2f}")
    with col2:
        st.metric("Total Payment", f"{total_amount:.2f}")
    with col3:
        st.metric("Total Interest", f"{total_interest:.2f}")

    df = pd.DataFrame({ "Month": [f"Month {i+1}" for i in range(int(number_of_payments))],
                    "Payment": [f"{mortgage:.2f}" for _ in range(int(number_of_payments))]})

    st.dataframe(df)