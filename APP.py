import streamlit as st
import pandas as pd

# Initialize the session state
if 'expenses' not in st.session_state:
    st.session_state['expenses'] = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])

# App title
st.title('Expense Tracker')

# Input form for new expenses
st.header('Add a New Expense')
with st.form(key='expense_form'):
    date = st.date_input('Date')
    description = st.text_input('Description')
    category = st.selectbox('Category', ['Food', 'Transport', 'Utilities', 'Entertainment', 'Others'])
    amount = st.number_input('Amount', min_value=0.0, format="%.2f")
    submit_button = st.form_submit_button(label='Add Expense')

    if submit_button:
        new_expense = pd.DataFrame({
            'Date': [date],
            'Description': [description],
            'Category': [category],
            'Amount': [amount]
        })
        st.session_state['expenses'] = pd.concat([st.session_state['expenses'], new_expense], ignore_index=True)
        st.success('Expense added!')

# Display all expenses
st.header('Expense History')
st.dataframe(st.session_state['expenses'])

# Display total expenses
st.header('Total Expenses')
st.write(f"Total: ${st.session_state['expenses']['Amount'].sum():,.2f}")
