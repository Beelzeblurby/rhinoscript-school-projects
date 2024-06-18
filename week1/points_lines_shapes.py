#######################################
#######################################

#ASSIGNMENT_1
#NAME: Maho Kobayashi

#######################################
#######################################

#INSTRUCTIONS:
##All work should be done as 2D LINE WORK
##Format as LETTER SIZE (8.5" X 11") in LANDSCAPE
##Pay special attention to your LINE WIDTH
##Submit as a SINGLE PDF FILE, not neccessarily 1 pg
##First PNG/JPG in attachments will be cover image

#DELIVERABLES:
##PDF
##code (saved in RTF = Rich Text Format)
##both(?)should be uploaded to the Gallery Site

#RHINOSCRIPT REFERENCES:
#https://developer.rhino3d.com/
##rs.GetObject()_IN#######rs.GetInteger()########rs.GetReal()
##rs.AddLine()_IN#########rs.AddPoint()_IN
##rs.PointCoordinates()###rs.RotateObject()_IN###rs.ScaleObject()_
###rs.MoveObject()_IN#####rs.CopyObject()_IN

#######################################
#######################################

#BRING IN LIBRARIES
import rhinoscriptsyntax as rs

##############################

#STEP_0: ADDING CENTER POINT (cntr_pt)
cntr_pt0 = rs.AddPoint(0,0,0)

#STEP_1: CREATING LINE (line_0)
startpt_0 = [0,0.25,0]
endpt_0 = [0,0.75,0.5]
line_0a = rs.AddLine(startpt_0, endpt_0)

#STEP_2: ROTATING AND COPYING LINE_0
##line_? = rs.RotateObject(the line, mid pt of the line, Copy_t/f)
line_1a = rs.RotateObject(line_0a,cntr_pt0,45,None,True)
line_2a = rs.RotateObject(line_0a,cntr_pt0,90,None,True)
line_3a = rs.RotateObject(line_0a,cntr_pt0,135,None,True)
line_4a = rs.RotateObject(line_0a,cntr_pt0,180,None,True)
line_5a = rs.RotateObject(line_0a,cntr_pt0,-45,None,True)
line_6a = rs.RotateObject(line_0a,cntr_pt0,-90,None,True)
line_7a = rs.RotateObject(line_0a,cntr_pt0,-135,None,True)

#STEP_3: SELECTING CURVE_0 TO ROTATE
curve_0a= rs.GetObject('select curve', rs.filter.curve)

#STEP_4: ROTATING AND COPYING CURVE_0
curve_1a = rs.RotateObject(curve_0a,cntr_pt0,45,None,True)
curve_2a = rs.RotateObject(curve_0a,cntr_pt0,90,None,True)
curve_3a = rs.RotateObject(curve_0a,cntr_pt0,135,None,True)
curve_4a = rs.RotateObject(curve_0a,cntr_pt0,180,None,True)
curve_5a = rs.RotateObject(curve_0a,cntr_pt0,-45,None,True)
curve_6a = rs.RotateObject(curve_0a,cntr_pt0,-90,None,True)
curve_7a = rs.RotateObject(curve_0a,cntr_pt0,-135,None,True)

#STEP_5: SCALE EVERYTHING FROM STEP 0 - 6
line_0a_2 = rs.ScaleObject(line_0a, cntr_pt0, (1.5,1.5,1.5), True)
line_1a_2 = rs.ScaleObject(line_1a, cntr_pt0, (1.5,1.5,1.5), True)
line_2a_2 = rs.ScaleObject(line_2a, cntr_pt0, (1.5,1.5,1.5), True)
line_3a_2 = rs.ScaleObject(line_3a, cntr_pt0, (1.5,1.5,1.5), True)
line_4a_2 = rs.ScaleObject(line_4a, cntr_pt0, (1.5,1.5,1.5), True)
line_5a_2 = rs.ScaleObject(line_5a, cntr_pt0, (1.5,1.5,1.5), True)
line_6a_2 = rs.ScaleObject(line_6a, cntr_pt0, (1.5,1.5,1.5), True)
line_7a_2 = rs.ScaleObject(line_7a, cntr_pt0, (1.5,1.5,1.5), True)
curve_0a_2 = rs.ScaleObject(curve_0a, cntr_pt0, (1.5,1.5,1.5), True)
curve_1a_2 = rs.ScaleObject(curve_1a, cntr_pt0, (1.5,1.5,1.5), True)
curve_2a_2 = rs.ScaleObject(curve_2a, cntr_pt0, (1.5,1.5,1.5), True)
curve_3a_2 = rs.ScaleObject(curve_3a, cntr_pt0, (1.5,1.5,1.5), True)
curve_4a_2 = rs.ScaleObject(curve_4a, cntr_pt0, (1.5,1.5,1.5), True)
curve_5a_2 = rs.ScaleObject(curve_5a, cntr_pt0, (1.5,1.5,1.5), True)
curve_6a_2 = rs.ScaleObject(curve_6a, cntr_pt0, (1.5,1.5,1.5), True)
curve_7a_2 = rs.ScaleObject(curve_7a, cntr_pt0, (1.5,1.5,1.5), True)

#STEP_6: ADDING ANOTHER CENTER POINT MOVED UP 0.5
cntr_pt1 = rs.AddPoint(0,0,0.5)

