import sys


def main():

    sys.stdout.write("$ ")

    # Wait for user input
    enter = input()
    command = enter[:4]
    args = enter[4:]
    if command == "exit":
        sys.exit(0)
    elif command == "echo":
        print(args)

    print(f"{enter}: command not found")
    main()

if __name__ == "__main__":
    main()
