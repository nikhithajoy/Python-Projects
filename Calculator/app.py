import streamlit as st

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        # Replace HTML entities with their corresponding operators for evaluation
        expression = expression.replace('&divide;', '/').replace('&times;', '*').replace('&minus;', '-').replace('&plus;', '+')
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    return result

# Streamlit app
st.title("Simple Calculator")

# Session state to store the current expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Display the current expression/output
st.text_input("Display", st.session_state.expression, key="display", disabled=True, help="Display")

# Buttons layout with HTML entities for symbols
buttons = [
    ['7', '8', '9', '&divide;'],   # Use &divide; for division symbol
    ['4', '5', '6', '&times;'],    # Use &times; for multiplication symbol
    ['1', '2', '3', '&minus;'],    # Use &minus; for subtraction symbol
    ['0', '.', '=', '&plus;'],     # Use &plus; for addition symbol
]

# Function to handle button clicks
def button_click(btn):
    if btn == "=":
        # Evaluate the expression
        st.session_state.expression = evaluate_expression(st.session_state.expression)
    elif btn == "C":
        # Clear the expression
        st.session_state.expression = ""
    elif btn == "←":
        # Backspace functionality
        st.session_state.expression = st.session_state.expression[:-1]
    else:
        # Replace HTML entities with their symbols before adding to the expression
        btn = btn.replace('&divide;', '/').replace('&times;', '*').replace('&minus;', '-').replace('&plus;', '+')
        st.session_state.expression += btn

# Set the button style
button_style = """
    <style>
    .css-1emrehy.edgvbvh3 {
        font-size: 20px;
        height: 80px;
        width: 80px;
    }
    </style>
"""

# Inject custom CSS into the Streamlit app
st.markdown(button_style, unsafe_allow_html=True)

# Display the buttons
for row in buttons:
    cols = st.columns(4, gap="small")
    for i, btn in enumerate(row):
        with cols[i]:
            st.button(btn, on_click=button_click, args=(btn,), use_container_width=True)

# Clear and backspace buttons
col1, col2 = st.columns(2, gap="small")
with col1:
    st.button("C", on_click=button_click, args=("C",), use_container_width=True)
with col2:
    st.button("←", on_click=button_click, args=("←",), use_container_width=True)
