#######################################
#######################################

#ASSIGNMENT_2_2
#NAME: Maho Kobayashi

#######################################
#######################################

#INSTRUCTIONS:
##All work should be done as 2D LINE WORK
##Format as LETTER SIZE (8.5" X 11") in LANDSCAPE
##Pay special attention to your LINE WIDTH
##Submit as a SINGLE PDF FILE, not neccessarily 1 pg
##First PNG/JPG in attachments will be cover image

##The assignment should involve the use of . . .
###Lists
###Iteration
###Conditional Execution

##############################

#DELIVERABLES:
##PDF
##code (saved in RTF = Rich Text Format)
##both(?)should be uploaded to the Gallery Site

#######################################
#######################################

#RHINOSCRIPT REFERENCES:
#https://developer.rhino3d.com/

##############################

#PYTHON REFERENCES:

##.append()**###############.sort()**
##.reverse()**##############.pop()**
##len()**

##.append()
###"To add an object to an already existing collections type,
###for instance. This is where the append method in Python
###shows its value. Append in Python is a pre-defined
###method used to add a single item to certain collection types"

###(https://www.simplilearn.com/ Google)

#REF: "bone structure: example 02" / 12:11 / rs.HideObject(ID)

#######################################
#######################################

#BRING IN LIBRARIES
import rhinoscriptsyntax as rs

##############################

#STEP_0: CREATE EMPTY LIST
ptList = []

#STEP_1: SET THE ATTRACTOR POINT
attrPt = rs.GetObject('select an attractor point',rs.filter.point)

#STEP_2: CREATE 2D POINT MATRIX
for i in range(20):
    for j in range(20):
        for k in range(3):
            #KEY
            ##define x in terms of i
            ##define y in terms of j
            x = i
            y = j
            z = k

            rs.AddPoint(x,y,z)
            #NOTES ABOUT 'rs.AddPoint()'
            ##rs.AddPoint(stop)
            ##rs.AddPoint(start,stop)
            ##rs.AddPoint(start,stop,step)

            #rs.AddTextDot((x,y,z),(x,y,z))
            #NOTES ABOUT 'rs.AddTextDot()
            ##if do not need the z, exclude z

            ptList.append((x,y,z))
            #print(ptList_0)
for i in range(len(ptList)):
    # print i, ':', ptList[i]
    #rs.AddTextDot(i, ptList[i])#<--- unhashtag to see labeled as index #
##NOTES: loop through point list and print out index number and values

##############################

#STEP 3: CREATING TRANSFORMATION OF GEOMETRY
#measure distance between attracor point and current point in the list
distance = rs.Distance(ptList[i], attrPt)
print distance/20
#create circle using distance value as radius
# rs.AddCylinder(ptList[i], distance/80,1/8)
# rs.AddSphere(ptList[i], distance/180)
# rs.AddCircle(ptList[i], distance/2)
rs.AddCylinder(ptList[i], distance/15,1/10)