# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = OpenAI( 
#     api_key=os.environ.get('OPENAI_KEY')
# )

# response = client.responses.create(
#     model="gpt-5",
#     input="Write a one-sentence bedtime story about a unicorn."
# )

# print(response.output_text)

from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_KEY"))
try:
    # response = client.responses.create(
    #     model="gpt-5",
    #     input="Write a one-sentence bedtime story about a unicorn."
    # )

    # # robust way to print output across SDK versions
    # print(response.output[0].content[0].text)
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": 'system', "content": "You are a virtual assitant."},
            {"role": 'user', "content": "What is coding"},
        ]
    )

    print(completion.choices[0].message.content)

except Exception as e:
    print(e)



print("The program ends")