import sys


def main():

    sys.stdout.write("$ ")

    # Wait for user input
    command = input()
    if command[:4] == "exit":
        sys.exit(0)
    print(f"{command}: command not found")
    main()

if __name__ == "__main__":
    main()
