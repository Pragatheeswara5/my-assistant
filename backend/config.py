import os
from dotenv import load_dotenv
import urllib.parse
load_dotenv()

class Config:
    username = urllib.parse.quote_plus("ptwkarl")
    password = urllib.parse.quote_plus("mniPraga@5")

    MONGO_URI = os.getenv("MONGO_URI", f"mongodb+srv://{username}:{password}@cluster0.uejdgqx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")