import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai_api_key=os.environ["OPENAI_API_KEY"]


from langchain_openai import OpenAI
llmModel= OpenAI()

# for chunk in llmModel.stream(
#   "tell me about the pm modi in details."
# ):
#   print(chunk, end="", flush=True)
  
  
creativellmModel=OpenAI(temperature=0.9)
response=creativellmModel.invoke("tell me one fact about the kennedy family")
print(response)