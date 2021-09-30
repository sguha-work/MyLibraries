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
    def write(self, collectionName, documentName, data, merge=True):
        dbInstance = self.__getDBInstance()
        documentRefference = dbInstance.collection(collectionName).document(
            documentName
        )
        if merge == True:
            print(len(self.read(collectionName, documentName)))
        else:
            dataToWrite = {}
            items = []
            items.append(data)
            dataToWrite.update({"items":items})
            documentRefference.set(dataToWrite)

    def writeBulk(self, collectionName, documentName, data, merge=True):
        dbInstance = self.__getDBInstance()
        dataToWrite = {"items": data}
        documentRefference = dbInstance.collection(collectionName).document(
            documentName
        )
        try:
            if merge == True:
                documentRefference.set(dataToWrite, merge=True)
            else:
                documentRefference.set(dataToWrite)
            return True
        except:
            print("Unable to write database")

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
        docToReturn = []
        if docName == "" or docName == "all":
            for doc in docs:
                for item in doc.to_dict()["items"]:
                    docToReturn.append(item)
                break
        else:
            for doc in docs:
                if doc.id == docName:
                    for item in doc.to_dict()["items"]:
                        docToReturn.append(item)
                    break
        return docToReturn
