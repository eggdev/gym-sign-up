from dotenv import load_dotenv

load_dotenv()
import os

email = os.environ["EMAIL"]
avalon_url = os.environ["AVALON_URL"]
password = os.environ["PASSWORD"]
amenity_key = os.environ["AMENITY_KEY"]
reservation_terms = os.environ["RESERVATION_TERMS"]
names_input_id = os.environ["NAMES_INPUT_ID"]