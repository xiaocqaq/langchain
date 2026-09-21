"""
@Author:shkstart
@Desc: 第1个测试程序
"""
import langchain



print(langchain.__version__)

from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

# 加载配置文件
load_dotenv(override=True)

# 获取大模型
model = init_chat_model(
    model="openai:step-3.7-flash",
    # model_provider="openai",
    api_key=os.getenv("STEP_API_KEY"),
    base_url= os.getenv("STEP_BASE_URL"),
)


#  openai

model = init_chat_model(
    model="openai:gpt-5.4-mini",
    temperature=0,
    api_key=os.getenv("CLOSEAI_API_KEY"),
    base_url=os.getenv("CLOSEAI_BASE_URL"),
)