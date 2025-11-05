import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = genai.list_models()
    print("✅ Available Models:")
    for m in models:
        print(m.name)
except Exception as e:
    print("❌ Error listing models:", e)
