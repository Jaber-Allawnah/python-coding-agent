import json
from pycodeagent.tools.get_file_content import get_file_content
from pycodeagent.tools.get_files_info import get_files_info
from pycodeagent.tools.run_python_file import run_python_file
from pycodeagent.tools.write_file import write_file
from collections.abc import Callable

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")

    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    function_map : dict[str , Callable[..., str]] = {
        "get_file_content": get_file_content,
        "get_files_info": get_files_info,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    function_to_call = function_map.get(function_name)
    if function_to_call is None:
        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": f"Error: Unknown function: {function_name}",
        }
    
    result = function_to_call(working_directory="examples/calculator", **function_args)
    
    return {
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": result,
    }
    