# Aaron Aikman Copyright 2014
# keyUndulation
# Creates keyframes for undulation
# Good for bouncing objects, pistons, and undulating particles
# Default values are set to demonstrate a bouncing object



import maya.cmds as cmds
import math


#Defining the Window
def keyUndulation():
	winName = cmds.window(title="Automated Undulation")
	cmds.columnLayout()
	
	
	cmds.text(label="Height of Change")
	cmds.floatSliderGrp("yChange", field=True, v=50, min=1, max=100, fmx=10000)
	
	cmds.text(label="Start Keyframe")
	cmds.intSliderGrp("sKey", field=True, v=1, min=1, max=2000, fmx=10000)
	
	cmds.text(label="End Keyframe")
	cmds.intSliderGrp("eKey", field=True, v=1000, min=2, max=2000, fmx=10000)
	
	cmds.text(label="Number of Keys")
	cmds.intSliderGrp("keys", field=True, v=7, min=1, max=50, fmx=10000)
	
	cmds.text(label="Stretch Amount")
	cmds.floatSliderGrp("stretch", field=True, v=1.2, min=1, max=2, fmx=100)
	
	cmds.text(label="Squash Amount")
	cmds.floatSliderGrp("squash", field=True, v=1.2, min=1, max=2, fmx=100)
	
	
	cmds.button(label="Animate", command="setKeys()")
	cmds.showWindow(winName)

 

# Making Joints
def setKeys():
	# Defining Variables
	yChange = cmds.floatSliderGrp("yChange", q=True, v=True)
	sKey = cmds.intSliderGrp("sKey", query=True, value=True)

	eKey = cmds.intSliderGrp("eKey", query=True, value=True)

	keys = cmds.intSliderGrp("keys", query=True, value=True)
	
	stretch = cmds.floatSliderGrp("stretch", q=True, v=True)
	squash = cmds.floatSliderGrp("squash", q=True, v=True)

	

	# Setting Start and End Keys
	objPos = cmds.xform(query=True, translation=True)
	
	cmds.currentTime(sKey, edit=True)
	cmds.setKeyframe( v=objPos[1], at='translateY' )
	cmds.setKeyframe(at='scale' )
	

	cmds.currentTime(eKey, edit=True)
	cmds.setKeyframe( v=objPos[1], at='translateY' )
	cmds.setKeyframe(at='scale' )
	
	# Defining Additional Variables
	inc = (eKey-sKey) / float(keys-1)
	newInc = inc/6
	
	dir = 1
	
	# Handling Key Increments
	for i in range(1, keys-1):
		
		# Translation
		cmds.currentTime(sKey + i*inc, edit=True)

		cmds.move(0, (dir*yChange), 0, relative=True)
		
		cmds.setKeyframe(at="translateY")
		
		# Scaling
		if (dir>0):
			cmds.scale(1, stretch, 1)
			cmds.setKeyframe(at='scale' )
		elif (dir<0):
			
			cmds.scale(1, 1, 1)
			cmds.setKeyframe( at='scale' )
			
			cmds.currentTime((sKey + i*inc + newInc), edit=True)
			
			cmds.scale(squash, 1, squash)
			cmds.setKeyframe(at='scale' )

		# Switching Direction
		dir = dir*-1
	
	# Reseting Time
	cmds.currentTime(sKey, edit=True)
	
# Run
keyUndulation()