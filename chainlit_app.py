import os
import sys
import chainlit as cl
from dotenv import load_dotenv
load_dotenv()
from src.langchainplamai.langchainplamai_app import invoke_response


@cl.on_chat_start
async def on_chat_start():
    print("on_chat_start")
    cl.user_session.set("app", "langchainplamai")

@cl.on_message
async def on_message(message: cl.Message):
    print("on_message", message.content)
    response_text = await invoke_response(message.content)
    await cl.Message(content=response_text).send()

