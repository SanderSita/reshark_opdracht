from linkedin_api import Linkedin
from dotenv import load_dotenv
import os

load_dotenv()

# Authenticate using any Linkedin account credentials
api = Linkedin(os.getenv("EMAIL"), os.getenv("PASSWORD"))

def get_profile(profile_id: str):
    return api.get_profile(profile_id)

def get_profile_contact_info(profile_id: str):
    return api.get_profile_contact_info(profile_id)

def get_profile_connections(profile_id: str):
    return api.get_profile_connections(profile_id)