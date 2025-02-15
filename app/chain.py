from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

with open("openai.txt") as f:
    docs = f.read()


#task : 사용자 입력
#instruction : 참고 자료 (.txt)

template = """Based on the following instrutions, help me write a good prompt TEMPLATE for the following task:

{task}

Notably, this prompt TEMPLATE expects that additional information will be provided by the end user of the prompt you are writing. For the piece(s) of information that they are expected to provide, please write the prompt in a format where they can be formatted into as if a Python f-string.

When you have enough information to create a good prompt, return the prompt in the following format:\n\n```prompt\n\n...\n\n```

Instructions for a good prompt:

{instructions}
"""
prompt = ChatPromptTemplate.from_messages([("system", template)]).partial(
    instructions=docs
)

chain = (
    prompt | ChatOpenAI(model="gpt-4-turbo-preview", temperature=0) | StrOutputParser()
)
