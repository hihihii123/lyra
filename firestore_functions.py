import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account
from auth_functions import getUserId
import json


## LOAD DB

creds = service_account.Credentials.from_service_account_info(st.secrets["firestore"])
db = firestore.Client(credentials=creds, project=st.secrets['firestore']['project_id'])



## FIRESTORE FUNCTIONS

# Write a document
def writeorupdateDocument(collection, documentid, content, subcollection=None, subcollectionid=None):
    """
    Docstring for writeorupdateDocument
    
    WRITE ONE EACH FOR MAIN FIELDS AND SUBCOLLECTIONS
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

    doc_ref.set(content) # merge=True updates existing fields


# Read a specific document, with optional parameter to read subcollections [for id,  use getUserId from auth_functions]
def readDocumentFromCollection(collection, documentid, subcollection=None, subcollectionid=None, field=None):
    if subcollection:

        # Reads all documents from a subcollection
        if not subcollectionid:
            print(f"Accessing all documents in {subcollection}")
            doc_ref = db.collection(collection).document(documentid)
            all_docs = []

            for subref in doc_ref.collections():
                for doc in subref.stream():
                    doc_data = doc.to_dict()[field]
                    all_docs.append(doc_data)
            return all_docs
        doc_ref = db.collection(collection).document(documentid).collection(subcollection).document(subcollectionid)
    else:
        doc_ref = db.collection(collection).document(documentid)

    doc = doc_ref.get() 

    if doc.exists:
        doc = doc.to_dict()
        if not field:
            return doc
        else:
            return doc[field]   # Returns a field of the document
    else:
        print("No such document")
        return None


# Delete document
def deleteFromCollection(collection, documentid): # [doesnt delete subcollections]
    if db.collection(collection).document(documentid).get().exists:  # Existence check
        db.collection(collection).document(documentid).delete()
    else:
        print("No such document")




## TEMPLATE !!!!
if __name__ == "__main__":
    with open("resources/hi.json", "r") as fin:
        data = json.load(fin)

    name = data["name"]
    writeorupdateDocument("users", getUserId(), data, "studyplans", name)