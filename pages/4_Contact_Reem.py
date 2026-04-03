import streamlit as st
import gspread
from styles import inject_custom_css
st.markdown(inject_custom_css(), unsafe_allow_html=True)


from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

st.title("Contact Reem")

st.write("If you're interested in working together or want to learn more, feel free to reach out.")

def get_google_sheet():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        st.secrets["gcp_service_account"],
        scope
    )

    client = gspread.authorize(creds)
    sheet = client.open(st.secrets["GOOGLE_SHEET_NAME"]).sheet1
    return sheet

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    company = st.text_input("Company (optional)")
    message = st.text_area("Message")

    submitted = st.form_submit_button("Send Message")

if submitted:
    if name and email and message:
        try:
            sheet = get_google_sheet()
            sheet.append_row([
                name,
                email,
                company,
                message,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ])
            st.success("Thanks! Your message has been received.")
        except Exception as e:
            st.error(f"Something went wrong while saving your message: {e}")
    else:
        st.error("Please fill in your name, email, and message.")