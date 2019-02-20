#Question 6
#Using the CallsforService feature class that you��ve been given, add a field called 
#Crime_Explanation�� with the data type Text/String. Then, if the value of field ��CFSType�� is 
#Burglary Call, write ��This is a burglary�� into the field that you just adde

import arcpy
from arcpy import env
env.overwriteOutput = True
arcpy.env.workspace = r'C:\Users\jw\Desktop\610 python\Exercise 3.gdb'
arcpy.AddField_management('CallsforService','Crime_Explanation','TEXT')

inTable = "CallsforService"
fieldName = "Crime_Explanation"
expression = "getype(str(!CFSType!))"
BurValue = "This is a burglary"

codeblock = """
def getype(type):
    if type ==  'Burglary Call':
        return BurValue

    """
 
 
# Execute CalculateField 
arcpy.CalculateField_management(inTable, fieldName, expression, "PYTHON3.5", 
                                codeblock)