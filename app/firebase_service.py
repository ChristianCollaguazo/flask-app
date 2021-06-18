import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

credential = credentials.ApplicationDefault()

project_id = 'platzi-flask-d1add'
firebase_admin.initialize_app(credential, {
  'projectId': project_id,
})

db = firestore.client()

def get_users(): 
    return db.collection('users').get()

def get_user(user_id):
  return db.collection('users').document(user_id).get()

def get_todos(user_id):
  return db.collection('users')\
          .document(user_id)\
          .collection('todos')\
          .get()

def user_put(user_data):
  user_ref = db.collection('users')\
    .document(user_data.username)
  user_ref.set({'password': user_data.password})

def put_todo(username, description):
  todo_ref = db.collection('users')\
    .document(username)\
    .collection('todos')
  todo_ref.add({'description': description, 'done': False})

def delete_todo(username, todo_id): 
  todo_ref = _get_todo_ref(username, todo_id)    
  todo_ref.delete()

def update_todo(username, todo_id, done):
  todo_done = not bool(done)
  todo_ref = _get_todo_ref(username, todo_id)
  todo_ref.update({'done': todo_done})


def _get_todo_ref(username, todo_id): 
  return db.collection('users')\
    .document(username)\
    .collection('todos')\
    .document(todo_id)