import re
import os
from dotenv import load_dotenv

# loading the environment variables from .env file
load_dotenv()


def update_environment_variable(file_path, temp_file, pattern, replace):
    # array to store the contents
    updated_lines = []
    changes_made = False

    os.chmod(file_path, 0o755)

    print(f"Opening file: {file_path}")

    try:
        with open(file_path, "r") as fin:
            for line in fin:
                # Loop through each line to search for the line that matches the pattern
                if re.search(pattern, line):
                    print(f" Found:  {line.strip()}")
                    updated_line = re.sub(pattern, replace, line)
                    print(f" Update: {updated_line.strip()}\n")
                    if line != updated_line:
                        changes_made = True
                    updated_lines.append(updated_line)
                else:
                    updated_lines.append(line)

        if changes_made:
            with open(temp_file, "w") as fout:
                fout.writelines(updated_lines)

            # replace the original file with the newly updated file
            os.remove(file_path)
            os.rename(temp_file, file_path)
            print(f"{file_path} updated with build number {build_num}.\n")
        else:
            print("No changes needed — file is already up to date!\n")

    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except PermissionError:
        print(f"Permission denied for file {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Getting the environment variables from .env file
    build_num = os.getenv("BuildNum")

    # dynamically getting the source path from the environment variable
    source_path = os.getenv("SourcePath")
    if source_path in [None, "DEFAULT"]:
        source_path = os.getcwd()

    # file paths to be updated
    sconstruct_file_path = os.path.join(
        source_path, "Test", "develop", "global", "src", "SConstruct"
    )
    version_file_path = os.path.join(
        source_path, "Test", "develop", "global", "src", "VERSION"
    )

    # patterns to search for in the files
    sconstruct_pattern = r"point\s*=\s*\d+"
    version_pattern = r"ADLMSDK_VERSION_POINT\s*=\s*\d+"

    # replacements strings when the patterns found a match
    sconstruct_replace = f"point = {build_num}"
    version_replace = f"ADLMSDK_VERSION_POINT = {build_num}"

    # temp file to store the updated contents
    # the original file is deleted and replaced with the temp file
    sconstruct_temp_path = sconstruct_file_path + "1"
    version_temp_path = version_file_path + "1"

    # calling sconstruct
    update_environment_variable(
        sconstruct_file_path,
        sconstruct_temp_path,
        sconstruct_pattern,
        sconstruct_replace,
    )

    # calling version
    update_environment_variable(
        version_file_path,
        version_temp_path,
        version_pattern,
        version_replace,
    )

    print("Operation Completed!")
