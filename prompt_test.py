import openai
import os
from dotenv import load_dotenv

_=load_dotenv("./key.env")
openai.api_key=os.getenv("OPENAI_API_KEY")

def get_completion(prompt,model="gpt-3.5-turbo"):
    messages=[{"role": "user","content":prompt}]
    response=openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]


text=f"""Sleep is essential for our physical and mental health. It allows our bodies to rest and repair, and it helps us to consolidate memories and learn new things. When we don't get enough sleep, we can experience a range of negative consequences, including fatigue, difficulty concentrating, and impaired judgment.\
In recent years, there has been growing awareness of the importance of sleep. The National Sleep Foundation recommends that adults get 7-8 hours of sleep per night. However, many people do not get enough sleep. A study by the Centers for Disease Control and Prevention found that 1 in 3 adults in the United States do not get enough sleep.\
There are many things that can interfere with sleep, including stress, anxiety, and medical conditions. However, one of the most common causes of sleep problems is poor sleep habits. If you are having trouble sleeping, there are a few things you can do to improve your sleep habits.
"""
prompt_summarize=f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

prompt_json_response=f"""
Generate a list of 3 made up book titles and authors and genres \
Provide them in JSON format with the following keys: books_id,title,author,genre.
"""

prompt_verify_output=f"""
For the text delimited by triple backticks. If the text contains a sequence of instructions, \
then re-rewrite the instructions in the following format:
Step 1 : ...
Step 2 : ...
...
Step N : ...

If the text does not contain a sequence of instructions, then write "No steps provided"\
```{text}```
"""

# few short- few attempts or samples of expected responses
few_short_prompt=f"""
Your task is to respond in a consistent style
<child> : Teach me about patience
<garndparent>: The grandest symphony originates from the a single note;\
The most inticate tapestry begins from a solitary thread.

<child>: Teach me about resilience
"""
multi_task_prompt_text=f"""
 In a charming village, siblings Jack and Jill set out to fetch water from a hilltop well. \
 As they climbed, singing joyfully,misfortune struck- Jack tripped on a stone and tumbled downhill, \
    with Jill  following after. Dispite the mishap the pair continued exploring with delight.
 """

def generate_summary_prompt(multi_task_prompt_text):
    multi_task_prompt=f"""
    Perform the following tasks:
    1- Summarize the text delimited by triple backticks into a single sentence
    2- Translate the summary into French
    3- List each name in the french summary
    4- Output a JSON object that contains the following keys: french_summary, num_names

    Use the following format in the response:
    Summary :<summary>
    Translation:<translation>
    Names:<list of names in the summary>
    Output JSON: <json with the french summary and num_names>

    Text:```{multi_task_prompt_text}```
    """

    response=get_completion(multi_task_prompt)
    return response