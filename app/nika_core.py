from auth import get_role
from workflow import execute

def nika(message: str, user_id: str):
    role = get_role(user_id)

    if role != "owner":
        return "นิกะพร้อมตอบคำถามพื้นฐานให้คุณ"

    if message.startswith("create"):
        return execute(message)

    if message.startswith("connect api"):
        return execute(message)

    return "นิกะพร้อมสร้างและเชื่อมต่อระบบให้เจ้านาย"
