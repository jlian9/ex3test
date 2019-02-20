import os
import sys
import arcpy

from arcpy import env
env.overwriteOutput = True



current_dir = os.getcwd() 
fgdb_name = '610pythonEX3.gdb'
workspace_path = current_dir + '\\' +fgdb_name

#fc_path = workspace_path + '\\'  + fc_name
    
#SR Definition
SRDefinition="PROJCS['WGS_1984_Web_Mercator_Auxiliary_Sphere',GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Mercator_Auxiliary_Sphere'],PARAMETER['False_Easting',0.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',0.0],PARAMETER['Standard_Parallel_1',0.0],PARAMETER['Auxiliary_Sphere_Type',0.0],UNIT['Meter',1.0]];-22041257.773878 -33265068.6042249 10000;-100000 10000;-100000 10000;0.001;0.001;0.001;IsHighPrecision"

#create a gdb
arcpy.CreateFileGDB_management(current_dir, fgdb_name)
 




   
featureList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']




#Create the Feature Class
#go through the list and create one by one 
for featureName in featureList:
 arcpy.CreateFeatureclass_management(out_path=workspace_path
                                    , out_name=featureName
                                    , geometry_type=""
                                    , template=""
                                    , has_m="DISABLED"
                                    , has_z="DISABLED"
                                    , spatial_reference=SRDefinition
                                    , config_keyword=""
                                    , spatial_grid_1="0"
                                    , spatial_grid_2="0"
                                    , spatial_grid_3="0"
                                    )
print('Done creating feature class')
    