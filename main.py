import json
from utils.whatsapp_api import send_message, fetch_messages

# โหลด config
with open("config.json") as f:
    config = json.load(f)

# รับข้อความใหม่
messages = fetch_messages(config["whatsapp_api_url"], config["access_token"])

for msg in messages:
    # ส่งข้อความตอบกลับ
    send_message(
        api_url=config["whatsapp_api_url"],
        token=config["access_token"],
        to=msg["from"],
        message=config["default_reply"]
    )

print("ระบบ WhatsApp Meta AI ทำงานเสร็จเรียบร้อย")

from modules.nika_whatsapp import handle_message, full_ai_response, basic_ai_response, send_message, greeted_users
from utils.whatsapp_api import fetch_messages

messages = fetch_messages("https://wa.me/ais/876126961720902?s=5", ACCESS_TOKEN)

for msg in messages:
    response = handle_message(
        sender_id=msg["from"],
        message=msg["body"],
        ai_full_function=full_ai_response,
        ai_basic_function=basic_ai_response
    )
    if response:
        send_message(msg["from"], response)
