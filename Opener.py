from com.cisco.vcs.modules.rally.RallyLaunch import RallyLaunch
from com.cisco.vcs.common.PageCommon import *
import os,sys,socket
from threading import Timer

"""
Requirements:
------------
Note: working fine with mozilla firefox version 30 .

a.Mozilla Firefox 30
b.python 3.4
c.selenium [ - 3rd party python library ]
"""


#this method creates the firefox profile to aid in SSO login to Rally app
def createProfile():
    pr = webdriver.FirefoxProfile('C:\Program Files (x86)\Mozilla Firefox')
    pr.set_preference('network.http.phishy-userpass-length',255)
    pr.set_preference('network.automatic-ntlm-auth.trusted-uris','wwwin-sso.cisco.com')
    return pr


def automate(mod):
    initDriver(createProfile())
    loadUrl("https://us1.rallydev.com/#/9561764839d/dashboard")
    launch=RallyLaunch()
    launch.startLoginProcess()
    sleepFor(5)
    loadUrl("https://sso.rallydev.com/sp/startSSO.ping?PartnerIdpId=cloudsso.cisco.com")
    sleepFor(8)
    return launch.startProcess()



def main(argv):
    while True:
        print("new run ............")
        close=automate('rally')
        if close==-1:
            print('closing browser.....')
            force_timeout() #quitBrowser()


def force_timeout():
    os.system('taskkill /im firefox.exe /f /t')


if __name__ == "__main__":
    main(sys.argv[1:])
