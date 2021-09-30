from csvParser import CsvParser
from firebase import FirebaseDB
import json

csvParserobj = CsvParser("sample-csv.csv")
data = json.loads(csvParserobj.getJSONData())
firebaseObj = FirebaseDB()
# read entire collection example
# firebaseObj.read('users')

## Bulk insert example
# firebaseObj.writeBulk(u'users',u'agents', data)
## Single insert example
firebaseObj.write(u'users',u'agents', {
      "Sno": "1",
      "Consumer ID": "2720629",
      "Current Status": "Running ",
      "Subdivision": "Jamtara ",
      "Consumer No": "PDRCS00091 ",
      "K No": "",
      "Name": "M/s TOWER VISION INDIA ",
      "Address": "C/o KAMLAKANT TRIPATHI  PINDARI ",
      "Load": "10",
      "Meter Slno": "Y0274439 \n"
    }, False)