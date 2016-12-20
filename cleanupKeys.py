import maya.cmds as mc

attributes= [
    'translateX',
    'translateY',
    'translateZ',
    'rotateX',
    'rotateY',
    'rotateZ',
    'scaleX',
    'scaleY',
    'scaleZ',
    'visibility']
    
def cleanupKeys(selection, aArray):
    for obj in selection:
        i = 0
        tArray = mc.keyframe(obj, query=True, attribute='translateX')
        for t in tArray:
            i+=1
            for a in aArray:
                if i >= len(tArray):
                    break
                checkAttr(obj,t,tArray[i],a)
            

def checkAttr(obj, t0, t1, attr):
    att0 = mc.getAttr(obj+'.'+attr, time=t0)
    att1 = mc.getAttr(obj+'.'+attr, time=t1)
    if (att0==att1):
        mc.cutKey(obj, time=(t0,t0), clear=True, option='keys', attribute=attr)

sel = mc.ls(selection=True)
tArr = mc.keyframe(sel, query=True, attribute='translateX')

# cleanupKeys(sel, attributes)

mc.window(width=150)
mc.columnLayout(adjustableColumn=True)
mc.button(label='Clean Up Keys of Selected',command="cleanupKeys(mc.ls(selection=True),mc.keyframe(sel, query=True, attribute='translateX'))")
mc.showWindow()