''' Program to Find ConvexHull using Jarvis March method(with modification to handle collinear points)'''

import math #to use sqrt function
#a function to calculate Cosine angle between two vectors
#a,b and c are three points,with their vectors being <ab> and <bc>
def cosang(a,b,c):
    if ((a==b)or(b==c)or(a==c)):
        return -99
    v1x = float(b[0]-a[0])
    v1y = float(b[1]-a[1])
    v2x = float(c[0]-b[0])
    v2y = float(c[1]-b[1])
    
    modv1 = float(math.sqrt((v1x*v1x)+(v1y*v1y)))
    modv2 = float(math.sqrt((v2x*v2x)+(v2y*v2y)))
    return (float(((v1x*v2x)+(v1y*v2y))/(modv1*modv2)))
#function to get the point with highest cosine value
#since the the point with highest cosine value
#is the one with lowest angle
def getMaxCosangR(plist,hullPoints,p,q):
    minAngPoint = points[0]
    maxcos= cosang(p,q,minAngPoint)
    
    poss_col=[]
    for r in points[1:]:
        cosval = cosang(p,q,r)
        
        if cosval>maxcos:
            minAngPoint= r
            maxcos = cosval


        if cosval == maxcos:
            poss_col.append([r[0],r[1],cosval])

    i=0
    maxCosList =[]
    for y in poss_col:
        if maxcos==y[2]:
            maxCosList.append(y)
            i+=1
    
    maxcospoint  = [float(maxCosList[0][0]),float(maxCosList[0][1])]
    for x in maxCosList:
        
        hullPoints.append(x)
        if x[1]>maxcospoint[1]:
            maxcospoint=[float(x[0]),float(x[1])]
            
    if len(maxCosList)>1:
        print "appending" ,maxcospoint,"   out of", maxCosList
    

    return maxcospoint#the point r

####################################
####################################
###############MAIN#################
####################################
####################################
file1 = open('sample.txt','r')
i=0
points = []
#Points are extracted from the file
#stored as a List called points
while 1:
	str1=file1.readline().strip().split()
	#print str1
	if str1==[]:
		print "Hit"
		break
		
	#print str1[0]+"||"+str1[1]+">>"+`i`
	points.append([float(str1[0]),float(str1[1])])
	i+=1

file1.close()
#all the points have been extracted and from now on only the list points will be used
#Find the Leftmost Point
#add it to the hullPoints List
hullPoints = []
minPoint = points[0]
for x in points:
	if minPoint[0]>=x[0]:
		minPoint=x
hullPoints.append(minPoint)
print "Lefmost Point  = "+str(minPoint)
p_not =minPoint
p = [minPoint[0],0]
q = minPoint
minAngPoint = points[0]
maxcos= cosang(p,q,minAngPoint)
#print "maxCos"+`maxcos`
poss_col = []
#to find the next hull point using a reffrential vector y= p_not(x)
for r in points[1:]:
    cosval = cosang(p,q,r)
    
    if cosval>maxcos:
        minAngPoint= r
        maxcos = cosval
    if cosval == maxcos:
         poss_col.append([r[0],r[1],cosval])
i=0

maxCosList =[]
for y in poss_col:
    if maxcos==y[2]:
        maxCosList.append(y)
        i+=1


maxcospoint  = [float(maxCosList[0][0]),float(maxCosList[0][1])]
for x in maxCosList:
    
    hullPoints.append(x)
    if x[1]>maxcospoint[1]:
        maxcospoint=[float(x[0]),float(x[1])]
        
		
print p
print q
minAngPoint = maxcospoint
print minAngPoint

p = q
q = minAngPoint



while 1:
    
    r  = getMaxCosangR(points,hullPoints,p,q)
    if r == p_not:
        break
    else:
        p=q
        q=r
        
        print r

i = 0
file2 = open('Jarv_Classic.off','w')
file2.write("OFF\n")
k =0
file2.write(`len(hullPoints)`+" 1 0\n")
for x in hullPoints:
    
    print x
    i+=1
    file2.write(`x[0]`+" "+`x[1]`+" "+`float(0)`+"\n")
    k+=1
file2.write(`k`+" ")
j=k-1
while j>=0:
    
    file2.write(`j`+" ")
    j-=1
file2.close()
print "Final Total Hull Points = "+`i`
