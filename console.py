#!/usr/bin/python3

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, line):
	return True

    def do_EOF(self, line):
	print("\n")
	return True

    def do_help(self, line):
	print("Description of given command")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
