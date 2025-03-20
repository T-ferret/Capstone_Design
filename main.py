from fastapi import FastAPI
from pydantic import BaseModel
# from openai import OpenAI
# from pyexpat.errors import messages

# client = OpenAI(INSERT_YOUR_KEY)
app = FastAPI()

class ChatDto(BaseModel):
    role: str
    content: str

# OpenAI의 일반적인 Example response
# [
#     {
#         "index": 0,
#         "message": {
#             "role": "assistant",
#             "content": "Under the soft glow of the moon, Luna the unicorn danced through fields of twinkling stardust, leaving trails of dreams for every child asleep.",
#             "refusal": null
#         },
#         "logprobs": null,
#         "finish_reason": "stop"
#     }
# ]
# 이 중에서, chat에 필요한 데이터는 index, content

fake_items = [
    {
        "index": 0,
        "content": "first"
    },
    {
        "index": 1,
        "content": "second"
    },
    {
        "index": 2,
        "content": "third"
    }
]

@app.post("/chats")
async def generate_chats(dto: ChatDto):

    completion = fake_items.index({"index": 0})

    # completion = client.chat.completions.create(
    #     model="gpt-4o-mini-2024-07-18",
    #     messages=[
    #         {
    #             "role": "developer",
    #             "content": "test"
    #         },
    #         dto
    #     ]
    # )

    print(dto)

    return completion

# @app.post()
# @app.get()
# @app.delete()
# @app.put()