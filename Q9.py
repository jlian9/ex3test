#Create a feature class (you may re-use the geodatabase from Question 5). Add a field to your 
#feature class. Then add a domain to the just created field. Finally, add at least 5 values to your 
#domain. (*Your domain may be of any type)
import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True
current_dir = os.getcwd() 
fgdb_name = 'DataCollection.gdb'
workspace_path = current_dir + '\\' +fgdb_name
arcpy.env.workspace = r'D:\vs2015 项目练习\610EX3\610EX3\DataCollection.gdb'

arcpy.CreateFeatureclass_management(fgdb_name, "test", "POINT")

#add field
arcpy.AddField_management("test", "rateScore", "TEXT")

# Set local parameters
domName = "Rate"
gdb = "DataCollection.gdb"

inField = "rateScore"

# Process: Create the coded value domain
arcpy.CreateDomain_management("DataCollection.gdb", domName, "score", 
                              "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the "key" 
# and the domain description as the "value" (domDict[code])
domDict = {"A":"111", "B": "222", "C": "333", 
           "D": "444", "E": "555"}
    
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

# Process: Constrain the material value of distribution mains
arcpy.AssignDomainToField_management('test', inField, domName)