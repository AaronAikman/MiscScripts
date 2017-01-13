# Aaron Aikman Copyright 2014
# wingExp
# Creates an expression for the flapping of wings
# Particularly useful for the wings of small insects
# Negation allows for creating the expression for a mirrored wing



import maya.cmds as cmds



def wingExp():
	#Defining Window
	wEWind = cmds.window(title="Flapping Wings")

	cmds.columnLayout()
	
	cmds.radioButtonGrp('whichAx', label='Axis', labelArray3=['X', 'Y', 'Z'], numberOfRadioButtons=3, select=1, cal=(1, 'left'), cw4=(30, 30, 30, 30))
	
	cmds.text(l='Speed')
	cmds.floatSliderGrp('speed', field=True, v=3, min=0.001, max=20, fmx=10000)

	cmds.text(l='Rotation Arc')
	cmds.floatSliderGrp('arc', field=True, v=45, min=1, max=100, fmx=10000)

	cmds.radioButtonGrp('neg', label='Negation', labelArray2=['Normal', 'Reversed'], numberOfRadioButtons=2, select=1, cal=(1, 'left'), cw3=(60, 60, 60))
	
	cmds.button(label="Create Expression", command="makeWingExp()")

	cmds.showWindow(wEWind)

def makeWingExp():
	#Defining Variables
	axis = cmds.radioButtonGrp('whichAx', q=True, select=True)
	neg = cmds.radioButtonGrp('neg', q=True, select=True)
	speed = cmds.floatSliderGrp('speed', q=True, v=True)
	arc = cmds.floatSliderGrp('arc', q=True, v=True)

	if (axis == 1):
		chosenAxis = "rotateX"
	elif (axis == 2):
		chosenAxis = "rotateY"
	elif (axis == 3):
		chosenAxis = "rotateZ"
	
	if (neg == 1):
		negated = 1
	elif (neg == 2):
		negated = -1
	
	#Defining Selection
	selection = cmds.ls( sl=True )
	
	#Creating Expression
	expContent = ( selection[0] + "." + str(chosenAxis) + " = ( " + str(negated) + "* sin (time * " + str(speed) + ") * " + str(arc) + ");" )

	cmds.expression(string=expContent)
	
#Run
wingExp()