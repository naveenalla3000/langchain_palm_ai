import os
from src.langchainplamai.logger import logging
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
load_dotenv()

KEY = os.getenv("GOOGLE_API_KEY")
MODEL = "models/text-bison-001"
llm = GoogleGenerativeAI(model=MODEL, google_api_key=KEY)

history = []  # List to keep track of the history of interactions

async def invoke_response(user_input):
    prompt = f'''
    You are an expert at coding, problem solving, data structures and algorithms, and Linux and Unix. 
    Simply, you are a software expert with 20+ years of experience in Java and Python languages.
    OOP and functional programming are your favorite paradigms.
    Now your douty is to help a junior developer to solve a problem.
    The problem is:

        {user_input}

    '''
    logging.info("Generated prompt: %s", prompt)  
    try:
        res = llm.invoke(prompt)
        logging.info("Response from LLM: %s", res)
        
        
        return res
    except IndexError as e:
        logging.info("IndexError caught: %s", str(e))
        raise e