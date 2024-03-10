# Resume Optimizer

The Resume Optimizer is a Python-based tool designed to enhance and optimize resumes by taking user input for various sections such as Experience, Education, Projects, etc., and integrating it into a sample LaTeX template. The tool ensures that the generated content is ATS (Applicant Tracking System) friendly and adheres to specified word limits for each section.

## Features

- **User Input Integration:** Accepts user input for different resume sections, including Experience, Education, Projects, etc.
- **Sample LaTeX Template Integration:** Utilizes sample LaTeX templates for various resume sections and automatically customizes them using the large language model's response.
- **Content Optimization:** Enhances user input by adding necessary keywords, ensuring ATS compatibility, and maintaining word limits for each section.
- **Reverse Chronological Order:** Populates user data in reverse chronological order for Experience, Education, and Projects sections.
- **Customizable Output:** Generates a raw Python string that can be easily integrated into existing LaTeX files.
- **Content Integrity:** Ensures that the generated content does not exceed the content limit of the sample LaTeX code, preventing the resume from becoming too lengthy.

## What This Script Does

This script allows the user to briefly explain details about their experience, education, skills, etc., without worrying much about the proper keywords or whether their inputs are grammatically and ATS compliant. All these tasks are handled by the script.

The user's input is fed into a finetuned large language model (LLM) that takes care of everything, from ensuring that the grammar is correct to enhancing the user's input with proper keywords and technical terms. The LLM's response is then fed into a LaTeX file, and the script compiles the LaTeX and returns a PDF. This PDF serves as a complete resume of the individual.

## Prerequisites

Before using the Resume Optimizer tool, ensure that the following prerequisites are met:

- **pdflatex:** Install a LaTeX distribution such as TeX Live or MiKTeX, which includes the pdflatex command for compiling LaTeX documents into PDF format.

- **OpenAI API Key:** Obtain an API key from OpenAI to use their language model for content optimization. You can sign up for an API key on the OpenAI website.

## Usage

To use the Resume Optimizer tool, follow these steps:

1. Clone the repository to your local machine:
2. Navigate to the /python directory:
3. Ensure that Python 3.x is installed on your system.
4. create a new virual environment and run this
   ```
   pip install -r requirements.txt
   ```
5. Run the `resume_optimizer.py` script and provide user input for each resume section as prompted.
6. The script will generate the final optimized LaTeX content, which you can use directly without the need for customizing the sample LaTeX templates.
7. Compile the LaTeX files to generate the final resume document.

## Dependencies

The project requires the following dependencies:

- Python 3.x

## Contributing

Contributions to the Resume Optimizer project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


