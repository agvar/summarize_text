import openai
import os
from dotenv import load_dotenv

_=load_dotenv("./key.env")
openai.api_key=os.getenv("OPENAI_API_KEY")

def generate_summary_prompt(text):
    model="gpt-3.5-turbo"
    prompt=f"""
    Perform the following task:
    You are an AI teaching assistant that has expertize in summarising large texts into easy-to-understand text. \
    Summarize the text delimited by triple backticks into a single sentence of under 50 words, \
    highligting important points.Ensure the summary is grammatically correct ,concise and easy-to-understand \
    for anyone that is a beginner in the subject discussed in the input text.
    Use the following format in the response:
    Summary :<summary>
    
    Text:```{text}```
    """
    messages=[{"role": "user","content":prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]
  