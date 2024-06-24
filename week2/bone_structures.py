#######################################
#######################################

#ASSIGNMENT_2
#NAME: Maho Kobayashi

#######################################
#######################################

#INSTRUCTIONS:
##All work should be done as 2D LINE WORK
##Format as LETTER SIZE (8.5" X 11") in LANDSCAPE
##Pay special attention to your LINE WIDTH
##Submit as a SINGLE PDF FILE, not neccessarily 1 pg
##First PNG/JPG in attachments will be cover image

##############################

#DELIVERABLES:
##PDF
##code (saved in RTF = Rich Text Format)
##both(?)should be uploaded to the Gallery Site

#######################################
#######################################

#RHINOSCRIPT REFERENCES:
#https://developer.rhino3d.com/

#KEY
##** = added functions denoted in bold and asterisks
##_IN = means it was included in the code

##Input:
##rs.GetObject()############rs.GetInteger()
##rs,GetReal()##############rs.GetObjects()**

##Create/Analyze:
##rs.AddLine()_IN###########rs.AddPoint()
##rs.PointCoordinates()#####rs.AddCircle()_IN**
##rs.AddCurve()_IN**

##Line/Curve:
##rs.CurveStartPoint()######rs.CurveMidPoint()
##rs.CurveEndPoint()########rs.DivideCurve()_IN**
##rs.CurveAreaCentroid()####rs.CurveEditPoints()**

##Transform:
##rs.RotateObject()#########rs.ScaleObject()
##rs.MoveObject()###########rs.CopyObject()
##rs.CopyObjects()##########rs.MoveObjects()**

##############################

#PYTHON REFERENCES:

##.append()**###############.sort()**
##.reverse()**##############.pop()**
##len()**

#REF: "bone structure: example 02" / 12:11 / rs.HideObject(ID)

#######################################
#######################################

#BRING IN LIBRARIES
import rhinoscriptsyntax as rs

##############################

#STEP_0: ADDING CENTER LINE
startpt_0 = [0,0,0]
endpt_0 = [0,0,6]
line_0 = rs.AddLine(startpt_0, endpt_0)

#STEP_1: DIVIDING LINE_0 INTO 7/ADD POINTS ON LINE
pts_line_0 = rs.DivideCurve(line_0,5,False,True)

#STEP_2: LABEL POINTS FROM STEP_1
#rs.AddTextDot('0L', pts_line_0[0])
#rs.AddTextDot('1L', pts_line_0[1])
#rs.AddTextDot('2L', pts_line_0[2])
#rs.AddTextDot('3L', pts_line_0[3])
#rs.AddTextDot('4L', pts_line_0[4])

##############################

#STEP_3: ADD BIGGER CIRCLES ON POINTS
circle_0 = rs.AddCircle(pts_line_0[0],0.5)
circle_1 = rs.AddCircle(pts_line_0[1],1)
circle_2 = rs.AddCircle(pts_line_0[2],2)
circle_3 = rs.AddCircle(pts_line_0[3],1)
circle_4 = rs.AddCircle(pts_line_0[4],0.5)

#STEP_4: DIVIDE CIRCLES/ ADD POINTS
pts_circle_0 = rs.DivideCurve(circle_0,7,False,True)
pts_circle_1 = rs.DivideCurve(circle_1,7,False,True)
pts_circle_2 = rs.DivideCurve(circle_2,7,False,True)
pts_circle_3 = rs.DivideCurve(circle_3,7,False,True)
pts_circle_4 = rs.DivideCurve(circle_4,7,False,True)

#STEP_5: LABEL POINTS FROM STEP_1
#NOTE: Since I know they order for the numbers of each circle are the same
#######I can just keep the numbers for one of the circles
#######and just "#" or delete the rest out

#BIG C 3
#rs.AddTextDot('0', pts_circle_3[0])
#rs.AddTextDot('1', pts_circle_3[1])
#rs.AddTextDot('2', pts_circle_3[2])
#rs.AddTextDot('3', pts_circle_3[3])
#rs.AddTextDot('4', pts_circle_3[4])
#rs.AddTextDot('5', pts_circle_3[5])
#rs.AddTextDot('6', pts_circle_3[6])

