#Return the count of records in the CallsforService feature class.
import arcpy

arcpy.env.workspace = r'C:\Users\jw\Desktop\610 python\Exercise 3.gdb'

print(arcpy.GetCount_management("CallsforService"))
