from genericpath import isfile
import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.normpath(os.path.join(working_abs, file_path))

    if os.path.commonpath([working_abs, file_abs]) != working_abs:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(file_abs):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    parent_dir = os.path.dirname(file_abs)
    if not os.path.exists(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'Error: {e}'

    with open(file_abs, "w") as f:
        try:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: {e}'