##############################

#STEP_6: ADD SMALLER CIRCLES ON POINTS FROM STEP_
circle_0s = rs.AddCircle(pts_line_0[0],0.25)
circle_1s = rs.AddCircle(pts_line_0[1],0.5)
circle_2s = rs.AddCircle(pts_line_0[2],1)
circle_3s = rs.AddCircle(pts_line_0[3],0.5)
circle_4s = rs.AddCircle(pts_line_0[4],0.25)

#STEP_7: DIVIDE CIRCLES/ ADD POINTS
pts_circle_0s = rs.DivideCurve(circle_0s,14,False,True)
pts_circle_1s = rs.DivideCurve(circle_1s,14,False,True)
pts_circle_2s = rs.DivideCurve(circle_2s,14,False,True)
pts_circle_3s = rs.DivideCurve(circle_3s,14,False,True)
pts_circle_4s = rs.DivideCurve(circle_4s,14,False,True)

#STEP_9: LABEL POINTS FROM STEP_1
#NOTE: Since I know they order for the numbers of each circle are the same
#######I can just keep the numbers for one of the circles
#######and just "#" or delete the rest out

#SMALL C 3
#rs.AddTextDot('0s', pts_circle_3s[0])
#rs.AddTextDot('1s', pts_circle_3s[1])
#rs.AddTextDot('2s', pts_circle_3s[2])
#rs.AddTextDot('3s', pts_circle_3s[3])
#rs.AddTextDot('4s', pts_circle_3s[4])
#rs.AddTextDot('5s', pts_circle_3s[5])
#rs.AddTextDot('6s', pts_circle_3s[6])
#rs.AddTextDot('7s', pts_circle_3s[7])
#rs.AddTextDot('8s', pts_circle_3s[8])
#rs.AddTextDot('9s', pts_circle_3s[9])
#rs.AddTextDot('10s', pts_circle_3s[10])
#rs.AddTextDot('11s', pts_circle_3s[11])
#rs.AddTextDot('12s', pts_circle_3s[12])
#rs.AddTextDot('13s', pts_circle_3s[13])

##############################

#STEP_10: CREATE NEW SHAPES WITHIN THE CIRCLES USING POINTS FROM STEP_4
#REF: "bone structure: example 03" / 6:22 / "rs.AddCurve"
# ex: rs.AddCurve(ptGUID, pts[0], pts[1], ptGUID)
#NOTE: changed to tuples[] instead of list()

star_0 = rs.AddCurve([pts_circle_0[0], pts_line_0[1], pts_circle_0s[1
], pts_line_0[1], pts_circle_0[1], pts_line_0[1], pts_circle_0s[3],
pts_line_0[1], pts_circle_0[2], pts_line_0[1],pts_circle_0s[5], pts_line_0
[1], pts_circle_0[3], pts_line_0[1], pts_circle_0s[7], pts_line_0[1],
pts_circle_0[4], pts_line_0[1], pts_circle_0s[9], pts_line_0[1], pts_circle_0
[5], pts_line_0[1], pts_circle_0s[11], pts_line_0[1], pts_circle_0[6]
, pts_line_0[1], pts_circle_0s[13], pts_line_0[1], pts_circle_0[0]],3
)
#NOTES: to prevent errors, wrote it broken up into smaller bits first
#(pts_circle_0[0], pts_line_0[1], pts_circle_0s[1],
###
# pts_line_0[1], pts_circle_0[1],
# pts_line_0[1], pts_circle_0s[3],
###
# pts_line_0[1], pts_circle_0[2],
# pts_line_0[1],pts_circle_0s[5],
###
# pts_line_0[1], pts_circle_0[3],
# pts_line_0[1], pts_circle_0s[7],
###
# pts_line_0[1], pts_circle_0[4],
# pts_line_0[1], pts_circle_0s[9],
###
# pts_line_0[1], pts_circle_0[5],
# pts_line_0[1], pts_circle_0s[11],
###
# pts_line_0[1], pts_circle_0[6],
# pts_line_0[1], pts_circle_0s[13],
###
# pts_line_0[1], pts_circle_0[0],

