import os
import requests

class DifyAIInterface:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("DIFY_API_KEY")
        self.api_url = os.getenv("DIFY_API_URL", "https://api.dify.ai/v1/chat-messages")

    def ask(self, question, user_id="default-user"):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "inputs": {},
            "query": question,
            "user": user_id
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            result = response.json()
            return result.get("answer", "[Dify 无回应]")
        except Exception as e:
            return f"[Dify 错误] {e}"
