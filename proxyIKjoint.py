'''
Make proxies for three joints and a pole vector controller and
finalize into an IK 3-joint-combo rig for arms or legs
'''
import maya.cmds as cmds

class proxyIKjoint(object):

    #make UI
    def __init__(self):

        self.UIWindow = "proxJnt_Window"
        self.UITitle = "Proxy-based Joint Creator"
        self.UISize = (400, 400)

        #close old window if opened
        if cmds.window(self.UIWindow, exists = True):
            cmds.deleteUI(self.UIWindow, window = True)
    
        #create new window
        cmds.window(self.UIWindow, title=self.UITitle, widthHeight=self.UISize)
        cmds.columnLayout(adjustableColumn = True)
        cmds.text(self.UITitle)
        cmds.separator(height=20)

        #get user input for joint names
        self.jnt_1_name = cmds.textFieldGrp(label="Joint 1 Name:")
        self.jnt_2_name = cmds.textFieldGrp(label="Joint 2 Name:")
        self.jnt_3_name = cmds.textFieldGrp(label="Joint 3 Name:")

         #make button
        cmds.button(label="Create Proxies", command=self.make_proxies)
        cmds.button(label="Finalize Rig", command=self.make_rig)

        #display new window
        cmds.showWindow()


    #define make proxy function
    def make_proxies(self, *args):
         #retreive proxy/joint names
        self.proxName_1 = cmds.textFieldGrp(self.jnt_1_name, q=True, text=True)
        self.proxName_2 = cmds.textFieldGrp(self.jnt_2_name, q=True, text=True)
        self.proxName_3 = cmds.textFieldGrp(self.jnt_3_name, q=True, text=True)
        #create proxies of 3 joints and 1 pole vector ctl
        self.prox_1 = cmds.spaceLocator(n=self.proxName_1+"_proxy")[0]
        self.prox_2 = cmds.spaceLocator(n=self.proxName_2+"_proxy")[0]
        self.prox_3 = cmds.spaceLocator(n=self.proxName_3+"_proxy")[0]
        self.prox_4 = cmds.spaceLocator(n=self.proxName_2+"_poleVector_proxy")[0]
        #move proxies to default locations
        cmds.setAttr(self.prox_1+'.translate', 0, 1, 0)
        cmds.setAttr(self.prox_2+'.translate', 2, 1, 0)
        cmds.setAttr(self.prox_3+'.translate', 4, 1, 0)
        cmds.setAttr(self.prox_4+'.translate', 2, 1, 2)
        #make a list for joint proxies
        self.jointProxy = [self.prox_1, self.prox_2, self.prox_3]

    #define finalize function
    def make_rig(self, *args):
        cmds.select(cl=True)
        for everyItem in self.jointProxy:
            jntLoc = cmds.xform(everyItem, q=True, t=True)
            self.jnt = cmds.joint(n= everyItem.replace('_proxy','_jnt'), position=jntLoc)
            print(self.jnt)




proxyIKjoint()