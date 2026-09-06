import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_abs = os.path.abspath(working_directory)
    file_abs = os.path.normpath(os.path.join(working_abs, file_path))
    if os.path.commonpath([working_abs, file_abs]) != working_abs:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_abs):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", file_abs]
    if args:
        command.extend(args)

    try:
        output = subprocess.run(command, capture_output=True, text=True, timeout=30)
        final_string = f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
"""
        if output.returncode != 0:
            return f"Process exited with code {output.returncode}"

        if output.stdout == "" and output.stderr == "":
            return "No output produced"

        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"
