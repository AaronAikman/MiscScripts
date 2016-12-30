Phoenix Tools ReadMe
Aaron Aikman 
Copyright 2014 All Rights Reserved

The Phoenix Toolset offers a variety of functions concerning primitive creation, modeling, and unwrapping.
For more info, contact 
AaronAikman@aol.com 
or visit
www.Guerilla-Tactics.com



################################### Installation Options ###################################



A. Script placement  (Option 1)
	I.  Place the .py file in the scripts section of your Maya preferences folder.
		This folder can be found in the following locations depending upon your operating system.
Windows XP
 \Documents and Settings\<username>\My Documents\maya\2013\en_US\prefs 
Windows XP 64bit
 \Documents and Settings\<username>\My Documents\maya\2013-x64\en_US\prefs 
Windows Vista and Windows 7
 \Users\<username>\Documents\maya\2013\en_US\prefs 
Windows Vista and Windows 7 64bit
 \Users\<username>\Documents\maya\2013-x64\en_US\prefs 
Mac OS X
/Users/<username>/Library/Preferences/Autodesk/maya/2013/prefs
Linux 64-bit
~<username>/maya/2013-x64/prefs
	II.  Run the Script
		a.   Type the following lines of code into the command line one at a time (without indentation) and press enter (Make sure that command line displays the Python button next to it rather than the Mel button)
			import maya.cmds as cmds
			cmds.rehash()
			import phoenixTools_v1_0_25
		b.  To reload the script or create a shelf button for running the script, run the following line of code or middle mouse drag it into the shelf and select the Python option
			reload (phoenixTools_v1_0_25)
B.  Shelf Button Creation (Option 2)
	I. Copy the contents of the script to the command line
	II. Middle mouse drag it to the shelf and select the Python option
	III. Name the button and edit the annotation as needed (Optional)



###################################  Tool Reference  ########################################




	######################################  CREATION  ######################################


	################
	##  Polygons  ##
	################

	Cube - Creates a default cube
	2x2 Cube - Creates a cube with 2 subdivisions each direction
	4x4 Cube - Creates a cube with 4 subdivisions each direction
	Human Ref - Creates a cube 96 units high and 32 units each direction for referencing that average character size in UDK

	Sphere - Creates a default sphere
	Diode Sphere - Creates a sphere with 4 subdivision along the x axis and 3 subdivisions along the y axis
	12x12 Sphere - Creates a sphere with 12 subdivisions each way
	12x12 Sphere - Creates a sphere with 12 subdivisions each way

	Plane - Creates a default plane
	1x1 Plane - Creates a plane with no subdivisions
	4x4 Plane - Creates a plane with 4 subdivisions each direction
	Floor Plane - Creates a plane that is 1000 units each direction

	Cylinder - Creates a default cylinder
	Tri Cylinder - Creates a triangular cylinder with poked caps
	12 Cylinder - Creates a cylinder with 12 subdivisions along the x axis
	12x4 Cylinder - Creates a cylinder with 12 subdivisions along the x axis and 4 subdivisions along the y axis
	
	Torus - Creates a default torus
	Quad Torus - Creates a square-shaped torus with 4 subdivisions around it's width
	Disk - Creates a disk with 8 sides
	Prism - Creates a default prism

	Cone - Creates a default cone
	Helix - Creates a default helix
	Pipe - Creates a default pipe
	Pyramid - Creates a default pyramid

	#################
	##     Misc    ##
	#################


	Create Geometry Tool - Activates the tool
	CV Curve Tool - Activates the tool
	EP Curve Tool - Activates the tool
	Locator - Creates a default space locator



	######################################  MODELING  ######################################


	
	#################
	##  Mirroring  ##
	#################

	Mirror Object - Select object and place pivot point on symmetry line
	
	#############
	##  Pivots ##
	#############

	Move Pivots - Select one or more objects to adjust the pivot point of.  Tool creates a temporary group and will alter the hierarchy.

	############
	##  Manip ##
	############

	Set Manipulator - Sets all transformation manipulators to world space or object space

	##############
	##   Holes  ##
	##############

	In order to create a hole.
		Create a disk
		Snap the disk to the desired face
		Scale the disk the desired hole size
		Combine the object and the disk
		Use the Make Hole Tool
		Select the object face and then the disk
        

	Create Disk - Creates a disk at the origin point

	Snap Together Tool - Click the face on the first object to be snapped into location after clicking the face on the second object. Then press enter.
	
	Combine - Unites the objects

	Make Hole Tool - Select the face being cut into. Then select the face to become to hole. Then press enter. 

	Quadrangulate Geo - Select an N-gon to automatically quadrangular.


	Make Hole Based On Geo - Create a smaller face based upon the number of sides of the selected face


	##############
	## Creasing ##
	##############
	
	Toggle Soft Edge Display - Toggle dashed lines for soft edges

	Crease Hard Edges - Affects the way the model smooths in smooth preview mode and once subdivided

	Uncrease All - Uncreases the edges of the selected object

	
	######################################  UNWRAPPING  ######################################

	#################
	## UV Creation ##
	#################

	Unwrap Selected Faces - Unwraps the selected faces into contiguous shells

	Unwrap Cylindrical - Select a seam of the cylindrical object to unfold.  Unstretched mode will have no distortion, but will be less optimal for UV placement.  Optimized mode will unwrap into a shell where each face is a square.  An optimized pipe can then be unfolded using Unfold Pipe

	Set Normal Smoothing Angle - Sets smoothing angle for object

	Toggle Soft Edge Display - Toggle dashed lines for soft edges

	Harden Edge - Hardens the edge for mesh display
	
	Soften Edge - Softens the edge for mesh display

	Layout - Enables automatic layout after the unwrapping completes (Affects both unwrapping modes)

	Unfold - Enables automatic unfolding after the unwrapping completes (Affects both unwrapping modes)

	Unwrap by Smoothing Angle - Creates UV shells for the selected object based upon the object's edge normals

	Unwrap by Selected Seams", command="unwrapBySeams()", ann="""Creates UV shells for the object using the selected edges as seams.""")

	#################
	## UV Editing  ##
	#################

	Unfold Vertical Pipe - Select the UVs of an unfolded pipe or cylindrical object that run around the pipe (i.e.that are not touching the origin or insertion of the pipe). If the width is only one face, select the entire shell.  Use this option for UVs that tall.

	Unfold Horizontal Pipe - Select the UVs of an unfolded pipe or cylindrical object that run around the pipe (i.e.that are not touching the origin or insertion of the pipe). If the width is only one face, select the entire shell. Use this option for UVs that wide.
	
	Select Uvs Edge to Loop - Select an edge to convert selection to uv edge loop
	
	Straighten Border - Select a line of border UVs to straighten the UVS in between the furthest UVS

	####################
	## UV Management  ##
	####################

	Layout UVs - Lays out the UVs to have matching texel density and fit in the 0-1 space.  Rotation affects whether the shell are allowed to rotate during placement or not.

	Transfer UVs - Select the parent object to derive UVs from and then any children to copy the UVs to. Children will become UV instances of the parent unless Child History is cleared. Keeping History tends to slow down performance


PhoenixTools V10.02.1