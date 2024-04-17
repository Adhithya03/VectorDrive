import os

def collect_tex_files(directory):
    """
    Walks through the directory and finds all .tex files.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                yield os.path.join(root, file)

def write_to_output(output_path, tex_files):
    """
    Writes the contents of each .tex file to the output file, wrapped in XML-like tags.
    """
    with open(output_path, 'w') as output_file:
        for tex_file in tex_files:
            with open(tex_file, 'r') as file:
                contents = file.read()
                # Create XML-like tags based on the file path
                tag = f"<{tex_file}>"
                closing_tag = f"</{tex_file}>"
                # Write to the output file
                output_file.write(f"{tag}\n{contents}\n{closing_tag}\n\n")

def main():
    directory = "E:/VectorDrive"
    output_path = "output.txt"
    tex_files = list(collect_tex_files(directory))
    write_to_output(output_path, tex_files)
    print(f"All .tex files have been compiled into {output_path}")

if __name__ == "__main__":
    main()