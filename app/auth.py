OWNERS = {"Thanva"}  # เปลี่ยนเป็น WhatsApp ID จริง

def get_role(user_id: str):
    return "owner" if user_id in OWNERS else "public"
