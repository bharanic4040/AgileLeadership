"""
This file contains all the common constants required for Alerts, Toasters ,Selector Constants
for selecting the DOM Nodes
"""
class _LoginPageConstants:
    class ConstError(TypeError): pass
    def __init__(self):
        self.LOGIN_USERNAME_ID="userInput"
        self.LOGIN_PASSWORD_NAME="password"
        self.LOGIN_SUBMIT_BUTTON_CSS="input[type='submit']"
        self.LOGIN_WORKSPACE_LINK_CSS="div[class='sp-picker icon-workspace selectable']"
        self.LOGIN_WORKSPACE_MENU_ITEMS_CSS="div.simple-picker-menu-body div.simple-picker-menu-item"
        self.LOGIN_PROJECT_NAV_MENU_CSS="div.project-nav-container div.project-nav-label"
        self.LOGIN_PROJECT_MAIN_PLUS_ID="ygtvt1"
        self.LOGIN_PROJECT_SUB1_PLUS_ID="ygtvt2"
        self.LOGIN_PROJECT_SUB2_PLUS_ID="ygtvt3"
        self.LOGIN_ACTUAL_PROJECT_XPATH="//div[@class='link_container']/a" #xpath query will be further appended in the page object getter
        self.REPORTS_MAIN_TAB_CSS="div#header ul.nav-bar a[title='Reports']"
        self.TRACK_MAIN_TAB_CSS="div#header ul.nav-bar a[title='Track']"
        self.TRACK_MENU_ITEMS_CSS="div.menu-pane table.menu-table ul li a"
        self.REPORTS_MENU_ITEMS_CSS="div.menu-pane table.menu-table ul li a"

    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise(self.ConstError, "Can't rebind const(%s)"%name)
        self.__dict__[name]=value
import sys
sys.modules[__name__]=_LoginPageConstants()



        
