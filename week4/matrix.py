#######################################
#######################################

#NOTES: WEEK 4 ASSIGNMENT 1
#NAME: Maho Kobayashi

#######################################
#######################################

import rhinoscriptsyntax as rs
import random as rnd
import Rhino.Geometry as rg
import scriptcontext as sc

#######################################
#3D POINT MATRIX
#import modules
import rhinoscriptsyntax as rs

def PointMatrix(IMAX,JMAX,KMAX):

    #set up empty list
    ptList_0 = []
    ptList_1 = []
    ptList_2 = []
    ptList_3 = []
    ptList_4 = []
    ptList_5 = []
    ptDict_0 = {}
    ptDict_1 = {}
    ptDict_2 = {}
    ptDict_3 = {}
    ptDict_4 = {}
    ptDict_5 = {}
    circDict_0 = []
    circDict_1 = []
    circDict_2 = []
    circDict_3 = []
    circDict_4 = []
    circDict_5 = []

    #loop to generate point values as a product of the loop counter
    #save values in list
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                #define x,y,z in terms of i,j,k
                x = i /.5+40
                y = j /.5+45
                z = k

                #SAVING POINTS TO DICTIONARY_0
                point_0 = (x,y,z)
                ptDict_0[(i,j,k)] = point_0
                #dict = key value pair
               
                #DICTIONARY_1
                point_1 = (x,y,0.5)
                ptDict_1[(i,j,k)] = point_1
                
                #DICTIONARY_2
                point_2 = (x,y,1)
                ptDict_2[(i,j,k)] = point_2
                
                #DICTIONARY_3
                point_3 = (x,y,1.5)
                ptDict_3[(i,j,k)] = point_3
                
                #DICTIONARY_4
                point_4 = (x,y,2)
                ptDict_4[(i,j,k)] = point_4
               
                #DICTIONARY_5
                point_5 = (x,y,2+rnd.random())
                ptDict_5[(i,j,k)] = point_5
                
                #print out dictionary key:value pairs
                #print (i,j,k), ':', point_0
               
                #render point in rhinospace
                rs.AddPoint(point_0)
                rs.AddPoint(point_1)
                rs.AddPoint(point_2)
                rs.AddPoint(point_3)
                rs.AddPoint(point_4)
                rs.AddPoint(point_5)
               
                #save points in a list
                ptList_0.append(point_0)
                ptList_1.append(point_1)
                ptList_2.append(point_2)
                ptList_3.append(point_3)
                ptList_4.append(point_4)
                ptList_5.append(point_5)

#######################################
#######################################

#REFERENCES

#https://developer.rhino3d.com/api/rhinoscript/math_methods/rnd.htm
#https://discourse.mcneel.com/t/how-to-loft-circle-through-rhinocommon/53850/2

    #loop through dictionary to label points with (i,j,k) keys
    #for i in range(IMAX):
        #for j in range(JMAX):
            #for k in range(KMAX):
                #rs.AddTextDot((i,j,k), ptDict[(i,j,k)])
#######################################
    #Loop through dictionaries to create cirlces with randomized     circumfrence
    for i in range(IMAX):
        for j in range(JMAX):
            for k in range(KMAX):
                circDict_0 = rs.AddCircle(ptDict_0[(i,j,k)],rnd.random())
                circDict_1 = rs.AddCircle(ptDict_1[(i,j,k)],rnd.random())
                circDict_2 = rs.AddCircle(ptDict_2[(i,j,k)],rnd.random())
                circDict_3 = rs.AddCircle(ptDict_3[(i,j,k)],rnd.random())
                circDict_4 = rs.AddCircle(ptDict_4[(i,j,k)],rnd.random())
                circDict_5 = rs.AddCircle(ptDict_5[(i,j,k)],rnd.random())
                
                #Loop through dictionaries to loft the circles
                circle_1 = rs.coercecurve(circDict_0)
                circle_2 = rs.coercecurve(circDict_1)
                circle_3 = rs.coercecurve(circDict_2)
                circle_4 = rs.coercecurve(circDict_3)
                circle_5 = rs.coercecurve(circDict_4)
                circle_6 = rs.coercecurve(circDict_5)
                no_pt=rg.Point3d.Unset
                norm_loft=rg.LoftType.Normal

                breps = rg.Brep.CreateFromLoft([circle_1,
                circle_2,circle_3,circle_4,circle_5,circle_6],no_pt,no_pt,norm_loft,False) #False
                new_IDs=[sc.doc.Objects.AddBrep(brep) for
                brep in breps]
                
                sc.doc.Views.Redraw()
            
                #Loop through to color
                rs.ObjectColor(new_IDs, (255/IMAX*i, 255-(255/JMAX)*j,255/KMAX*k))

#######################################

def main():
    #get values from user
    imax = rs.GetInteger('maximum number x', 4)
    jmax = rs.GetInteger('maximum number y', 4)
    kmax = rs.GetInteger('maximum number z', 1)

    #call function
    PointMatrix(imax,jmax,kmax)
    
#call main() function to start program
main()