import math 
def minmax(cd,nodeval,maxt,scr,td):
    if(cd==td):
        return scr[nodeval]
    if(maxt):
        return max(minmax(cd+1,nodeval*2,False,scr,td),minmax(cd+1,nodeval*2+1,False,scr,td))
    else:
        return min(minmax(cd+1,nodeval*2,True,scr,td),minmax(cd+1,nodeval*2+1,True,scr,td))

scr=[-1,8,-3,-1,2,1,-3,4]
td=math.log(len(scr),2)
cd=0
nodeval=0
maxt=True
answer= minmax(cd,nodeval,maxt,scr,td)
print(" The Solution is : ", answer)
