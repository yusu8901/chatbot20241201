import os
from openai import OpenAI



# OpenAIクライアントを初期化
client = OpenAI(
    api_key=API_KEY,  # APIキーを設定
)

def get_response(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="gpt-4o",  # 利用するモデルを指定
    )
    return chat_completion.choices[0].message

while True:
    user_message = input("あなた: ")
    response = get_response(user_message)
    print("チャットボット: ", response.content)