# calculator/pkg/render.py

import json


def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    """Format the expression and result as a JSON string.

    Args:
        expression: The arithmetic expression that was evaluated.
        result: The result of the evaluation.
        indent: Number of spaces for JSON indentation (default: 2).

    Returns:
        A JSON-formatted string containing the expression and result.
    """
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)
