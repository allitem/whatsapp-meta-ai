import os
import subprocess

BASE = "runtime"

def execute(cmd: str):
    if "web" in cmd:
        os.makedirs(f"{BASE}/web", exist_ok=True)
        return "สร้างระบบเว็บเรียบร้อย"

    if "game" in cmd:
        os.makedirs(f"{BASE}/game", exist_ok=True)
        return "สร้างระบบเกมเรียบร้อย"

    if "database" in cmd:
        os.makedirs(f"{BASE}/database", exist_ok=True)
        return "สร้างระบบฐานข้อมูลเรียบร้อย"

    return "ดำเนินการ workflow สำเร็จ"
