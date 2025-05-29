import sys
import os
import subprocess

def echo_cmd(args):
    print(" ".join(args))

def type_cmd(args, commands):
    if not args:
        return

    target = args[0]
    if target in commands:
        print(f"{target} is a shell builtin")
    else:
        result = findtarget(target)
        if result:
            print(f"{target} is {result}")
        else:
            print(f"{target}: not found")

def findtarget(target):
    path_env = os.environ.get("PATH", "")
    paths = path_env.split(":")
    for directory in paths:
        try:
            for file in os.listdir(directory):
                if file == target:
                    full_path = os.path.join(directory, file)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        return full_path
        except Exception:
            continue
    return None

def find_cmd(args):
    if not args:
        print("find: missing argument")
        return

    target = args[0]
    result = findtarget(target)
    if result:
        print(result)
    else:
        print(f"{target}: not found")

def main():
    commands = {
        "exit": lambda args: sys.exit(0),
        "echo": echo_cmd,
        "type": lambda args: type_cmd(args, commands),
        "find": find_cmd,
    }

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        enter = input()
        if not enter.strip():
            continue

        commarr = enter.split()
        command, args = commarr[0], commarr[1:]

        func = commands.get(command)
        if func:
            func(args)
        else:
            result = findtarget(command)
            if result:
                try:
                    subprocess.run(commarr)
                except Exception as e:
                    print(f"Execution failed: {e}")
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()