import os
import checks
from dotenv import load_dotenv
load_dotenv('./.env')

elevenlabs_key = os.getenv('elevenlabs_key')