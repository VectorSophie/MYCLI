import sys


def main():
    while True:
        sys.stdout.write("$ ")

    enter = input()
    commarr=enter.split()

    command = commarr[0]
    args = commarr[1:]
    if command == "exit":
        sys.exit(0)
        continue
    elif command == "echo":
        print(" ".join(args))
        continue
    else:
        print(f"{command}: command not found")

if __name__ == "__main__":
    main()
