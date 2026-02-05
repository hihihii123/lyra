# structure
'''
1. users/{userid}}
    > name
    > year
    > subjectCodes (array)
2. studyPlans/{planid}
    > name
    > subjectCode
    > tasks (array??)
    > planCompletion
    > completionDate
    > archived
3. tasks/{taskid}
    > name
    > description
    > completionStatus
    > startDate
    > dueDate
'''

import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

# Load credentials
creds = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
db = firestore.Client(credentials=creds, project=st.secrets['firestore']['project_id'])


# Write a doc
def writeToFirestore(collection, documentid, content):
    doc_ref = db.collection(collection).document(documentid)
    doc_ref.set(content)


# Read a specific document (for id, use doc.id. maybe separate function or something)
def readFromFirestore(collection, documentid, key=None, type=None):
    doc_ref = db.collection(collection).document(documentid)
    doc = doc_ref.get()

    if doc.exists:
        st.write(doc)
        if key is None:
            return doc.to_dict()
        else:
            return doc.to_dict()[key]
    else:
        print("No such document")


def deleteFromFirestore(collection, documentid): # doesnt delete subcollections
    if db.collection(collection).document(documentid).get().exists:
        db.collection(collection).document(documentid).delete()
    else:
        print("No such document")


writeToFirestore('users', '4', {'name': 'Martshias', 'subjects': ['Chinese', 'Chemistry'], 'year':2011})
# st.write(readFromFirestore('users', '2', 'name'))
# deleteFromFirestore("users", "2")

