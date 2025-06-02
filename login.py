import streamlit as st
import subprocess
import base64

st.set_page_config(initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

# Function to validate login
def validate_login(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False

# Function to load image with caching
@st.cache_data
def load_image(file):
    with open(file, "rb") as f:
        data = f.read()
    return data

# Load image
local_image_path = "african-american-doctor-isolated-white-background-professional-occupation.jpg"
image_data = load_image(local_image_path)
encoded_image = base64.b64encode(image_data).decode()

# Display background image
page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url('data:image/png;base64,{encoded_image}');
        background-size: cover;
    }}
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

close_tab_js = """
<script>
function closeTab() {
    window.open("", "_self");
    window.close();
}
</script>
"""

# Main function for the login page
def main():

    # Creating a container to hold the login form
    login_container = st.container()
    login_container.title("Login")

    # Adding username and password input fields
    username = login_container.text_input("Username", placeholder="Please Input Your username")
    password = login_container.text_input("Password", type="password", placeholder="Please Input Your password")

    # If username and password are empty, show a message
    if not username or not password:
        st.warning("Please enter your credentials to login")
        return

    # Login button
    if login_container.button("Login"):
        with st.spinner("Logging in..."):
            if validate_login(username, password):
                # Set login status to True
                st.session_state.logged_in = True
                st.success("Login successful. Redirecting to the home page...")
                # Redirect to the home page
                subprocess.Popen(["streamlit", "run", "Home.py"])
                st.markdown(close_tab_js, unsafe_allow_html=True)
                st.markdown("<script>closeTab()</script>", unsafe_allow_html=True)
            else:
                st.error("Invalid username or password. Please try again.")

if __name__ == "__main__":
    main()
