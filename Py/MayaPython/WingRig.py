# Aaron Aikman Copyright 2014
# wingRig
# Create and Place Locators for the Shoulder, Elbow, and Wrist of the Wing
# Creates Joints based upon user input



import maya.cmds as cmds
import math


#Defining the Window
def wingRig():
	winName = cmds.window(title="Wing Joint Creator")
	cmds.columnLayout()
	
	cmds.text(label="""\n Create and Place the Locators at the Left "Shoulder," \n "Elbow," and "Wrist" of the Wing\n""")
	cmds.button(label="Create Joint Locators", command="makeLocators()")
	cmds.button(label="Select Shoulder Locator", command="selLoc(1)")
	cmds.button(label="Select Elbow Locator", command="selLoc(2)")
	cmds.button(label="Select Wrist Locator", command="selLoc(3)")
	
	cmds.text(label="Bone Length")
	cmds.floatSliderGrp("boneLength", field=True, v=3, min=0.01, max=100, fmx=100000)
	
	cmds.text(label="Length of Subsequent Bones")
	cmds.floatSliderGrp("nextBoneLength", field=True, pre=2, v=0.66, min=0.01, max=1)
	
	cmds.text(label="Number of Fingers")
	cmds.intSliderGrp("fingerNum", field=True, v=4, min=1, max=10, fmx=50)
	
	cmds.text(label="Number of Finger Joints")
	cmds.intSliderGrp("fJointNum", field=True, v=3, min=1, max=10, fmx=50)
	
	cmds.text(label="Finger Spread")
	cmds.floatSliderGrp("fingerSpread", field=True, v=1, min=0.01, max=10, fmx=100)

	cmds.button(label="Create Joints", command="makeJoints()")
	cmds.showWindow(winName)

 

# Making Locators
def makeLocators():
	shoulderLoc = cmds.spaceLocator( p=(0, 0, 0), n='ShoulderJointLocator')
	elbowLoc = cmds.spaceLocator( p=(0, 0, 0), n='ElbowJointLocator')
	wristLoc = cmds.spaceLocator( p=(0, 0, 0), n='WristJointLocator')

def selLoc(lChoice):
	if (lChoice == 1):
		cmds.select('ShoulderJointLocator')
	elif (lChoice == 2):
		cmds.select('ElbowJointLocator')
	elif (lChoice == 3):
		cmds.select('WristJointLocator')

# Making Joints
def makeJoints():
	# Defining Variables
	jointLength = cmds.floatSliderGrp("boneLength", query=True, value=True)
	fNum = cmds.intSliderGrp("fingerNum", query=True, value=True)
	fJNum = cmds.intSliderGrp("fJointNum", query=True, value=True)
	fSpread = cmds.floatSliderGrp("fingerSpread", query=True, value=True)
	nBLength = cmds.floatSliderGrp("nextBoneLength", query=True, value=True)

	# Finder Locator Vectors
	shoulderPos = cmds.xform('ShoulderJointLocator', q=True, t=True, ws=True)
	elbowPos = cmds.xform('ElbowJointLocator', q=True, t=True, ws=True)
	wristPos = cmds.xform('WristJointLocator', q=True, t=True, ws=True)
	

	cmds.select( clear=True )
	
	# Creating Initial Joints
	cmds.joint(a=True, p=(shoulderPos), n='L_Wing_ShoulderJoint')
	cmds.joint(a=True, p=(elbowPos), n='L_Wing_ElbowJoint')
	wristJoint = cmds.joint(a=True, p=(wristPos), n='L_Wing_WristJoint')
	
	# Defining Variables for ForLoop
	startPos = -fSpread / 2
	fingerGap = fSpread / (fNum-1)
	
	# Creating Fingers
	for f in range(fNum):
	
		newJointLength = (jointLength*nBLength)
	
		cmds.select('L_Wing_WristJoint')
		
		cmds.joint( r=True, p=( -jointLength, (startPos + (f*fingerGap)), 0), n='L_Wing_Finger'+(str(f+1))+'Joint_Knuckle') 
		
		# Creating Digits
		for j in range(fJNum):
			newJointLength = (newJointLength*nBLength)
			print(newJointLength)
			cmds.joint( r=True, p=( -newJointLength, 0, 0), n='L_Wing_Finger'+(str(f+1))+'Joint_'+(str(j+1))+'Digit')
			
	
	# Deleting Locators
	cmds.delete( 'ShoulderJointLocator', 'ElbowJointLocator', 'WristJointLocator')
	
	cmds.select ('L_Wing_ShoulderJoint', r=True)
	
#Run
wingRig()