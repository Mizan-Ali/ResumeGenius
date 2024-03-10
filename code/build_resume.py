import os
from compile_latex import *
from open_ai_custom import *
from section_type_const import *

current_dir = os.curdir
project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
output_dir = os.path.join(project_dir, 'output')
latex_main_dir = os.path.join(project_dir, 'SampleResumeTemplate')
latex_code_dir = os.path.join(latex_main_dir, 'src')

latex_orig_dir_read_only = os.path.join(project_dir, 'OriginalResumeTemplate')
latex_code_dir_read_only = os.path.join(latex_orig_dir_read_only, 'src')

# Print directories for verification
print("Latex main directory:", latex_main_dir)
print("Latex code directory:", latex_code_dir)


def update_section(section_type, user_input):
    updated_section_tex = generate_section_tex(section_type, user_input)
    section_tex_file = os.path.join(latex_code_dir, section_file_map[section_type])

    # Read the contents of the existing projects.tex file
    with open(section_tex_file, 'r') as file:
        section_tex_content = file.read()

    # Replace the content of projects.tex with updated_projects_tex
    section_tex_content = updated_section_tex

    # Write the updated content back to the projects.tex file
    with open(section_tex_file, 'w') as file:
        file.write(section_tex_content)

    print(section_file_map[section_type] + " file updated successfully.")

def generate_section_tex(section_type, user_input):
    sample_file_path = os.path.join(latex_code_dir_read_only, section_file_map[section_type])
    updated_sample_tex = openai_response(user_input, section_type, sample_file_path)
    return updated_sample_tex


# update_section(ACHIEVEMENTS, user_input=test_achievements)
# update_section(HEADING, "phone : 9628146011, email: tony.stark@gmail, linkedin and github-username : tony-stark")
update_section(SKILLS, user_input="java, python, c, c++, javasript, Spring, sprintboot, aws, azure, cicd, cloud, machine learning, AI, langchain, meta ai, unit testing, postman")
# afer update
compile_latex(output_dir, latex_main_dir)