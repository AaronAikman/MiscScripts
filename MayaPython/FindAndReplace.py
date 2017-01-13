# Aaron Aikman Copyright 2014
# recordTransformations
# Saves selected transformations information to selected text file

import maya.cmds as cmds


# Defining Window
def recordTransformations():
	rtWindow = cmds.window(title="Record Transforms")
	cmds.columnLayout()
	cmds.checkBox('tBox', label='Translation', value=True)
	cmds.checkBox('rBox', label='Rotation', value=True)
	cmds.checkBox('sBox', label='Scale', value=True)
	cmds.button(label="Choose File to Save", c="chooseAndRun()")
	cmds.showWindow(rtWindow)

 
# Process
def chooseAndRun():
	
	# Defining Variables
	tCh = cmds.checkBox('tBox', query=True, value=True)
	rCh = cmds.checkBox('rBox', query=True, value=True)
	sCh= cmds.checkBox('sBox', query=True, value=True)
	
	# Accessing File
	theFile = cmds.fileDialog()
	if( len(theFile) == 0 ): return
	fileOBJ = open(theFile, "w")
	
	# Defining Selection
	selection = cmds.ls( sl=True )
	
	for i in range (len(selection)):
		
		# Writing Info
		fileOBJ.write(selection[i])
		fileOBJ.write("\n")
		
		if (tCh == True):
			objLoc = cmds.xform(selection[i], q=True, t=True)# Finding Transforms
			fileOBJ.write('Translation = ' + str(objLoc))
			fileOBJ.write("\n")
			
		elif (rCh == True):
			objLoc = cmds.xform(selection[i], q=True, ro=True)# Finding Transforms
			fileOBJ.write('Rotation = ' + str(objLoc))
			fileOBJ.write("\n")
			
		elif (sCh == True):
			objLoc = cmds.xform(selection[i], q=True, s=True, r=True)# Finding Transforms
			fileOBJ.write('Scale = ' + str(objLoc))
			fileOBJ.write("\n")
			
		else:
			cmds.error("No transforms selected")
		
		fileOBJ.write("\n")
		
	fileOBJ.close()
	
#Run
recordTransformations()