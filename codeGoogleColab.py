# Loading audio from a computer
# Audio files up to 25 MB in size are supported, in one of the formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm

from google.colab import files
uploaded = files.upload()


# OpenAi library
# Loading the OpenAi library, importing the OpenAi module, and installing the API key

!pip install openai
import openai
API_KEY = 'YOUR_KEY'
openai.api_key = API_KEY


# Getting text from audio

model_id = 'whisper-1'

media_file_path = list(uploaded.keys())[0]
media_file = open(media_file_path, 'rb')

response_0 = openai.Audio.transcribe(
    api_key=API_KEY,
    model=model_id,
    file=media_file,
    response_format='text' # text, json, srt, vtt
)
print(response_0)


# Processing text from audio

response_1 = openai.ChatCompletion.create(
    # model="gpt-3.5-turbo",
    # model="gpt-4",
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "Summarize the meeting and formulate the main tasks that need to be done based on the following text: "},
        {"role": "user", "content": response_0}
    ],
    max_tokens=4000
)

print(response_1["choices"][0]["message"]["content"])


