from fastapi import FastAPI, Form
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    try:
        chat = ChatOllama(model="llama2")
        messages = [
            SystemMessage(content="You are a helpful assistant that summarizes text."),
            HumanMessage(content=f"Summarize this:\n\n{text}")
        ]
        response = chat.invoke(messages)
        return {"summary": response.content}
    except Exception as e:
        return {"summary": f"Error: {str(e)}"} 