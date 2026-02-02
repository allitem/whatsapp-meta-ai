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
