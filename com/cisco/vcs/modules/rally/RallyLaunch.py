from com.cisco.vcs.modules.rally.Login import Login
from com.cisco.vcs.modules.rally.ProjectMain import ProjectMain

class RallyLaunch:
    def __init__(self):
        pass

    def startLoginProcess(self):
        try:
            app=Login()
            app.startLoginProcess()
        finally:
           pass

    def startProcess(self):
        try:
            main=ProjectMain()
            return main.startProcess()
        finally:
           pass

