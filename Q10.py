#Perform a spatial join between the census tracts feature class and the general offense feature 
#class

import arcpy
from arcpy import env
env.overwriteOutput = True

target_features = r"C:\Users\jw\Desktop\610 python\Exercise 3.gdb\Tracts"
join_features = r"C:\Users\jw\Desktop\610 python\Exercise 3.gdb\General_Offense"
out_feature_class = r"C:\Users\jw\Desktop\610 python\Exercise 3.gdb\OjoinT"

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)