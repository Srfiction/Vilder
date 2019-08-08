chainJoint(cantidad=8, nombre='test', lado='s', chin=True, radio=1, inicio='joint1', fin='joint2', unparent=True)

nurbs = makeRibbon(point1='joint1', point2='joint2', width=10, module='koko', side='s', u=1, v=7)[0]

attachBones(nurb = nurbs, side='side', system='spine')

import vilder as wtf
import AutoRig.Functions_Autorig


class refAutorig:
    def __init__(self, module, side): 
        self.name = '{}_{}_vilder'.format(module, side)
    def boneCircle(self, number):
        name = self.name
        jnt = cmds.joint(n='position{}{}'.format(number, name.capitalize()))
        cir = cmds.circle(n='circle{}{}'.format(number, name.capitalize()))   
        cmds.parentConstraint(cir, jnt, n='parent{}'.format(number, name.capitalize()))
        return jnt
    def referenceChain(self, mod, sid, quantity):
        ref = refAutorig(module=mod, side=sid)
        jnt_list=[]
        for num in range(quantity):
            cmds.select(cl=True)
            jnt = ref.boneCircle(number=num)
            if num == 0:
                jnt_list.append(jnt)
            else:
                cmds.parent(jnt, jnt_list[num-1])  
                jnt_list.append(jnt)  
            
         
ref = refAutorig('spine', 'r')
ref.referenceChain(mod='spine', sid='l', quantity=2)
    