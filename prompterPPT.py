import os
import re
import string

# Regex pattern to find \subsubsection{foobar}
pattern = r'\\subsubsection\{(.*?)\}'

# Function to convert matched text to title case
def convert_to_titlecase(match):
    return f'\\subsubsection{{{string.capwords(match.group(1))}}}'

# Walk through current directory and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        # Process only .tex files
        if file.endswith('.tex'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r+', encoding='utf8') as f:
                content = f.read()
                # Replace matched text with title case version
                content_new = re.sub(pattern, convert_to_titlecase, content, flags=re.DOTALL)
                # Write changes back to file
                f.seek(0)
                f.write(content_new)
                f.truncate()