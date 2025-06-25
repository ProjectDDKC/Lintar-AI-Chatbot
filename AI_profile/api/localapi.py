import json
from save import save_engine as save 
import requests
import json

configapi = {
    "api_url":"http://localhost:5001/v1/chat/completions", 
    "api_key":"4501650",
    "model":"Lintar",
    "temperature": 0.8,
    "max_tokens": 500
}

def localapi():
    configapi["api_url"] = save.loader["api_url"]
    with open("AI_profile/configapi.json", "w") as file:
        json.dump(configapi, file, indent=4)

CONFIG_API = "AI_profile/configapi.json"
PROMPT = "AI_profile/Prompt.json"
CHAT_MEMORY_PATH = "AI_profile/chat_memory.json"
MAX_MEMORY = 5  # บทสนทนาเก่าสุดที่จะโหลดกลับมา

# ✅ โหลด memory
def load_recent_memory(path=CHAT_MEMORY_PATH, limit=MAX_MEMORY):
    try:
        with open(path, "r", encoding="utf-8") as f:
            history = json.load(f)
            return history[-limit:]
    except FileNotFoundError:
        return []

def save_message(role, content, path=CHAT_MEMORY_PATH):
    try:
        with open(path, "r", encoding="utf-8") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append({"role": role, "content": content})
    with open(path, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

# ✅ ฟังก์ชันหลัก
def chat_with_local(text):
    with open(CONFIG_API, "r", encoding="utf-8") as f:
        config = json.load(f)

    with open(PROMPT, "r", encoding="utf-8") as f:
        prompt = json.load(f)

    print(text)

    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }

    # 🧠 ดึง memory และระบบ prompt
    messages = prompt["system_prompts"][:] #ดึง prompt ที่ตั้งค่า system ไว้
    messages += load_recent_memory() #โหลดข้อความล่าสุด
    messages.append({"role": "user", "content": text}) #เพิ่มข้อความผู้ใช้ที่พิมล่าสุดมา 

    payload = {
        "model": config["model"],
        "messages": messages,
        "temperature": config["temperature"],
        "max_tokens": config["max_tokens"]
    }

    try:
        response = requests.post(config["api_url"], headers=headers, json=payload)
        print(payload)
        response_data = response.json()
        ai_response = response_data["choices"][0]["message"]["content"].strip()

        save_message("user", text)
        save_message("assistant", ai_response)

        return ai_response
    except Exception as e:
        return f"⚠️ ข้อผิดพลาด: ไม่สามารถเชื่อมต่อ LLM API (HTTP Error) โปรดตรวจสอบการเชื่อมต่อ Link API HTTP"