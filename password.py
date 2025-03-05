import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="Password Strength Checker By Syed NoorAlam",
    page_icon="🔑",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
        .main { text-align: center; }
        .stTextInput { width: 60% !important; margin: auto; }
        .stButton button {
            width: 50%;
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
        }
        .stButton button:hover { background-color: #45a049; }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("Password Strength Checker")
st.write("Enter a password to check its strength.")

# Function to check password strength
# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check length requirement
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    # Check for at least one number
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    # Check for at least one special character
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong Password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate Password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak Password** - Follow the suggestions below to strengthen it.")

    # Show feedback for improvement
    if feedback:
        with st.expander("🔵 **Improve Your Password**"):
            for item in feedback:
                st.write(item)
    
    return score, feedback

# User input for password
password = st.text_input(
    "Enter your password:", 
    type="password", 
    help="Ensure your password is strong 🔒"
)

# Button to check password strength
if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)  # Get score and feedback
    else:
        st.warning("⚠️ Please enter a password first!")

 


   

