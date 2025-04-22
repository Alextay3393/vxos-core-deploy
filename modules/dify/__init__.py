# modules/dify/__init__.py
# Claude Infinity 接入 Dify 智能模块（即时部署版本）

import requests
import os

DIFY_API_URL = os.getenv("DIFY_API_URL", "https://api.dify.ai/v1/chat-messages")
DIFY_API_KEY = os.getenv("DIFY_API_KEY", "sk-xxx")

def ask_dify(question, user_id="default-user"):
    headers = {
        "Authorization": f"Bearer {DIFY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": {},
        "query": question,
        "response_mode": "streaming",
        "user": user_id
    }

    try:
        response = requests.post(DIFY_API_URL, json=payload, headers=headers, timeout=15)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Dify Error: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
