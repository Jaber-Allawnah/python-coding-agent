import os
from pycodeagent.config import MAX_CHARS


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        file_abs = os.path.normpath(os.path.join(working_abs, file_path))

        if os.path.commonpath([working_abs, file_abs]) != working_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_abs):
            f'Error: File not found or is not a regular file: "{file_path}"'

        file_content = ""
        with open(file_abs, "r") as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return file_content

    except Exception as e:
        return f"Error: {e}"
