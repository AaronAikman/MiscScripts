import maya.cmds as cmds
import maya.mel as mel

ctrlScaleMult = 1.5
sel = cmds.ls(sl=True)
rootName = 'joint'
cmds.select(cl=True)
cmds.joint(n=rootName)
for i in sel:
	cmds.select(i, r=True)
	loc = cmds.xform(q=True, piv=True)
	objBB = cmds.xform(q=True, bb=True)
	# xmin ymin zmin xmax ymax zmax.
	ctrlScale = ((abs(objBB[0]) + abs(objBB[3])) + (abs(objBB[1]) + abs(objBB[4])) / 2)
	ctrlScale *= ctrlScaleMult

	jntName = '{}_jnt'.format(i)
	cmds.joint(n=jntName)
	cmds.move(loc[0], loc[1], loc[2])
	cmds.skinCluster( jntName, i)
	cmds.parent(jntName, rootName)

	ctrlName = '{}_ctrl'.format(i)
	cmds.circle(n=ctrlName)
	cmds.move(loc[0], loc[1], loc[2])
	cmds.rotate( '90deg', 0, 0,)
	cmds.scale(ctrlScale, ctrlScale, ctrlScale)
	mel.eval('performFreezeTransformations(0)')

	cmds.parentConstraint(ctrlName, jntName, mo=True)
	cmds.scaleConstraint(ctrlName, jntName)
