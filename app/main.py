import sys

def __echo__(args):
    print(" ".join(args))

def __type__(args, commands):
    if args and args[0] in commands:
        print(f"{args[0]} is a shell builtin")
    else:
        print(f"{args[0]}: not found")

def main():
    commands = {
        "exit": lambda args: sys.exit(0),
        "echo": __echo__,
        "type": lambda args: __type__(args, commands)
    }

    while True:
        sys.stdout.write("$ ")
        enter = input()
        if not enter.strip():
            continue

        commarr = enter.split()
        command, args = commarr[0], commarr[1:]

        func = commands.get(command)
        if func:
            func(args)
        else:
            print(f"{command}: command not found")

if __name__ == "__main__":
    main()
