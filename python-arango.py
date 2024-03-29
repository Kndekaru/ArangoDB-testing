from arango import ArangoClient
import time

# Initialize the ArangoDB client.
client = ArangoClient(protocol='http', host='127.0.0.1', port=8529)


# Connect to "_system" database as root user.
# This returns an API wrapper for "_system" database.
sys_db = client.db('_system', username='root', password='somepassword')


# Connect to "test" database as root user.
# This returns an API wrapper for "test" database.
db = client.db('_system', username='root', password='somepassword')

# Create a new collection named "students" if it does not exist.
# This returns an API wrapper for "students" collection.
if db.has_collection('test'):
    test = db.collection('test')
else:
    test = db.create_collection('test')

# Truncate the collection.
test.truncate()

# Insert new documents into the collection.
def docCreate():
    q = time.time()
    for x in range(1,1001):
        test.insert({'name': 'hello' ,'age': x})
    qw = time.time()
    return (q - qw)

for j in range(1,500):
    print(str(docCreate()))
