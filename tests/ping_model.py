import os
from dotenv import load_dotenv
from langchain_together.chat_models import ChatTogether

# Assumes the .env file is in the 'backend' directory, sibling to 'tests'
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'backend', '.env'))

try:
    llm = ChatTogether(model=os.getenv("TOGETHER_MODEL", "meta-llama/Llama-3-70b-chat-hf"))
    llm.invoke("Hello")
    print("✅")
except Exception as e:
    print(f"❌ Failed to ping model: {e}") 