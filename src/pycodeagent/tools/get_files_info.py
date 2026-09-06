import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_abs = os.path.abspath(working_directory)
        directory_abs = os.path.normpath(os.path.join(working_abs, directory))

        if os.path.commonpath([working_abs, directory_abs]) != working_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(directory_abs):
            return f'Error: "{directory}" is not a directory'

        content = os.listdir(directory_abs)

        if directory == ".":
            result = "Result for current directory:\n"
        else:
            result = f"Result for '{directory}' directory:\n"

        for item in content:
            item_path = os.path.join(directory_abs, item)
            result += (
                f"- {item}: "
                f"file_size={os.path.getsize(item_path)} bytes, "
                f"is_dir={os.path.isdir(item_path)}\n"
            )
        return result

    except Exception as e:
        return f"Error: {e}"
