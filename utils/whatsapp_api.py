import requests

def send_message(api_url, token, to, message):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "text": {"body": message}
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    r = requests.post(api_url, json=payload, headers=headers)
    return r.json()

def fetch_messages(api_url, token):
    # ตัวอย่างการดึงข้อความล่าสุด (ต้องปรับตาม API จริง)
    # สำหรับเฉพาะกิจ สมมติข้อความใหม่เป็น list
    return [{"from": "1234567890", "body": "สวัสดี"}]
