#Write Python code that selects a subset of the records from a given feature class and writes 
#those features to a different feature class. You may choose which feature class that your code 
#uses.
import arcpy
from arcpy import env
env.overwriteOutput = True

arcpy.env.workspace = r'C:\Users\jw\Desktop\610 python\Exercise 3.gdb'
 
# Set local variables
inFeatures = "CallsforService"
outLocation = r'C:\Users\jw\Desktop\610 python\Exercise 3.gdb'
outFClass = "FightCall"
delimitedField = arcpy.AddFieldDelimiters(inFeatures, "CFSType")
expression = delimitedField + " = 'Fight Call'"
 
# Execute FeatureClassToFeatureClass
arcpy.FeatureClassToFeatureClass_conversion(inFeatures, outLocation, 
                                            outFClass, expression)