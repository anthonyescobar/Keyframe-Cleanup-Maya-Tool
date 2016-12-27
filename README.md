# Keyframe-Cleanup-Maya-Tool
A python tool to delete extraneous keyframes from a selected object or objects in Maya. Extraneous keyframes are defined as non-changing attributes between keys.


![alt text][ui]
**_Fig 0:** Simple interface that calls the script by creating an array of objects containing the selected objects and creating an array of keyed frames based on one of the attributes.
``` python
mc.window(width=150)
mc.columnLayout(adjustableColumn=True)
mc.button(label='Clean Up Keys of Selected',command="cleanupKeys(mc.ls(selection=True),mc.keyframe(sel, query=True, attribute='translateX'))")
mc.showWindow()
```

```python
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
```


Key check and deletion are taken care of with the `checkAttr(obj,t0,t1,attr)` method which takes in an object `obj` and compares the passed in attribute `attr` at given time values `t0` and `t1`.

`cleanupKeys(selection, aArray)` is the main command that calls `checkAttr(obj,t0,t1,attr)` while iterating through the selection list and checking through the attributes in the list of provided attributes. This is done so the user can provide custom attributes to check by editing the attributes array.

![alt text][fig1]
**_Fig 1:** After selecting both objects we see the keyframes attributed to them._

![alt text][fig2]
**_Fig 2:** After running the script with the objects to clean selected we see that some keyframes are missing from the timeline and that the attributes of the pCube, which are listed on the right, are in light pink denoting that those keyframes are nonexistent._

![alt text][fig3]
**_Fig 3:** Selecting just the pCube we see that frame 1 is removed from the timeline as well because no attributes are keyframed._

![alt text][fig4]
**_Fig 4:** All keys attached to non-changing attributes are also deleted however the keyframe is noted on the timeline because at least one attribute is keyed._

[ui]: https://github.com/anthonyescobar/Keyframe-Cleanup-Maya-Tool/blob/master/DocPics/UI.PNG "interface to run script"
[fig1]: https://github.com/anthonyescobar/Keyframe-Cleanup-Maya-Tool/blob/master/DocPics/Maya2.PNG "Figure 1"
[fig2]: https://github.com/anthonyescobar/Keyframe-Cleanup-Maya-Tool/blob/master/DocPics/Maya3.PNG "Figure 2"
[fig3]: https://github.com/anthonyescobar/Keyframe-Cleanup-Maya-Tool/blob/master/DocPics/Maya4.PNG "Figure 3"
[fig4]: https://github.com/anthonyescobar/Keyframe-Cleanup-Maya-Tool/blob/master/DocPics/Maya5.PNG "Figure 4"
