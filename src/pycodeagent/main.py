import argparse

from pycodeagent.agent.runner import run_agent


def parse_args():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str)
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    run_agent(args.user_prompt, verbose=args.verbose)


if __name__ == "__main__":
    main()
