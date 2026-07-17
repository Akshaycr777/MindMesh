from agent import get_agent
from langchain_core.messages import HumanMessage, SystemMessage
from database import init_db

init_db()

agent = get_agent("gemini-3.1-flash-lite")

config = {
    "configurable": {
        "thread_id": "test_thread_id",
    }
}

for message_chunk, metadata in agent.stream(
    {
        'messages': [HumanMessage(content="What is my name ?")]},
        config = config,
        stream_mode = 'messages'):

        if message_chunk.content:
            if isinstance(message_chunk.content, str):
                print(message_chunk.content, end="", flush=True)
            elif isinstance(message_chunk.content, list):
                for item in message_chunk.content:
                    if isinstance(item, dict) and "text" in item:
                        print(item["text"], end="", flush=True)
                    elif isinstance(item, str):
                        print(item, end="", flush=True)

print()


    

