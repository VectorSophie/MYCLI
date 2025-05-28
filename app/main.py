import sys


def main():

    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    enter = input()
    commarr=enter.split()
    if not commarr:
        continue
    command = commarr[0]
    args = commarr[1:]
    if command == "exit":
        sys.exit(0)
        continue
    elif command == "echo":
        print(" ".join(args))
        continue

    print(f"{command}: command not found")

if __name__ == "__main__":
    main()
