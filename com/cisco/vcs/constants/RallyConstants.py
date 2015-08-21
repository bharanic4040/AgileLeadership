class RallyConstants:

    class ConstError(TypeError): pass

    def __init__(self):
     #list of rally projects for automation to be run on
     self.PROJS_ARRAY = ['Services Management Block','DBDS Chennai UI Framework team' , 'DBDS Chennai DTACS Development']
     #list of items under Track menu to run the automation on
     self.TRACK_MENU_ITEMS_ARRAY=['Iteration Status' , 'Iteration Tracking Board']
     #list of items under Reports menu to run the automation on
     self.REPORTS_MENU_ITEMS_ARRAY=['Super Customizable Iteration Chart','Scope Change Report','Active Defect Charts','Enhanced Velocity Chart','Iteration Traceability']
     self.REPORT_SHOW_TIME=10 #time to show each item or graph under Reports menu
     self.TRACK_SHOW_TIME=10  # time to show each item or graph under Track menu
     #general wait time for click- throughout the rally app
     self.CLICK_AND_WAIT_TIME=3


    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise (self.ConstError, "Can't rebind const(%s)" % name)
        self.__dict__[name] = value
