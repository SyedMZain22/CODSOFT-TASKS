#TASK 3:
#syed muhammad zain bin faisal
"""
A password generator is a useful tool that generates strong and
random passwords for users. This project aims to create a
password generator application using Python, allowing users to
specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the password.
Generate Password: Use a combination of random characters to
generate a password of the specified length.
Display the Password: Print the generated password on the screen.
"""
import random
import string
import streamlit as st
from streamlit_lottie import st_lottie
import requests
st.set_page_config(page_title="ZPG", page_icon=":cyclone:", layout="wide")
page_by_img ="""
<style>
[class="main css-uf99v8 ea3mdgi5"]{
background-image: url("https://images.unsplash.com/photo-1690178696521-f6fc338f1f64?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1374&q=80");
background-size: cover;
}
</style>
"""
st.markdown(page_by_img, unsafe_allow_html=True)
with st.container():
    st.subheader("Hey there, I'm Zain :wave:")
def loadd_url1(url):
    r_= requests.get(url)
    if r_.status_code != 200:
        return None
    return r_.json()
code_lot=loadd_url1("https://lottie.host/95526696-6844-46cb-ad54-3f04355f456c/TunuS27a7o.json")

with st.container():
    st.write("--------")
    left_column, right_column = st.columns(2)
    with left_column:
         def gen_pass(length, lowercase, uppercase, numbers, symbols):
            char = ""
            if lowercase:
              char += string.ascii_lowercase
            if uppercase:
              char += string.ascii_uppercase
            if numbers:
              char += string.digits
            if symbols:
              char += string.punctuation
            if not char:
              st.error("Please select at least one character type.")
              return ""
            pass_ = ''.join(random.choice(char) for _ in range(length))
            return pass_


         def main():
            st.title("Password Generator!")
            length = st.number_input("Enter the passwords's desired length:", min_value=1, step=2)
            lowercase = st.toggle("Add lowercase letters")
            uppercase = st.toggle("Add uppercase letters")
            numbers = st.toggle("Add numbers")
            symbols = st.toggle("Add symbols")

            if st.button("Generate Password"):
               pass_ = gen_pass(int(length), lowercase, uppercase, numbers, symbols)
               st.success("Generated Password: " + pass_)
         if __name__ == "__main__":
            main()

    with right_column:
        st_lottie(code_lot, height=350, key="coding1")



