# PyCodeAgent

PyCodeAgent is a Python-based agentic AI coding assistant that uses LLM function calling to interact with a local codebase. The agent can inspect project structures, read and modify files, execute Python programs, analyse execution results, and iteratively work toward completing coding tasks.

The project was built to explore the core concepts behind AI coding agents, including tool calling, agent loops, structured tool schemas, filesystem interaction, and controlled code execution.

## Features

- **Project inspection** — Lists files and directories to understand the structure of a codebase.
- **File reading** — Reads source files selected by the agent.
- **File modification** — Creates and overwrites files based on the agent's decisions.
- **Python execution** — Executes Python files and captures both standard output and error output.
- **LLM function calling** — Exposes local Python functions to the language model through structured tool schemas.
- **Dynamic tool dispatch** — Maps LLM tool requests to the appropriate Python functions at runtime.
- **Iterative agent loop** — Allows the model to call multiple tools, inspect their results, and continue reasoning until it produces a final response.
- **Filesystem sandboxing** — Restricts file operations and code execution to a designated working directory, currently fixed in code (`examples/calculator`). Making this configurable at runtime is a planned improvement (see Future Improvements).
- **Verbose CLI mode** — Displays tool calls, tool results, and token usage for debugging and inspection.
- **Iteration limit** — Prevents uncontrolled infinite agent loops.

## How It Works

PyCodeAgent follows a simple agent loop:

```text
User Prompt
    ↓
LLM
    ↓
Select Tool
    ↓
Tool Dispatcher
    ↓
Execute Python Function
    ↓
Return Tool Result
    ↓
LLM analyses result
    ↓
Call another tool or return final response
```

For example, when asked to investigate a Python project, the agent can:

1. Inspect the project's files and directories.
2. Select and read relevant source files.
3. Reason about the code and identify required changes.
4. Modify the appropriate files.
5. Execute the program or its tests.
6. Inspect the execution results.
7. Continue iterating or return a final response.

## Available Tools

| Tool | Purpose |
| --- | --- |
| `get_files_info` | Lists files and directories inside the permitted working directory |
| `get_file_content` | Reads the contents of a selected file |
| `write_file` | Creates or overwrites files |
| `run_python_file` | Executes Python files and captures their output |

Each tool is exposed to the LLM using a structured function schema. The agent requests a tool and its arguments, while the application remains responsible for executing the actual Python function.

## Project Structure

```text
PyCodeAgent/
├── examples/
│   └── calculator/
├── src/
│   └── pycodeagent/
│       ├── agent/
│       ├── tools/
│       ├── __init__.py
│       ├── config.py
│       ├── main.py
│       └── prompts.py
├── tests/
├── .env.example
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

The `examples/calculator` project provides a small codebase that can be used to demonstrate and test the agent's ability to inspect, modify, and execute Python code.

## Installation

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- An API key for a supported LLM provider

Clone the repository:

```bash
git clone https://github.com/Jaber-Allawnah/python-coding-agent.git
cd PyCodeAgent
```

Install the project dependencies:

```bash
uv sync
```

Create a `.env` file based on `.env.example`:

```env
API_KEY=your_api_key_here
```

> Never commit your real API key to GitHub.

## Usage

Run the agent with a coding task:

```bash
uv run python -m pycodeagent.main "your prompt here"
```

For example:

```bash
uv run python -m pycodeagent.main "Use run_python_file to run tests.py"
```

Enable verbose mode to display tool calls and results:

```bash
uv run python -m pycodeagent.main "Use run_python_file to run tests.py" --verbose
```

## Safety

PyCodeAgent executes model-requested filesystem operations and Python programs. To reduce unintended access, tools are restricted to a designated working directory.

Requested paths are normalised and validated before operations are performed. Attempts to access paths outside the permitted working directory are rejected.

The project is intended for learning and experimentation. Run AI-generated code only in environments where you understand and accept the associated risks.

## Technologies

- Python
- OpenAI-compatible Python SDK
- OpenRouter
- LLM Function Calling / Tool Calling
- `subprocess`
- `argparse`
- `python-dotenv`
- uv

## What I Learned

Building PyCodeAgent provided practical experience with:

- Agentic AI architecture and multi-step agent loops
- LLM tool/function calling
- JSON-based tool arguments and schemas
- Dynamic function dispatch in Python
- Maintaining conversation context across agent iterations
- Filesystem operations and path validation
- Programmatic Python execution with `subprocess`
- Capturing `stdout`, `stderr`, and process exit codes
- CLI application development
- Defensive programming and execution boundaries

## Future Improvements

Potential improvements include:

- Support for additional programming languages
- Configurable working directories
- More granular tool permissions
- Improved error recovery and retry strategies
- Structured logging
- Additional automated tests
- Multiple LLM provider configurations
- Richer CLI output
- More advanced planning and tool-selection strategies

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

This project was developed while studying agentic AI and coding-agent concepts through the Boot.dev curriculum. The implementation was extended and organised as a portfolio project to demonstrate practical understanding of LLM tool calling, controlled code execution, and iterative agent workflows.

