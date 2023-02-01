import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admins_id_str = os.getenv("ADMINS_ID")

# Convert the string to a list of integers
admins_id = [int(id) for id in admins_id_str.strip("[]").split(",")]
print(admins_id)