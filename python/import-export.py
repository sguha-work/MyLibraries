from firebase import FirebaseDB

firebaseObj = FirebaseDB()
firebaseObj.export('BentecDB',['collections_consumers','collections_region','collections_report','collections_user'])
