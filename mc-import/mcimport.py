# before running, do: export GOOGLE_APPLICATION_CREDENTIALS=/Users/neumark/Downloads/rajzolos-11b35-firebase-adminsdk-vm3lo-717ee0d92c.json
from google.cloud import firestore

# Add a new document
db = firestore.Client()
doc_ref = db.collection(u'drawings').document(u'-LSPPtz49XRf1vdBmFul')
print(doc_ref.get().to_dict())
