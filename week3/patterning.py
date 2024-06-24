#######################################
#######################################

#NOTES: WEEK 3 ASSIGNMENT 1
#NAME: Maho Kobayashi

#######################################
#######################################

import rhinoscriptsyntax as rs
import random as rnd

#create an empty list / dictionary
ptDict = {}
crvList = []

#input values for imax and jmax
imax = rs.GetInteger('input number in x direction',10)
jmax = rs.GetInteger('input number in y direction',10)

#incremental loop to generate points
for i in range(imax):
    for j in range(jmax):
        #define x in terms of i
        #define y in terms of j
        x = i*6+(rnd.random()*3)
        y = j*6+(rnd.random()*3)
        z = 0

        #render point in rhinospace
        rs.AddPoint(x,y,z)

        #save point values in a dictionary using (i,j) as a key
        ptDict[(i,j)] = (x,y,z)

#loop through dictionary to create geometry
for i in range (imax):
    for j in range(jmax):

        #CREATE GEOMETRY
        if i > 0 and j > 0:
            #find centroid of module using midPt of constructed line
            constLine = rs.AddLine(ptDict[(i,j)],ptDict[(i-1,j-1)])
            centroid = rs.CurveMidPoint(constLine)
           
            #delete constructed line
            rs.DeleteObject(constLine)
           
            #POINTS
            #   2-------1 1: (i,j)
            #   | | 2: (i-1,j)
            #   | mid | 3: (i-1,j-1)
            #   | | 4: (i,j-1)
            #   3-------4
            
            #draw line from 1 to centroid to 2
            rs.AddCurve((ptDict[(i,j)], centroid, ptDict[(i-1,j)]))
            
            #draw line from 2 to centroid to 3
            rs.AddCurve((ptDict[(i-1,j)], centroid, ptDict[(i-1,j-1)]))
            
            #draw line from 1 to 4 to 3
            curve_0 = rs.AddCurve((ptDict[(i,j)], ptDict[(i,j-1)], ptDict[(i-1,j-1)]))
           
            #draw line from 1 to 2 to 3
            curve_0 = rs.AddCurve((ptDict[(i,j)], ptDict[(i-1,j)], ptDict[(i-1,j-1)]))
           
            #construct a closed curve from corner points
            curve = rs.AddCurve((ptDict[(i,j)], centroid, ptDict[(i-1,j-1)], ptDict[(i,j-1)], ptDict[(i,j)]))