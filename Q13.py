import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True



current_dir = os.getcwd() 
fgdb_name = 'EX3_13.gdb'
workspace_path = current_dir + '\\' +fgdb_name

    
#SR Definition
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)



arcpy.env.workspace = r'C:\Users\jw\Desktop\610 python\Question 13'
arcpy.FeatureClassToGeodatabase_conversion(['tl_2018_us_county.shp', 'tl_2018_04_tract.shp'],
                                           workspace_path)

#set local variables to create clip_features
delimitedField = arcpy.AddFieldDelimiters('tl_2018_us_county.shp', "NAME")
expression = delimitedField + " = 'Maricopa'"
in_feature1="tl_2018_us_county.shp"
outfile = "MaricopaCounty"
arcpy.FeatureClassToFeatureClass_conversion(in_feature1, workspace_path, 
                                            outfile, expression)


# Set local variables for clip 
arcpy.env.workspace = r'D:\vs2015 项目练习\610EX3\610EX3\EX3_13.gdb'
in_features = "tl_2018_04_tract"
clip_features = "MaricopaCounty"
out_feature_class = "MaricopaCountyTracts"
xy_tolerance = ""

# Execute Clip
arcpy.Clip_analysis(in_features, clip_features, out_feature_class, xy_tolerance)