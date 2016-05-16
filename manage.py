# Sets the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from JSON-REST-API import app

manager = Manager(app)

manager.add_command("runserver", Server(
    user_debugger = True,
    user_reloader = True,
    host = '0.0.0.0')
    )

if __name__ == "__main__":
    manager.run()

#manager allows you to make own commands for terminal for the API
#server instance allows us to choose properties for server
