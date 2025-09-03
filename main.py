from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv("KEY")
model = os.getenv("MODEL")

client = OpenAI(api_key=key, base_url="https://api.siliconflow.cn/v1")

good_name=input("请输入商品名称：")

response=client.chat.completions.create(
    model=model,
    messages=[
        {"role":"system","content":"你是一个经验丰富的小红书运营，擅长撰写小红书笔记，根据用户给你的商品名称，撰写一篇关于分享并卖货的小红书笔记，笔记内容要符合小红书平台规则，要吸引用户,要求内容稍微精简200字左右"},
        {"role":"user","content":f"商品名称：{good_name}"}
    ]
)

print(response.choices[0].message.content)