import json
from save import save
import google.generativeai as genai

configapi = {
    "gimini_key":"", 
    "gimini_model":"",
    "temperature": 0.8,
    "max_tokens": 150
}

def giminiapi():
    configapi["gimini_key"] = save.loader["gimini_key"]
    configapi["gimini_model"] = save.loader["gimini_model"]
    with open("ai_setup/configapi.json", "w") as file:
        json.dump(configapi, file, indent=4)

CONFIG_API = "ai_setup/configapi.json"
PROMPT = "ai_setup/Prompt.json"
CHAT_MEMORY_PATH = "ai_setup/chat_memory.json"
MAX_MEMORY = 5  # บทสนทนาเก่าสุดที่จะโหลดกลับมา

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

def chat_with_gimini(message):
    with open(CONFIG_API, "r", encoding="utf-8") as f:
        config = json.load(f)

    with open(PROMPT, "r", encoding="utf-8") as f:
        prompt = json.load(f)

    genai.configure(api_key=config["gimini_key"])

    model = genai.GenerativeModel(config["gimini_model"])

    # 👇 โหลด memory เดิม + system prompt (ต่อเป็นข้อความยาว)
    messages = prompt["system_prompts"][:]  # system prompt
    messages += load_recent_memory()
    messages.append({"role": "user", "content": message})

    # 👇 รวมข้อความทั้งหมดเป็น string เดียว
    conversation_text = "\n".join(m["content"] for m in messages)

    try:
        response = model.generate_content(
            conversation_text,
            generation_config={
                "temperature": config["temperature"],
                "max_output_tokens": config["max_tokens"]
            }
        )

        ai_response = response.text.strip()

        # ✅ บันทึก memory
        save_message("user", message)
        save_message("assistant", ai_response)

        return ai_response
    except Exception as e:
        return f"⚠️ เกิดข้อผิดพลาด: {e}"