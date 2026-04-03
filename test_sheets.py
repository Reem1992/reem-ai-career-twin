import gspread
from oauth2client.service_account import ServiceAccountCredentials
import streamlit as st

# Define scope
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from secrets
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"], scope
)

client = gspread.authorize(creds)

# Open sheet
sheet = client.open(st.secrets["GOOGLE_SHEET_NAME"]).sheet1

# Test write
sheet.append_row(["Test User", "test@email.com", "Test Company", "Hello", "NOW"])

print("✅ SUCCESS — data written")