#12)Retrieve records from the GeneralOffense feature class which meet the following criteria:
#     a.Return only records that has the OffenseCus = BURGLARY FORCE and have its field locationTranslation = Residence/Home
#        Finally, write the results to a CSV file.

import arcpy
import csv

featureClass = r'C:\Users\jw\Desktop\610 python\Exercise 3.gdb\General_Offense'
fieldNames = ['primary_key', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand','disclaimer', 'place_name','OffenseCustom','locationTranslation']
cursorFields = ','.join(fieldNames)


filterStatement = "OffenseCustom = 'BURGLARY FORCE'and locationTranslation = 'Residence/Home'"

with open('Q12test.csv','w') as csvFile:
	fileWriter = csv.writer(csvFile,delimiter = ',',quotechar = '|', quoting = csv.QUOTE_MINIMAL)
	fileWriter.writerow(fieldNames)
	with arcpy.da.SearchCursor(featureClass,fieldNames,filterStatement) as cursor:
		for row in cursor:
			fileWriter.writerow(row)

print('Created csv file')
