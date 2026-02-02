# Mapping เมนูเป็นฟังก์ชัน
MENU_FUNCTIONS_OWNER = {
    "1": full_ai_response,        # วิเคราะห์ข้อความ
    "2": lambda msg: f"เรียก API ด้วยข้อความ: {msg}",  # ตัวอย่างเรียก API
    "3": lambda msg: f"สร้างรายงานสำหรับข้อความ: {msg}",
    "4": lambda msg: f"รันโมดูลอื่น ๆ ด้วยข้อความ: {msg}"
}

MENU_FUNCTIONS_BASIC = {
    "1": basic_ai_response,       # ถาม-ตอบทั่วไป
    "2": lambda msg: f"ข่าวสารล่าสุด: {msg}",
    "3": lambda msg: f"คำแนะนำเบื้องต้น: {msg}"
}

def handle_menu_selection(sender_id, message):
    """
    ตรวจสอบว่าผู้ใช้เลือกตัวเลือกในเมนูและเรียกฟังก์ชันจริง
    """
    if sender_id == OWNER_ID:
        func = MENU_FUNCTIONS_OWNER.get(message)
    else:
        func = MENU_FUNCTIONS_BASIC.get(message)

    if func:
        response = func(message)
        send_message(sender_id, response)
        return True
    return False
