# Aaron Aikman Copyright 2014
# PhoenixTools



import maya.cmds as cmds


#Defining the Window
def phoenixTools():
	pToolsWindow = cmds.window(menuBar=True, title="Golden Triangle Creator")
	
	cmds.menu( label='Stuff' )
	cmds.menuItem( subMenu=True, label='Colors' )
	cmds.menuItem( label='Blue' )
	cmds.menuItem( label='Green' )
	cmds.menuItem( label='Yellow' )
	cmds.setParent( '..', menu=True )
	cmds.menuItem( divider=True )
	cmds.radioMenuItemCollection()
	cmds.menuItem( label='Yes', radioButton=False )
	cmds.menuItem( label='Maybe', radioButton=False )
	cmds.menuItem( label='No', radioButton=True )
	cmds.menuItem( divider=True )
	cmds.menuItem( label='Top', checkBox=True )
	cmds.menuItem( label='Middle', checkBox=False )
	cmds.menuItem( label='Bottom', checkBox=True )
	cmds.menuItem( divider=True )
	cmds.menuItem( label='Option' )
	cmds.menuItem( optionBox=True )
	
	cmds.menu( label='Things' )
	cmds.menuItem( subMenu=True, label='Colors' )
	cmds.menuItem( label='Blue' )
	cmds.menuItem( label='Green' )
	cmds.menuItem( label='Yellow' )
	cmds.setParent( '..', menu=True )
	cmds.menuItem( divider=True )
	cmds.radioMenuItemCollection()
	cmds.menuItem( label='Yes', radioButton=False )
	cmds.menuItem( label='Maybe', radioButton=False )
	cmds.menuItem( label='No', radioButton=True )
	cmds.menuItem( divider=True )
	cmds.menuItem( label='Top', checkBox=True )
	cmds.menuItem( label='Middle', checkBox=False )
	cmds.menuItem( label='Bottom', checkBox=True )
	cmds.menuItem( divider=True )
	cmds.menuItem( label='Option' )
	cmds.menuItem( optionBox=True )
	
	form = cmds.formLayout()
	tabs = cmds.tabLayout()
	#tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
	cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )

	child1 = cmds.scrollLayout( 'scrollLayout' )

	cmds.frameLayout( label='Buttons', borderStyle='out', cll=True )
	
	cmds.button()
	cmds.button()
	cmds.button()
	cmds.text(label="Number of Curls")
	cmds.intSliderGrp("curls", field=True, v=1, min=0.01, max=100, fmx=10000)

	cmds.text(label="Size")
	cmds.floatSliderGrp("size", field=True, v=1, min=0.01, max=100, fmx=10000)

	cmds.button(label="Create Golden Triangle", command="doGoldenTriangle()")
	cmds.setParent( '..' )
	cmds.setParent( '..' )

	child2 = cmds.scrollLayout( 'scrollLayout2' )
	cmds.frameLayout( label='Buttons', borderStyle='out', cll=True )
	cmds.text(label="Size")
	cmds.floatSliderGrp("size", field=True, v=1, min=0.01, max=100, fmx=10000)
	cmds.button(label="Unwrap by Smoothing Angle", command="unwrapByAngle()")
	cmds.setParent( '..' )
	cmds.setParent( '..' )

	cmds.tabLayout( tabs, edit=True, tabLabel=((child1, 'Modeling'), (child2, 'Unwrapping')) )
	cmds.showWindow(pToolsWindow)

 

def unwrapByAngle():
	#cmds.selectType( fc=True )
	cmds.polyForceUV( unitize=True)
	cmds.selectType( pe=True )
	#cmds.polySelectConstraint( m=3, t=0x8000, sm=1 ) # to get hard edges
	cmds.polySelectConstraint( m=3, t=0x8000, sm=2 ) # to get soft edges
	cmds.polyMapSew()
	cmds.polySelectConstraint( sm=0 ) # turn off edge smoothness constraint
	cmds.unfold()
	cmds.polyLayoutUV( sc=1, ws=True, rbf=2 )
	
def straightenUVBorder():
	cmds.polyStraightenUVBorder()
	cmds.unfold( oa=1, us=False)
	
def straightenUVs():
	cmds.polyStraightenUVBorder()
	cmds.unfold( oa=1, us=False)
	
	

 
def do():

	#Defining Variables
	numCurls = cmds.intSliderGrp("curls", query=True, value=True)
	size = cmds.floatSliderGrp("size", query=True, value=True)

	longSize = 3*size
	
	#Creating Initial Curve
	theCurve = cmds.curve(d=1, p=[(0, 0, 0), (-size, 0, longSize), (size, 0, longSize)])
	
	#Duplicating the Curve
	cmds.duplicate(theCurve)
	cmds.move (size, 0, longSize, rpr=True)
	cmds.rotate (0, 216.721501, 0, r=True, ws=True)
	cmds.scale (0.362375, 0.362375, 0.362375, r=True)

	
	for i in range(numCurls):
		cmds.duplicate (st=True)
	
	#Attaching the Curves and Deleting the Old Curves
	cmds.select(cmds.ls(type='nurbsCurve'))
	newSet1 = cmds.sets()
	cmds.attachCurve (rpo=False, ch=False, n='GoldenTriangle_MO',)
	cmds.select( newSet1, r=True)
	cmds.ls( selection=True )
	cmds.delete()
	
	#Creating the Spiral
	cmds.select('GoldenTriangle_MO')
	cmds.rebuildCurve (kcp=True, rpo=False, n='GoldenTriangleSpiral_MO')
	
#Run
phoenixTools()