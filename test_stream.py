import requests; r = requests.post("http://127.0.0.1:8080/chat/stream", json={"message": "Hello", "thread_id": "123", "model": "gemini-3.1-flash-lite"}, stream=True); print(r.text)
