import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# configurations begins
projectId = "developmentdb-51821"
serviceAccountJSONFilePath = (
    "developmentdb-51821-firebase-adminsdk-x53l8-6b69f0fa61.json"
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
        batch = dbInstance.batch()
        for index, datum in enumerate(data):
            newDoc = collectionRefference.document()
            batch.set(newDoc, datum)
        try:
            batch.commit()
        except:
            print('Unable to write database')
        ## Returning number of data inserted
        return (index + 1)

    def export(self, dbName, collectionNamesList):
        dataToReturn = {dbName: {}}
        for index, collectionName in enumerate(collectionNamesList):
            dataToReturn[dbName][collectionName] = self.read(collectionName);
        file = open(dbName+"_exported.json", "w")
        file.write(json.dumps(dataToReturn))
        file.close()
    def importDB(self, dbName):
        return
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
                docToReturn[doc.id] = doc.to_dict()
        else:
            for doc in docs:
                if doc.id == docName:
                    docToReturn = doc.to_dict()
                break
        return docToReturn