#STEP_7: OVER-WRITE POINT VARIABLES WITH VALUES
ptFrm_0 = rs.PointCoordinates(cntr_pt1)
ptTo_0 = rs.PointCoordinates(cntr_pt0)


#STEP_8: MOVING EVERYTHING IN STEP 1- 4 UP 0.5

translation = ptFrm_0 - ptTo_0
#this calculate how much to move everything and in what direction

line_0a = rs.MoveObject(line_0a, translation)
line_1a = rs.MoveObject(line_1a, translation)
line_2a = rs.MoveObject(line_2a, translation)
line_3a = rs.MoveObject(line_3a, translation)
line_4a = rs.MoveObject(line_4a, translation)
line_5a = rs.MoveObject(line_5a, translation)
line_6a = rs.MoveObject(line_6a, translation)
line_7a = rs.MoveObject(line_7a, translation)

curve_0a = rs.MoveObject(curve_0a, translation)
curve_1a = rs.MoveObject(curve_1a, translation)
curve_2a = rs.MoveObject(curve_2a, translation)
curve_3a = rs.MoveObject(curve_3a, translation)
curve_4a = rs.MoveObject(curve_4a, translation)
curve_5a = rs.MoveObject(curve_5a, translation)
curve_6a = rs.MoveObject(curve_6a, translation)
curve_7a = rs.MoveObject(curve_7a, translation)


#STEP_9: ROTATING EVERYTHING IN STEP 8

line_0a = rs.RotateObject(line_0a,cntr_pt0,22.5,None,False)
line_1a = rs.RotateObject(line_1a,cntr_pt0,22.5,None,False)
line_2a = rs.RotateObject(line_2a,cntr_pt0,22.5,None,False)
line_3a = rs.RotateObject(line_3a,cntr_pt0,22.5,None,False)
line_4a = rs.RotateObject(line_4a,cntr_pt0,22.5,None,False)
line_5a = rs.RotateObject(line_5a,cntr_pt0,22.5,None,False)
line_6a = rs.RotateObject(line_6a,cntr_pt0,22.5,None,False)
line_7a = rs.RotateObject(line_7a,cntr_pt0,22.5,None,False)

curve_0a = rs.RotateObject(curve_0a,cntr_pt0,22.5,None,False)

curve_1a = rs.RotateObject(curve_1a,cntr_pt0,22.5,None,False)

curve_2a = rs.RotateObject(curve_2a,cntr_pt0,22.5,None,False)

curve_3a = rs.RotateObject(curve_3a,cntr_pt0,22.5,None,False)

curve_4a = rs.RotateObject(curve_4a,cntr_pt0,22.5,None,False)

curve_5a = rs.RotateObject(curve_5a,cntr_pt0,22.5,None,False)

curve_6a = rs.RotateObject(curve_6a,cntr_pt0,22.5,None,False)

curve_7a = rs.RotateObject(curve_7a,cntr_pt0,22.5,None,False)


#STEP_10: SELECTING CIRCLE_0 TO COPY AND ROTATE
circle_0 = rs.GetObject('select circle', rs.filter.curve)

circle_1 = rs.CopyObject(circle_0)
circle_1 = rs.RotateObject(circle_1,cntr_pt1,11.25,None,False)

circle_2 = rs.CopyObject(circle_1)
circle_2 = rs.RotateObject(circle_2,cntr_pt1,11.25,None,False)

circle_3 = rs.CopyObject(circle_2)
circle_3 = rs.RotateObject(circle_3,cntr_pt1,11.25,None,False)

circle_4 = rs.CopyObject(circle_3)
circle_4 = rs.RotateObject(circle_4,cntr_pt1,11.25,None,False)

circle_5 = rs.CopyObject(circle_4)
circle_5 = rs.RotateObject(circle_5,cntr_pt1,11.25,None,False)

circle_6 = rs.CopyObject(circle_5)
circle_6 = rs.RotateObject(circle_6,cntr_pt1,11.25,None,False)

circle_7 = rs.CopyObject(circle_6)
circle_7 = rs.RotateObject(circle_7,cntr_pt1,11.25,None,False)

circle_8 = rs.CopyObject(circle_7)
circle_8 = rs.RotateObject(circle_8,cntr_pt1,11.25,None,False)

circle_9 = rs.CopyObject(circle_8)
circle_9 = rs.RotateObject(circle_9,cntr_pt1,11.25,None,False)

circle_10 = rs.CopyObject(circle_9)
circle_10 = rs.RotateObject(circle_10,cntr_pt1,11.25,None,False)

circle_11 = rs.CopyObject(circle_10)
circle_11 = rs.RotateObject(circle_11,cntr_pt1,11.25,None,False)

circle_12 = rs.CopyObject(circle_11)
circle_12 = rs.RotateObject(circle_12,cntr_pt1,11.25,None,False)

circle_13 = rs.CopyObject(circle_12)
circle_13 = rs.RotateObject(circle_13,cntr_pt1,11.25,None,False)

circle_14 = rs.CopyObject(circle_13)
circle_14 = rs.RotateObject(circle_14,cntr_pt1,11.25,None,False)

circle_15 = rs.CopyObject(circle_14)
circle_15 = rs.RotateObject(circle_14,cntr_pt1,11.25,None,False)

#######################################
#######################################