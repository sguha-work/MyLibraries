from csvParser import CsvParser
from firebase import FirebaseDB
import json

csvParserobj = CsvParser("sample-csv.csv")
data = json.loads(csvParserobj.getJSONData())
firebaseObj = FirebaseDB()

## Bulk insert example
# dataToWrite = {
#     'items': data
# }
# firebaseObj.write(u'users',u'agents', dataToWrite)