from openai import OpenAI
client = OpenAI()

file = open("sample.wav", "rb")
transcript = client.audio.translations.create(
    model="whisper-1",
    file=file,
)

# 만약 영어로만 나오는 것을 원한다면?

# print(transcript.text)

# 영어를 한글로로 번역하면서 필사본을 요약을 원한다면?

# summary = client.chat.completions.create(
#     model = "gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "user",
#             "content": f"다음 문장을 한국어로 번역하고 3줄의 글머리 기호로 요악하세요.\n{transcript}"
#         }
#     ]
# )

# print(f"요약 결과: \n {summary.choices[0].message.content}")
# print(f"요약 사용한 토큰 수: \n {summary.usage.total_tokens}")