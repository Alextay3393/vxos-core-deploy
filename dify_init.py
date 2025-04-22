# modules/dify/_init_.py
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
        "response_mode": "blocking",
        "user": user_id
    }
    try:
        response = requests.post(DIFY_API_URL, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            return response.json().get("answer", "Dify 没有回答。")
        else:
            return f"请求失败，状态码：{response.status_code}"
    except Exception as e:
        return f"请求异常：{str(e)}"
