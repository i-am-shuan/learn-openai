# - Python Docstring(주석) 만들기
# 	- source: python-chatgpt/python_chatgpt/auto_docstring.py
# 	- import inspect
# 		- instpect.getsource(fucntion_name)
# 		- function 코드를 string 으로 반환
# 	- api: openai
# 	- model: text-davinci-003
# 	- prompt
# 		- Provide python docstring for the following function


import inspect
import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")

# def reverse_string(string: str) -> str:
#     """
#     Reverses the given string and returns the result.

#     Args:
#     string (str): The string to be reversed.

#     Returns:
#     str: The reversed string.
#     """
#     return string[::-1]

# # help function example
# print(help(reverse_string))

# # __doc__ method example
# print(reverse_string.__doc__)

def reverse_string(string: str) -> str:
    return string[::-1]

# print(inspect.getsource(reverse_string))

prompt = f"Provide python docstring for the following function: \n ```{inspect.getsource(reverse_string)}```"
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=300,
)
print(response['choices'][0]['text'])
