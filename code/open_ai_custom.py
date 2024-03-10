import os
import constants
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

# Access the API key from environment variables
api_key = os.getenv("API_KEY")

current_dir = os.curdir
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
output_dir = os.path.join(project_dir, 'output')
latex_main_dir = os.path.join(project_dir, 'SampleResumeTemplate')
latex_code_dir = os.path.join(latex_main_dir, 'src')

latex_orig_dir_read_only = os.path.join(project_dir, 'OriginalResumeTemplate')
latex_code_dir_read_only = os.path.join(latex_orig_dir_read_only, 'src')



client = OpenAI(base_url='https://api.naga.ac/v1', api_key=api_key)

def openai_response(user_input, section_name, sample_tex_file_path):
    # Define the path to the experience.tex file    
    sample_latex_code = ""
    # Read the contents of the existing experience.tex file
    with open(sample_tex_file_path, 'r') as file:
        sample_latex_code = file.read()
    updated_input_prompt = constants.INPUT_PROMPT.format(section_name=section_name, user_input=user_input, sample_latex_code=sample_latex_code)

    # initialize openai, supply the initial_prompt, the give it the updated_input_prompt
    # then return the openai response.
    ai_response_tex = generate_response(updated_input_prompt)
    print(ai_response_tex)
    return ai_response_tex

# sample_file_path = os.path.join(latex_code_dir_read_only, 'experience.tex')
# print(sample_file_path)
# print(openai_response("Hello this is a test experience", "Experience", sample_file_path))

def prepare_messages_list(UPDATED_INPUT_PROMPT):
  messages=[{'role': 'user', 'content': constants.INITIAL_PROMPT}, {'role': 'user', 'content': UPDATED_INPUT_PROMPT}]
  return messages

def generate_response(UPDATED_INPUT_PROMPT):
  response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=prepare_messages_list(UPDATED_INPUT_PROMPT)
  )
  response = response.choices[0].message.content
  print("***************** AI RESPONSE ****************************")
  print(response)
  return response