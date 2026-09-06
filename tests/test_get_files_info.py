from pycodeagent.tools.get_files_info import get_files_info


def test_get_files_info():
    print(get_files_info("examples/calculator", "."))
    print(get_files_info("examples/calculator", "pkg"))
    print(get_files_info("examples/calculator", "/bin"))
    print(get_files_info("examples/calculator", "../"))


if __name__ == "__main__":
    test_get_files_info()
