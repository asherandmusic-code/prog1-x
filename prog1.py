#Program 1

#-----import-libs-----

from datetime import datetime
from pathlib import Path
import importlib

commands = {}
h = '''
Available commands:
help           - shows all available commands
end            - ends program
time           - shows current time
clear          - clears command line
'''

plugin_folder = Path("comms")

for file in plugin_folder.glob("*.py"):

    if file.name == "__init__.py":
        continue

    module_name = f"comms.{file.stem}"
    module = importlib.import_module(module_name)

    if hasattr(module, "plug"):
        commands.update(module.plug["comms"])
        h += module.plug["desc"]+"\n"

#-----import-libs-----

#-----Variable-Initialisation-----

log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
i = True

#-----Variable-Initialisation-----

#-----Log-In-----
mt = input(":")
user = str(input("User ID:"))
password = str(input("Password:"))
#-----Log-In-----


if mt == "" and user == "SunxMoon" and password == "1945" :

    print(f"\nWelcome {user}")

    def c():
        
        while i == True:
            cmd = str(input("c/"))

            if cmd in commands:
                commands[cmd]()

            elif cmd == "help":
                print(f"{h}\n")
                
            elif cmd == "end":
                print("Thanks for using prog1")
                break

            elif cmd == "time":
                print("\n",datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"\n")

            elif cmd == "clear":
                print("\n"*25)
          
            elif cmd not in commands:
                print("\nCommand not available...Try again.\n") 
                    
    fxc = str(input("File(f) or Command line(c):"))

    if fxc == "f":
        print("\nIn progress - redirect to Command line\n")
        c()

    elif fxc == "c":
        c()
        
    
