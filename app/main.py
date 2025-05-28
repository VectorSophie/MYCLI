import sys


def main():

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    enter = input()
    commarr=enter.split()
    command = commarr[0]
    args = commarr[1:] if len(commarr) > 1 else ""
    if command == "exit":
        sys.exit(0)
    elif command == "echo":
        print(*args)
    else:
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
