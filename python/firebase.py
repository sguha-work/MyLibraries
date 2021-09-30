import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# configurations begins
projectId = "fir-project-sguha1988"
serviceAccountJSONFilePath = (
    "fir-project-sguha1988-firebase-adminsdk-3cha6-950836d42b.json"
)
# configurations ends


class FirebaseDB:
    def __init__(self):
        self.serviceAccountJSONFilePath = serviceAccountJSONFilePath
        self.projectId = projectId
        self.__initializeDB()

    # Private methods
    def __initializeDB(self):
        cred = credentials.Certificate(serviceAccountJSONFilePath)
        firebase_admin.initialize_app(cred)

    def __getDBInstance(self):
        dbInstance = firestore.client()
        return dbInstance

    def __convertToCSV(self, data):
        # todo
        return data

    ## Public method begins
    def write(self, collectionName, data):
        dbInstance = self.__getDBInstance()
        collectionRefference = dbInstance.collection(collectionName)
        try: 
            collectionRefference.add(data)
            return 1
        except:
            print("Unable to write database")
            return False

    def writeBulk(self, collectionName, data):
        dbInstance = self.__getDBInstance()
        collectionRefference = dbInstance.collection(collectionName)
        try:
            for index,datum in enumerate(data):
                collectionRefference.add(datum)
            ## Returning number of data inserted
            return index
        except:
            print("Unable to write database")
            return False

    def readCSV(self, collectionName, docName=""):
        dataToReturn = self.read(collectionName, docName)
        # todo
        return self.__convertToCSV(dataToReturn)

    def readJSON(self, collectionName, docName=""):
        dataToReturn = self.read(collectionName, docName)
        return json.dumps(dataToReturn)

    def read(self, collectionName, docName=""):
        dbInstance = self.__getDBInstance()
        collectionInstance = dbInstance.collection(collectionName)
        docs = collectionInstance.stream()
        docToReturn = {}
        if docName == "" or docName == "all":
            for doc in docs:
                docToReturn[doc.id]=doc.to_dict()
        else:
            for doc in docs:
                if doc.id == docName:
                    docToReturn = doc.to_dict()
                break
        return docToReturn
