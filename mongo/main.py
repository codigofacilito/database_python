from pymongo import MongoClient
import re


client = MongoClient()
db = client['minicurso_python']

if __name__ == '__main__':
  user1 = {'username': 'codigofacilito1', 'password': 'password123', 'age' : 23}
  user2 = {'username': 'codigofacilito2', 'password': 'password123', 'age' : 24}
  user3 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 25}
  user4 = {'username': 'codigofacilito3', 'password': 'password123', 'age' : 26}

  db.users.insert_many( [user1, user2, user3, user4] )
  # db.users.insert( user1 )

  #result = db.users.insert_one({'username': 'luffy'})
  #print(result.inserted_id)

  for user in db.users.find():
    print(user)

  db.users.find({'username':'codigofacilito1'})
  db.users.find({'username':'codigofacilito1'}).count()
  db.users.find({'username':'codigofacilito1'}).limit(1)

  user = db.users.find_one()
  user = db.users.find_one({'username' : 'codigofacilito1'})

  users = db.users.find({"$or":[ {'usernames':'codigofacilito1'}, {'age':23} ]})
  users = db.users.find({"$and":[ {'usernames':'codigofacilito1'}, {'age':23} ]})

  db.users.update({'username': 'codigofacilito1'}, {'$set' : { 'age' : 30}  })
  db.users.update_many({'password': 'password123'}, {'$inc': {'age': 1}})

  db.users.delete_one({'username': 'codigofacilito1'})
  db.users.delete_many({'password': 'password123'})


  regex = re.compile('codigo')  # LIKE %codigo%
  regex = re.compile('^codigo')  # LIKE %codigo
  regex = re.compile('codigo$')     # LIKE codigo%
    
 
  users = db.users.find_one({'username' : regex })
  




