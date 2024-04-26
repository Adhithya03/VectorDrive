import os
import re

# Regex pattern to find \section{foobar} and \subsection{foobar}
pattern = r'\\(section|subsection)\{(.*?)\}'

# Function to convert matched text to uppercase
def convert_to_uppercase(match):
    return f'\\{match.group(1)}{{{match.group(2).upper()}}}'

# Walk through current directory and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        # Process only .tex files
        if file.endswith('.tex'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r+', encoding='utf-8') as f:
                content = f.read()
                # Replace matched text with uppercase version
                content_new = re.sub(pattern, convert_to_uppercase, content, flags=re.DOTALL)
                # Write changes back to file
                f.seek(0)
                f.write(content_new)
                f.truncate()