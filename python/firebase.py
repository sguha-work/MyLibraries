import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#configurations begins
projectId = "fir-project-sguha1988"
serviceAccountJSONFilePath = "fir-project-sguha1988-firebase-adminsdk-3cha6-950836d42b.json"
#configurations ends

# cred = credentials.Certificate(serviceAccountJSONFilePath)
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     'first': 'Ada',
#     'last': 'Lovelace',
#     'born': 1815
# })
class FirebaseDB:
    def __init__(self):
        self.serviceAccountJSONFilePath = serviceAccountJSONFilePath
        self.projectId = projectId
        self.__initializeDB()
    def __initializeDB(self):
        cred = credentials.Certificate(serviceAccountJSONFilePath)
        firebase_admin.initialize_app(cred)
    def __getDBInstance(self):
        dbInstance = firestore.client()
        return dbInstance
    def write(self, collectionName, documentName, data, merge=True):
        dbInstance = self.__getDBInstance()
        documentRefference = dbInstance.collection(collectionName).document(documentName)
        try:
            if(merge == True):
                documentRefference.set(data,  merge=True)
            else:
                documentRefference.set(data)
            return True
        except:
            print('Unable to write database')
            
    def read(self, collectionName, asJSON=True):
        dbInstance = self.__getDBInstance()
        collectionInstance = dbInstance.collection(collectionName)
        docs = collectionInstance.stream()
        for doc in docs:
            print(f'{doc.id} => {doc.to_dict()}')

