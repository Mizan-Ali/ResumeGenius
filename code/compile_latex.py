import subprocess
import os
from datetime import datetime

def compile_latex(output_directory, latex_dir):
    # Change the working directory to ResumeBuilder/SampleResumeTemplate
    os.chdir(latex_dir)

    # Execute pdflatex to compile LaTeX code into a PDF
    subprocess.run(['pdflatex', '-output-directory', output_directory, 'resume.tex'])

    # Generate a unique filename for the output PDF using timestamp
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_filename = f'resume_{timestamp}.pdf'
    output_path = os.path.join(output_directory, output_filename)

    # Rename the generated PDF to the unique filename
    os.rename(os.path.join(output_directory, 'resume.pdf'), output_path)

    # Delete non-PDF files in the output directory
    for filename in os.listdir(output_directory):
        if filename != output_filename and not filename.endswith('.pdf'):
            file_path = os.path.join(output_directory, filename)
            os.remove(file_path)