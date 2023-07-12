import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21288218")

API_HASH = os.environ.get("API_HASH", "dd47d5c4fbc31534aa764ef9918b3acd")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5466682882:AAH4gU_zh-l1OJf6440HhmSLnDIaR6hGYSY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "jsjdhdbdjj") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/09d99d73b469b3ed2acb2.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5326801541').split()]

