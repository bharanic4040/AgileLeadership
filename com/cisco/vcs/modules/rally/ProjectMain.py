__author__ = 'bchennu'

from selenium.common.exceptions import TimeoutException
from com.cisco.vcs.common.PageCommon import *
from com.cisco.vcs.po.rally.LoginPage import LoginPage
from com.cisco.vcs.constants.RallyConstants import RallyConstants



class ProjectMain:
    def __init__(self):
        self.loginPage=LoginPage()
        self.consts=RallyConstants()
        self.success = False

    def startProcess(self):
        for item in self.consts.PROJS_ARRAY:
            try:
                print('Rally Project executing - '+item)
                self.startOver()
                self.runModule(item)
            except Exception as e:
             print(e)
        self.success = True
        return -1


     #this function is run for each project under rally,this actually kicks off other helper methods to show graphs or charts
    def runModule(self,module):
        sleepFor(self.consts.CLICK_AND_WAIT_TIME)
        #click the actual module link
        try:
            self.loginPage.getActualProject(module,5).click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            self.showTracks(self.consts.TRACK_MENU_ITEMS_ARRAY)
            self.showCharts(self.consts.REPORTS_MENU_ITEMS_ARRAY)
        except Exception as e:
            raise e

    def startOver(self):
        try:
            workElem=None
            try:
                workElem=self.loginPage.getWorkspaceLink(5)
            except Exception as e:
                while workElem is None:
                    sleepFor(self.consts.CLICK_AND_WAIT_TIME)
                    try:
                        workElem=self.loginPage.getWorkspaceLink(2)
                    except Exception as k:
                        workElem=None
            workElem.click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            self.loginPage.getDashboardMenuItem("SPVTG_VCBU_SystemsDev",10).click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            workElem.click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            self.loginPage.getDashboardMenuItem("SPVTG",10).click()
            sleepFor(3)
            elem=self.loginPage.getProjectMenu("Briggs Team",20)
            if elem is not None:
                elem.click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            doItAgain=False
            try:
                self.loginPage.getActualProject(self.consts.PROJS_ARRAY[0],5)
            except TimeoutException as e:
                doItAgain=True
            if doItAgain==False:
                return
            self.loginPage.getMainProject(20).click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            self.loginPage.getSub1Project(10).click()
            sleepFor(self.consts.CLICK_AND_WAIT_TIME)
            self.loginPage.getSub2Project(10).click()
            self.success=True
        except Exception as e:
            self.success=False
            raise e


    #this method shows the dashboard charts/graphs/data for a particular rally project under Reports menu
    def showCharts(self,arr):
        for chart in arr:
            self.loginPage.getReportsMainTab(10).click()
            elem=self.loginPage.getReportMenuItem(chart,10)
            if elem is not None:
                elem.click()
                sleepFor(self.consts.REPORT_SHOW_TIME)

    #this method shows the graphs/charts/data for a particular rally project under Track menu
    def showTracks(self,arr):
        for track in arr:
            self.loginPage.getTrackMainTab(10).click()
            sleepFor(2)
            elem=self.loginPage.getTrackMenuItem(track,10)
            if elem is not None:
                elem.click()
                sleepFor(self.consts.TRACK_SHOW_TIME)