star_1 = rs.AddCurve([pts_circle_1[0], pts_line_0[2], pts_circle_1s[1
], pts_line_0[2], pts_circle_1[1], pts_line_0[2], pts_circle_1s[3],
pts_line_0[2], pts_circle_1[2], pts_line_0[2],pts_circle_1s[5], pts_line_0
[2], pts_circle_1[3], pts_line_0[2], pts_circle_1s[7], pts_line_0[2],
pts_circle_1[4], pts_line_0[2], pts_circle_1s[9], pts_line_0[2], pts_circle_1
[5], pts_line_0[2], pts_circle_1s[11], pts_line_0[2], pts_circle_1[6]
, pts_line_0[2], pts_circle_1s[13], pts_line_0[2], pts_circle_1[0]],3)
star_2 = rs.AddCurve([pts_circle_2[0], pts_line_0[3], pts_circle_2s[1
], pts_line_0[3], pts_circle_2[1], pts_line_0[3], pts_circle_2s[3],
pts_line_0[3], pts_circle_2[2], pts_line_0[3],pts_circle_2s[5], pts_line_0
[3], pts_circle_2[3], pts_line_0[3], pts_circle_2s[7], pts_line_0[3],
pts_circle_2[4], pts_line_0[3], pts_circle_2s[9], pts_line_0[3], pts_circle_2
[5], pts_line_0[3], pts_circle_2s[11], pts_line_0[3], pts_circle_2[6]
, pts_line_0[3], pts_circle_2s[13], pts_line_0[3], pts_circle_2[0]],3
)
star_3 = rs.AddCurve([pts_circle_3[0], pts_line_0[4], pts_circle_3s[1
], pts_line_0[4], pts_circle_3[1], pts_line_0[4], pts_circle_3s[3],
pts_line_0[4], pts_circle_3[2], pts_line_0[4],pts_circle_3s[5], pts_line_0
[4], pts_circle_3[3], pts_line_0[4], pts_circle_3s[7], pts_line_0[4],
pts_circle_3[4], pts_line_0[4], pts_circle_3s[9], pts_line_0[4], pts_circle_3
[5], pts_line_0[4], pts_circle_3s[11], pts_line_0[4], pts_circle_3[6]
, pts_line_0[4], pts_circle_3s[13], pts_line_0[4], pts_circle_3[0]],3
)
star_4 = rs.AddCurve([pts_circle_4[0], pts_line_0[5], pts_circle_4s[1
], pts_line_0[5], pts_circle_4[1], pts_line_0[5], pts_circle_4s[3],
pts_line_0[5], pts_circle_4[2], pts_line_0[5],pts_circle_4s[5], pts_line_0
[5], pts_circle_4[3], pts_line_0[5], pts_circle_4s[7], pts_line_0[5],
pts_circle_4[4], pts_line_0[5], pts_circle_4s[9], pts_line_0[5], pts_circle_4
[5], pts_line_0[5], pts_circle_4s[11], pts_line_0[5], pts_circle_4[6]
, pts_line_0[5], pts_circle_4s[13], pts_line_0[5], pts_circle_4[0]],3)

##############################

#STEP_11: HIDING CIRCLE_0 - CIRCLE_4
rs.HideObject(circle_0)
rs.HideObject(circle_1)
rs.HideObject(circle_2)
rs.HideObject(circle_3)
rs.HideObject(circle_4)

#STEP_12: HIDING CIRCLE_0s - CIRCLE_4s
rs.HideObject(circle_0s)
rs.HideObject(circle_1s)
rs.HideObject(circle_2s)
rs.HideObject(circle_3s)
rs.HideObject(circle_4s)

#STEP_13: HIDING LINE_0
rs.HideObject(line_0)

#######################################
#######################################