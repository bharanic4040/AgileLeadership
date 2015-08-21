from com.cisco.vcs.common.PageCommon import *
from com.cisco.vcs.constants import PageConstants

class LoginPage:
    """
    page object for the login page in rally UI
    """

    def __init__(self):
        pass
    def getLoginUsernameText(self,secs=0):
        return waitForVisibilityOfId(secs, PageConstants.LOGIN_USERNAME_ID)
    def getLoginPasswordText(self,secs=0):
        return waitForVisibilityOfName(secs, PageConstants.LOGIN_PASSWORD_NAME)
    def getSubmitButton(self,secs=0):
        return waitForVisibilityOf(secs,PageConstants.LOGIN_SUBMIT_BUTTON_CSS)
    def getWorkspaceLink(self,secs=0):
        return waitForVisibilityOf(secs,PageConstants.LOGIN_WORKSPACE_LINK_CSS)

    def getDashboardMenuItem(self,find,secs=0):
        elems=waitForVisibilityOfMore(secs,PageConstants.LOGIN_WORKSPACE_MENU_ITEMS_CSS)
        for elem in elems:
            if elem.text==find:
                return elem
        return None

    def getProjectMenu(self,s,secs=0):
        elems=waitForVisibilityOfMore(secs,PageConstants.LOGIN_PROJECT_NAV_MENU_CSS)
        for elem in elems:
            if elem.text==s:
                return elem
        return None


    def getReportsMainTab(self,secs=0):
        return waitForVisibilityOf(secs,PageConstants.REPORTS_MAIN_TAB_CSS)

    def getTrackMainTab(self,secs=0):
        return waitForVisibilityOf(secs,PageConstants.TRACK_MAIN_TAB_CSS)


    def getMainProject(self,secs=0):
        return waitForVisibilityOfId(secs,PageConstants.LOGIN_PROJECT_MAIN_PLUS_ID)

    def getSub1Project(self,secs=0):
        return waitForVisibilityOfId(secs,PageConstants.LOGIN_PROJECT_SUB1_PLUS_ID)


    def getSub2Project(self,secs=0):
        return waitForVisibilityOfId(secs,PageConstants.LOGIN_PROJECT_SUB2_PLUS_ID)


    def getActualProject(self,proj,secs=0):
        xpathTxt=PageConstants.LOGIN_ACTUAL_PROJECT_XPATH+"[text()='"+proj+"']"
        elem=waitForVisibilityOfXPath(secs,xpathTxt)
        if elem.text==proj:
            return elem
        return None

    def getReportMenuItem(self,name,secs=0):
        elems=waitForVisibilityOfMore(secs,PageConstants.REPORTS_MENU_ITEMS_CSS)
        for elem in elems:
            if elem.text==name:
                return elem
        return None

    def getTrackMenuItem(self,name,secs=0):
        elems=waitForVisibilityOfMore(secs,PageConstants.TRACK_MENU_ITEMS_CSS)
        for elem in elems:
            if elem.text==name:
                return elem
        return None




















