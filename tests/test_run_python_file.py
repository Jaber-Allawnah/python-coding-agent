from pycodeagent.tools.run_python_file import run_python_file

def test_run_python_file():
    print(run_python_file("examples/calculator", "main.py"))
    print(run_python_file("examples/calculator", "main.py", ["3 + 5"]))
    print(run_python_file("examples/calculator", "tests.py"))
    print(run_python_file("examples/calculator", "../main.py"))
    print(run_python_file("examples/calculator", "nonexistent.py"))
    print(run_python_file("examples/calculator", "lorem.txt"))

if __name__ == "__main__":
    test_run_python_file()
