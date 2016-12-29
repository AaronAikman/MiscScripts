# Aaron Aikman Copyright 2014
# PhoenixTools

# Startup
import maya.cmds as cmds
import maya.mel

##########################################################################################
######################################  	UI      ######################################
##########################################################################################

# Defining the Window
def phoenixTools():
	pToolsWindow = cmds.window(menuBar=True, title="Phoenix Tools by Aaron Aikman 2014  Version 1.0.25", width=435, height=500)
	
	form = cmds.formLayout()
	tabs = cmds.tabLayout()
	cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )


	######################################  CREATION  ######################################


	child1 = cmds.scrollLayout( 'scrollLayout0' )



	#################
	##  Polygons   ##
	#################

	cmds.frameLayout( label='Polygons', borderStyle='out', cll=True, width=400)
	cmds.separator(style='none')


	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )


	cmds.button(label="Cube", command="cmds.polyCube()")
	cmds.button(label="2x2 Cube", command="cmds.polyCube(w=1, h=1, d=1, sx=2, sy=2, sz=2)")
	cmds.button(label="4x4 Cube", command="cmds.polyCube(w=1, h=1, d=1, sx=4, sy=4, sz=4)")
	cmds.button(label="Human Ref", command="cmds.polyCube(w=32, h=96, d=32, sx=1, sy=1, sz=1)")


	cmds.setParent( '..' )
	cmds.separator (w=400, style="in")
	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )

	cmds.button(label="Sphere", command="cmds.polySphere()")
	cmds.button(label="Diode Sphere", command="cmds.polySphere(sx=4, sy=3)")
	cmds.button(label="8x8 Sphere", command="cmds.polySphere(sx=8, sy=8)")
	cmds.button(label="12x12 Sphere", command="cmds.polySphere(sx=12, sy=12)")

	cmds.setParent( '..' )
	cmds.separator (w=400, style="in")
	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )

	cmds.button(label="Plane", command="cmds.polyPlane()")
	cmds.button(label="1x1 Plane", command="cmds.polyPlane(w=1, h=1, sx=1, sy=1)")
	cmds.button(label="4x4 Plane", command="cmds.polyPlane(w=1, h=1, sx=4, sy=4)")
	cmds.button(label="Floor Plane", command="cmds.polyPlane(w=1000, h=1000, sx=1, sy=1)")

	cmds.setParent( '..' )
	cmds.separator (w=400, style="in")
	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )

	cmds.button(label="Cylinder", command="cmds.polyCylinder()")
	cmds.button(label="Tri Cylinder", command="cmds.polyCylinder(sx=3, sy=1, sz=1)")
	cmds.button(label="12 Cylinder", command="cmds.polyCylinder(sx=12, sy=1, sz=1)")
	cmds.button(label="12x4 Cylinder", command="cmds.polyCylinder(sx=12, sy=4, sz=1)")

	cmds.setParent( '..' )
	cmds.separator (w=400, style="in")
	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )

	cmds.button(label="Torus", command="cmds.polyTorus()")
	cmds.button(label="Quad Torus", command="cmds.polyTorus(sx=4, sy=4)")
	cmds.button(label="Disk", command="makeDisk()")
	cmds.button(label="Prism", command="cmds.polyPrism()")

	cmds.setParent( '..' )
	cmds.separator (w=400, style="in")
	cmds.gridLayout( numberOfColumns=4, cellWidthHeight=(100, 25) )

	cmds.button(label="Cone", command="cmds.polyCone()")
	cmds.button(label="Helix", command="cmds.polyHelix()")
	cmds.button(label="Pipe", command="cmds.polyPipe()")
	cmds.button(label="Pyramid", command="cmds.polyPyramid()")



	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )

	#################
	##     Misc    ##
	#################

	cmds.frameLayout( label='Miscellaneous', borderStyle='out', cll=True, width=400)

	
	cmds.button(label="Create Geometry Tool", command="maya.mel.eval('setToolTo polyCreateFacetContext ;')")
	cmds.button(label="CV Curve Tool", command="cmds.CVCurveTool()")
	cmds.button(label="EP Curve Tool", command="cmds.EPCurveTool()")
	cmds.button(label="Locator", command="cmds.spaceLocator()")


	

	cmds.setParent( '..' )

	cmds.setParent( '..' )


	######################################  MODELING  ######################################


	child2 = cmds.scrollLayout( 'scrollLayout1' )

	
	#################
	##  Mirroring  ##
	#################


	cmds.frameLayout( label='Mirroring', borderStyle='out', cll=True, width=400)

	cmds.separator (style="none")
	
	cmds.radioButtonGrp('mDir', label='Direction', labelArray3=['X', 'Y', 'Z'], numberOfRadioButtons=3, select=1, cal=(1, 'right'), cw4=(80, 30, 30, 30))
	cmds.radioButtonGrp('mirrorMode', label='Mode', labelArray3=['Duplicate', 'Instance', 'Combined Geo'], numberOfRadioButtons=3, select=1, cal=(1, 'right'), cw4=(80, 70, 70, 100))
	
	cmds.rowLayout(numberOfColumns=2)

	cmds.text('                         ')
	cmds.button(label="Mirror Object", command="mirrorGeo()", ann='Select object and place pivot point on symmetry line')
	
	cmds.setParent( '..' )

	cmds.separator (style="none")

	cmds.setParent( '..' )

	##############
	##  Pivots 	##
	##############

	cmds.frameLayout( label='Pivot Manipulation', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')

	cmds.radioButtonGrp('pivPos', label='Pivot Location', labelArray2=['Bottom', 'Center'], numberOfRadioButtons=2, select=1, cal=(1, 'right'), cw3=(80, 60, 60))
	
	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')
	cmds.button(label="Move Pivots", command="movePivots()", ann='Select one or more objects to adjust the pivot point of.\nTool creates a temporary group and will alter the hierarchy.')

	cmds.text('                         ')
	cmds.button(label="Move Object to Origin", command="cmds.move(rpr=True)")

	cmds.setParent( '..' )
	cmds.separator(style='none')


	cmds.setParent( '..' )

	##############
	##  Manip 	##
	##############

	cmds.frameLayout( label='Manipulator Orientation', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')


	cmds.radioButtonGrp('manip', label=' ', labelArray2=['World Space', 'Object Space'], numberOfRadioButtons=2, select=1, cal=(1, 'right'), cw3=(80, 100, 60))
	

	cmds.rowLayout(numberOfColumns=2)

	cmds.text('                         ')

	cmds.button(label="Set Manipulator", command="setManip()", ann='Sets all transformation manipulators to world space or object space')
	
	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )


	##############
	##   Holes	##
	##############

	cmds.frameLayout( label='Hole Creation', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')



	cmds.intSliderGrp("numSides", l='Number of Sides', field=True, v=8, min=3, max=100, fmx=10000, cal=(1, 'right'), cw3=(100, 100, 200))
	

	cmds.rowColumnLayout(numberOfColumns=4)

	cmds.text('                         ')
	cmds.button(label="Create Disk", command="makeDisk()", ann='Creates a disk at the origin point')
	cmds.text('                         ')
	cmds.button(label="Help", command="makeHoleHelp()", ann='Click for instructions')
	cmds.setParent( '..' )

	cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(200, 25) )
	cmds.button(label="Snap Together Tool", command="maya.mel.eval('setToolTo snapTogetherToolCtx;')", ann='Click the face on the first object to be snapped into location\nafter clicking the face on the second object\nThen press enter')
	

	cmds.button(label="Combine", command="cmds.polyUnite()")

	cmds.button(label="Make Hole Tool", command="maya.mel.eval('MakeHoleTool;')", ann='Select the face being cut into\nThen select the face to become the hole\nThen press enter')
	cmds.button(label="Quadrangulate Geo", command="autoQuad()", ann='Select an N-gon to automatically quadrangulate')


	cmds.setParent( '..' )
	cmds.separator(style='none')
	cmds.separator(style='single')
	cmds.separator(style='none')
	cmds.button(label="Make Hole Based On Geo", command="makeHolebyGeo()", ann='Create a smaller face based upon the number of sides of the selected face')
	cmds.separator(style='none')
	cmds.separator(style='none')

	cmds.setParent( '..' )


	##############
	## Creasing ##
	##############

	cmds.frameLayout( label='Creasing', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')

	cmds.rowColumnLayout(numberOfColumns=2)
	cmds.text('                         ')
	cmds.button(label="Toggle Soft Edge Display", command="toggleSoftEdges()", ann='Toggle dashed lines for soft edges')

	cmds.setParent( '..' )
	cmds.floatSliderGrp("crsAmt", field=True, v=10, min=0.0, max=10, label='Crease Amount', cal=(1, 'right'), cw3=(90, 100, 210))
	
	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')
	cmds.button(label="Crease Hard Edges", command="creaseHardEdges()")
	cmds.text('                         ')
	cmds.button(label="Uncrease All", command="unCrease()", ann='Uncreases the edges of the selected object')

	

	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )
	cmds.setParent( '..' )


	######################################  UNWRAPPING  ######################################

	child3 = cmds.scrollLayout( 'scrollLayout2' )


	#################
	## UV Creation ##
	#################

	cmds.frameLayout( label='UV Creation', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')

	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')
	
	
	cmds.button(label="Unwrap Selected Faces", command="unwrapSelectedFaces()", ann='Unwraps the selected faces into contiguous shells')


	cmds.setParent( '..' )


	cmds.separator(style='single')

	cmds.radioButtonGrp('mode', label='Mode', labelArray2=['Unstretched', 'Optimized'], numberOfRadioButtons=2, select=1, cal=(1, 'right'), cw3=(80, 100, 100))
	


	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')

	
	cmds.button(label="Unwrap Cylindrical", command="unwrapCylindrical()", ann='Select a seam of the cylindrical object to unfold\nUnstretched mode will have no distortion,but will be less optimal for UV placement\nOptimized mode will unwrap into a shell where each face is a square\nAn optimized pipe can then be unfolded using Unfold Pipe')



	cmds.setParent( '..' )


	cmds.separator(style='single')

	cmds.floatSliderGrp('nSAngle', l='Smoothing Angle', field=True, v=45, min=0.5, max=179.5, cal=(1, 'right'), cw3=(100, 100, 200))
	

	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')
	cmds.button(label="Set Normal Smoothing Angle", command="setNormalAngle()", ann='Sets smoothing angle for object')


	

	cmds.text('                         ')
	cmds.text('                         ')
	cmds.text('                         ')
	

	cmds.button(label="Toggle Soft Edge Display", command="toggleSoftEdges()", ann='Toggle dashed lines for soft edges')


	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.rowColumnLayout(numberOfColumns=3)

	cmds.text('                         ')

	cmds.button(label="Harden Edge", command="cmds.polySoftEdge(a=0)")
	cmds.button(label="Soften Edge", command="cmds.polySoftEdge(a=180)")
	cmds.setParent( '..' )


	cmds.separator(style='single')

	cmds.rowColumnLayout(numberOfColumns=2)


	cmds.text('                         ')

	
	cmds.checkBox('lyt', label='Layout', value=True)
	cmds.text('                         ')


	cmds.checkBox('unf', label='Unfold', value=True)

	cmds.text('                         ')
	
	cmds.button(label="Unwrap by Smoothing Angle", command="unwrapByAngle()", ann="""Creates UV shells for the selected object based upon the object's edge normals.""")




	cmds.text('                         ')


	cmds.button(label="Unwrap by Selected Seams", command="unwrapBySeams()", ann="""Creates UV shells for the object using the selected edges as seams.""")


	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )


	#################
	## UV Editing  ##
	#################

	cmds.frameLayout( label='UV Editing', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')

	cmds.gridLayout( numberOfColumns=2, cellWidthHeight=(200, 25) )
	
	cmds.button(label="Unfold Vertical Pipe", command="unfoldPipe(2)", ann='Select the UVs of an unfolded pipe or cylindrical object\nthat run around the pipe (i.e.that are not touching the origin or insertion of the pipe)\nIf the width is only one face, select the entire shell\nUse this option for UVs that are tall')
	cmds.button(label="Unfold Horizontal Pipe", command="unfoldPipe(1)", ann='Select the UVs of an unfolded pipe or cylindrical object\nthat run around the pipe (i.e.that are not touching the origin or insertion of the pipe)\nIf the width is only one face, select the entire shell\nUse this option for UVs that are wide')
	cmds.button(label="Select Uvs Edge to Loop", command="selectUvEdgeLoop()", ann='Select an edge to convert selection to uv edge loop')
	cmds.button(label="Straighten Border", command="straightenUVBorder()", ann='Select a line of border UVs to straighten the UVS in between the furthest UVS')

	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )

	####################
	## UV Management  ##
	####################

	cmds.frameLayout( label='UV Management', borderStyle='out', cll=True, width=400)

	cmds.separator(style='none')
	
	cmds.radioButtonGrp('rot', label='Rotation', labelArray3=['None', '90 Deg', 'Free'], numberOfRadioButtons=3, select=3, cal=(1, 'right'), cw4=(80, 60, 60, 60))
	
	cmds.rowColumnLayout(numberOfColumns=2)

	cmds.text('                         ')
	cmds.button(label="Layout UVs", command="layoutUVs()")



	cmds.setParent( '..' )


	cmds.separator(style='single')

	cmds.rowColumnLayout(numberOfColumns=2)


	cmds.text('                         ')

	cmds.checkBox('cH', label='Clear Child History', value=False)

	cmds.text('                         ')
	cmds.button(label="Transfer UVs", command="transferUVs()", ann='Select the parent object to derive UVs from\nand then any children to copy the UVs to\nChildren will become UV instances of the parent unless Child History is cleared\nKeeping History tends to slow down performance')


	cmds.setParent( '..' )

	cmds.separator(style='none')

	cmds.setParent( '..' )

	cmds.setParent( '..' )
	
	cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Creation'), (child2, 'Modeling'), (child3, 'Unwrapping')) )


	cmds.showWindow(pToolsWindow)


##########################################################################################
######################################  Procedures  ######################################
##########################################################################################



def setNormalAngle():
	nSAngle = cmds.floatSliderGrp('nSAngle', q=True, v=True)
	cmds.polySoftEdge (a=str(nSAngle))

def makeHoleHelp():
        help ='In order to create a hole\n\nCreate a disk\nSnap the disk to the desired face\nScale the disk the desired hole size\nCombine the object and the disk\nUse the Make Hole Tool\nSelect the object face and then the disk\n\n'
        cmds.confirmDialog(title='Make Hole Help', button='OK', message=str(help));
        return
 
def creaseHardEdges():
	#crsAmt = 10
	crsAmt = cmds.floatSliderGrp ( 'crsAmt', q=True, value=True )
	cmds.selectType( pe=True ) # Selects Edges
	cmds.polySelectConstraint( m=3, t=0x8000, sm=1 ) # Constrains selection to hard edges
	cmds.polyCrease( value=crsAmt )
	cmds.polySelectConstraint( sm=0 ) # Turns off contraint

def unCrease():
	cmds.selectType ( pe=True ) # Selects Edges
	if (cmds.polyCrease ( q=True, value=True ) > 0 ): # Tests to see if there are creases
		cmds.polyCrease ( value=0.0 ) # Uncreases

def toggleSoftEdges():


	alreadySoft = cmds.polyOptions (q=True, allEdges=True) # Queries edge normals
	
	# Toggling edges
	if (alreadySoft[0] == True):
		cmds.polyOptions (softEdge=True) 
	else:
		cmds.polyOptions (allEdges=True)


def unwrapCylindrical():
	# Variables and selection
	mode = cmds.radioButtonGrp('mode', q=True, select=True)
	seam = cmds.ls( sl=True )

	cmds.SelectEdgeRingSp()
	cmds.ConvertSelectionToContainedFaces()

	body = cmds.ls ( sl=True )
	
	# Chooses desired seams
	numEdges = (len(seam))
	if (numEdges == 1):
		seamSel = (seam[0])
	else:
		seamSel = (seam[0:numEdges])

	bodySel = (body[0:(len(body))])
		
	# Unwraps with or without unfolding

	if (mode == 1):
		cmds.polyPlanarProjection ()
		cmds.select (seamSel, r=True)
		cmds.polyMapCut()
		cmds.unfold()

	elif (mode == 2):
		cmds.select (bodySel, r=True)
		cmds.ConvertSelectionToFaces()
		shell = cmds.ls( sl=True)
		cmds.polyForceUV (unitize=True)

		cmds.ConvertSelectionToContainedEdges()

		cmds.select (seamSel, d=True)
		cmds.polyMapSewMove()
		cmds.select(shell, r=True)
		cmds.ConvertSelectionToUVs()
		cmds.polyLayoutUV()
		cmds.select (shell, r=True)





def unwrapSelectedFaces():
	cmds.polyPlanarProjection()
	cmds.unfold()


def unwrapBySeams():

	# Variables and Selection
	unf= cmds.checkBox('unf', q=True, v=True)
	lyt = cmds.checkBox('lyt', q=True, v=True)
	selEdges= cmds.ls( sl=True )
	cmds.ConvertSelectionToShell()


	cmds.polyForceUV( unitize=True)
	cmds.ConvertSelectionToEdges()
	cmds.select(selEdges, d=True)
	cmds.polyMapSewMove()

	# Unfold if chosen
	if (unf==1):
		cmds.unfold()

	# Layout if chosen
	if (lyt == 1):
		cmds.select(selEdges)
		cmds.ConvertSelectionToShell()
		cmds.ConvertSelectionToUVs()
		cmds.polyLayoutUV( sc=1, ws=True, rbf=2 )

def unwrapByAngle():
	unf = cmds.checkBox('unf', q=True, v=True)
	lyt = cmds.checkBox('lyt', q=True, v=True)
	
	cmds.polyForceUV( unitize=True)
	cmds.selectType( pe=True )
	cmds.polySelectConstraint( m=3, t=0x8000, sm=2 ) # Constrains selection to soft edges
	selEdges= cmds.ls( sl=True )
	cmds.polyMapSewMove()
	cmds.polySelectConstraint( sm=0 ) # Turns off constraint

	# Unfold if chosen
	if (unf==1):
		cmds.unfold()

	# Layout if chosen
	if (lyt == 1):
		cmds.select(selEdges)
		cmds.ConvertSelectionToShell()
		cmds.ConvertSelectionToUVs()
		cmds.polyLayoutUV( sc=1, ws=True, rbf=2 )
	

def selectUvEdgeLoop():
	cmds.SelectEdgeLoopSp()
	cmds.ConvertSelectionToUVs()

def straightenUVBorder():
	cmds.polyStraightenUVBorder()
	cmds.unfold( oa=1, us=False)

def layoutUVs():
	# Variables and selection
	rot = cmds.radioButtonGrp('rot', q=True, sl=True)
	cmds.ConvertSelectionToShell()
	cmds.ConvertSelectionToUVs()
	# Choosing rotation mode
	if (rot==1):
		layoutSettings ='polyMultiLayoutUV -lm 1 -sc 1 -rbf 0 -fr 1 -ps 0.2 -l 2 -psc 2 -su 1 -sv 1 -ou 0 -ov 0;'
	elif (rot==2):
		layoutSettings ='polyMultiLayoutUV -lm 1 -sc 1 -rbf 1 -fr 1 -ps 0.2 -l 2 -psc 2 -su 1 -sv 1 -ou 0 -ov 0;'
	else:
		layoutSettings ='polyMultiLayoutUV -lm 1 -sc 1 -rbf 2 -fr 1 -ps 0.2 -l 2 -psc 2 -su 1 -sv 1 -ou 0 -ov 0;'
	maya.mel.eval(str(layoutSettings)) # Actual layout command
	
	

def unfoldPipe(dir):
	# Defining direction
	if (dir==1):
		first=1
		second=2
	elif (dir==2):
		first=2
		second=1
	cmds.unfold(oa=first, us=False)
	maya.mel.eval("polySelectBorderShell 0;") # Selecting UV Shell
	cmds.unfold(oa=second, us=False)

def transferUVs():
	cH = cmds.checkBox('cH', q=True, v=True)


	sel= cmds.ls( sl=True )
	for i in range (len(sel)):

		# Handling multiple objects
		if (len(sel)>2):
			cmds.select(sel[0], r=True)
			cmds.select(sel[i], add=True)
			cmds.transferAttributes( transferUVs=2, sampleSpace=5)
			
		elif (len(sel)==2):
			cmds.transferAttributes( transferUVs=2, sampleSpace=5)
			
		else:
			cmds.error ('Please select the source object first, and at least one target object.')

	# Deleting History if chosen
	if (cH==1):
		cmds.select(sel[1:len(sel)])
		cmds.DeleteHistory()

	cmds.select(sel, r=True)

def makeHolebyGeo():
	cmds.polyPoke()
	cmds.ConvertSelectionToVertices()
	cmds.ShrinkPolygonSelectionRegion()
	maya.mel.eval("polyChamferVtx 1 0.25 0;")

def makeDisk():
	numSides = cmds.intSliderGrp('numSides', q=True, v=True)


	cmds.polyCylinder(sx=numSides)
	sel = cmds.ls (sl=True)
	cmds.select (sel[0] +".f[" + str(numSides) + "]") # Selecting cap
	maya.mel.eval('GrowPolygonSelectionRegion;')
	cmds.delete() # Deleting all but one cap
	cmds.select (sel[0])
	cmds.xform (cp=True)
	cmds.move(rpr=True) # Moving Centered disk to origin
		
def autoQuad():
	cmds.polyTriangulate()
	cmds.polyQuad()

 
def movePivots():

	pivPos = cmds.radioButtonGrp('pivPos', q=True, sl=True)

	sel = cmds.ls (sl=True)

	# Testing for number of selected objects
	if (len(sel)<1):
		cmds.error ('No objects selected')
	elif (len(sel)==1):
		if (pivPos == 1):
				cmds.xform(cp=True) # Centering Pivot
		else:
			bBox = cmds.xform(q=True, ws=True, bb=True) # Querying bound box info
			centerPos = cmds.xform(q=True, ws=True, sp=True) #Querying transform info
			cmds.xform(piv=(centerPos[0], bBox[1], centerPos[2]), ws=True, ) # Adjusting pivot
	else:
		cmds.group(sel, n='pivotTempGrp', w=True) # Creating temporary group
		objCenter = cmds.objectCenter('pivotTempGrp')
		objBB = cmds.xform('pivotTempGrp', q=True, ws=True, bb=True) # Querying bound box info for group
		yAverage = ((objBB[1] + objBB[4])/2) # Calculating height
		for i in range(len(sel)):
			cmds.select(sel[i])
			if (pivPos == 1):
				cmds.xform(piv=(objCenter[0], objBB[1], objCenter[2]), ws=True)
			else:
				cmds.xform(piv=(objCenter[0], yAverage, objCenter[2]), ws=True)

		# Deleting temporary group
		cmds.ungroup ('pivotTempGrp')
		
	cmds.select(sel)

def setManip():

	manip = cmds.radioButtonGrp('manip', q=True, sl=True)

	# Setting to World Space
	if (manip == 1):
		cmds.manipMoveContext ('Move', e=True, mode=2)
		cmds.manipRotateContext ('Rotate', e=True, mode=1)
		cmds.manipScaleContext ('Scale', e=True, mode=2)

	# Setting to Object Space
	elif (manip == 2):
		cmds.manipMoveContext ('Move', e=True, mode=0)
		cmds.manipRotateContext ('Rotate', e=True, mode=0)
		cmds.manipScaleContext ('Scale', e=True, mode=0)

	maya.mel.eval('SelectToolOptionsMarkingMenu; MarkingMenuPopDown;') # Changing Tool to selection


def mirrorGeo():
	# Variables and selection
	mirrorMode = cmds.radioButtonGrp('mirrorMode', q=True, sl=True)
	mDir = cmds.radioButtonGrp('mDir', q=True, sl=True)
	sel =cmds.ls(sl=True)

	# Duplication type
	if (mirrorMode==1):
		cmds.duplicate()
	elif (mirrorMode==2):
		cmds.instance()
	else:
		newHalf = cmds.duplicate()

	# Scaling
	if (mDir==1):
		cmds.scale(-1, 1, 1)
	elif (mDir==2):
		cmds.scale(1, -1, 1)
	else:
		cmds.scale(1, 1, -1)

	# Merging Copy
	if (mirrorMode==3):
		cmds.select(sel[0], r=True)
		cmds.select(newHalf, add=True)
		cmds.polyUnite()
		cmds.ConvertSelectionToVertices()
		cmds.polyMergeVertex  (d=0.001, am=1, ch=1)
		cmds.select(sel[0])

	
# Run
phoenixTools()