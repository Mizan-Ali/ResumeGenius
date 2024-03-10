# import os
# from open_ai_custom import *
# from section_type_const import *

# current_dir = os.curdir
# project_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
# output_dir = os.path.join(project_dir, 'output')
# latex_main_dir = os.path.join(project_dir, 'SampleResumeTemplate')
# latex_code_dir = os.path.join(latex_main_dir, 'src')

# latex_orig_dir_read_only = os.path.join(project_dir, 'OriginalResumeTemplate')
# latex_code_dir_read_only = os.path.join(latex_orig_dir_read_only, 'src')

# def generate_section_tex(section_type, user_input):
#     sample_file_path = os.path.join(latex_code_dir_read_only, section_file_map[section_type])
#     updated_sample_tex = openai_response(user_input, section_type, sample_file_path)
#     return updated_sample_tex


# # def generate_achievements_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'achievements.tex')
# #     updated_experience_tex = openai_response(user_input, "Achievements", sample_file_path)
# #     return updated_experience_tex

# # def generate_education_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'education.tex')
# #     updated_experience_tex = openai_response(user_input, "Education", sample_file_path)
# #     return updated_experience_tex

# # def generate_experience_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'experience.tex')
# #     updated_experience_tex = openai_response(user_input, "Experience", sample_file_path)
# #     return updated_experience_tex


# # def generate_heading_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'heading.tex')
# #     updated_experience_tex = openai_response(user_input, "Heading", sample_file_path)
# #     return updated_experience_tex

# # def generate_projects_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'projects.tex')
# #     updated_projects_tex = openai_response(user_input, "Projects", sample_file_path)
# #     return updated_projects_tex

# # def generate_skills_tex(user_input):
# #     sample_file_path = os.path.join(latex_code_dir_read_only, 'skills.tex')
# #     updated_experience_tex = openai_response(user_input, "Skills", sample_file_path)
# #     return updated_experience_tex