from langchain import *
import os

# get openai api key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


def run_prompt(data):
    return "ran prompt!"
