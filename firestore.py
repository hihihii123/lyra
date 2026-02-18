import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

# Load db
creds = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
db = firestore.Client(credentials=creds, project=st.secrets['firestore']['project_id'])


# Write a doc  -- maybe change documentid to userid if root level is standardised
def writeorupdateDocument(collection, documentid, content, subcollection=None, subcollectionid=None):
    """
    Docstring for writeorupdateDocument
    
    :param collection: str; collection name
    :param documentid: str; typically user id
    :param content: dict; content to write in collection or subcollection depending on specifications
    :param subcollection: str, [subcollection name]
    :param subcollectionid: str, [subcollection document id]
    """
    if subcollection:
        if not subcollectionid:
            print("subcollectionid is required")
        doc_ref = db.collection(collection).document(documentid).collection(subcollection).document(subcollectionid)
    else:
        doc_ref = db.collection(collection).document(documentid)

    doc_ref.set(content, merge=True) # merge updates existing fields


# Read a specific document (for id,  use getUserId from auth_functions)
def readDocumentFromCollection(collection, documentid, subcollection=None, subcollectionid=None, field=None):
    if subcollection:
        if not subcollectionid:
            print("subcollectionid is required")
        doc_ref = db.collection(collection).document(documentid).collection(subcollection).document(subcollectionid)
    else:
        doc_ref = db.collection(collection).document(documentid)

    doc = doc_ref.get()

    if doc.exists:
        doc = doc.to_dict()
        if not field:
            return doc
        else:
            return doc[field]
    else:
        print("No such document")
        return None


def deleteFromCollection(collection, documentid): # doesnt delete subcollections
    if db.collection(collection).document(documentid).get().exists:
        db.collection(collection).document(documentid).delete()
    else:
        print("No such document")



writeorupdateDocument('users', '4', {'weak': ['None'], 'strong': ['NOI']}, "preferences", "strengths")
# print(readDocumentFromCollection('users', '2'))
# deleteFromFirestore("users", "2")

