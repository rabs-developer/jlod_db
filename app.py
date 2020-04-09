from jlod import database, console
import pymongo

dbi = database.connect('example').instance
client = dbi.collection('offers');

host = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = host["example"]
mongoClient = mydb["users"]


# Json Local Document Database (JLOD) is a document oriented database use for
# storing small aplication data offline just like SQLITE but in json fomart, the local database can be exported to Remote MongoDB automatically when needed.
# response = client.exportTo(mongoClient)
# console.log(response)

# for doc in mongoClient.find():
#     console.log(doc)

# client.truncate
# response = client.importFrom(mongoClient,{})
# print(response)

# client.truncate
# result=client.addMany([
#     {"name":"Rabiu","age":22},
#     {"name": "Aminu", "age": 27},
#     {"name": "Aisha", "age": 20},
#     {"name": "Zainab", "age": 21},
#     {"name": "Kehinde", "age": 22},
# ])

# result = client.findOne({
#     'age': 22,
#     'name': 'Kehinde'
# });

# print(result);

# result = client.removeOne({
#     'name': 'Aminu'
# })
# print(result)

# result = client.getOne(['name', 'age'], {
#     'age': 22
# })
# print(result)

# isUpdated = client.update({'name': 'Amina'}, {
#     'name': 'Rabiu'
# })
# if isUpdated:
#     print('updated')
# #


# print(client.find({},2))

# result = client.find({
#     'name': 'kehinde',
#     'age': 22
# })

# print(client.size)

#
result = client.sort(
    {}, {"name":1, "age":1}, limit=5
)
# print(result);
# result = client.addMany([
#     {'name': 'Ummi', 'age': 21},
#     {'name': 'Abubakar', 'age': 20}
# ])

#
# res = client.update(['age', 'name'], [23, 'Khadija'], {
#     'name': 'Aisha'
# })
# print(res)


# res = client.remove({
#     'name': [
#         'Kubra', 'Zainab'
#     ]
# })

#
# search = client.limit(1)
# print(search)
#

# result = client.addMany(
#     {'name': 'Zainab', 'age': 20},
#     {'name': 'Kubra', 'age': 20}
# )

# resultSet = client.documents
# print(resultSet)

# client2.truncate
# client2.remove(name='Rabs')
# client2.drop

# result = client.get(['name','city'])
# console.log(result)

# client2.add({
#     "name": 'Aisha Yahaya',
#     "city": 'Lagos',
#     "age": 23,
# })
#
# name = client.get('name,age', age=23)
# print(name)

# search = client.find(name="Rabs")
# print(search)

# client.add({
#     "name": 'Aisha Yahaya',
#     "city": 'Lagos',
#     "age": 23,
# })

# response = client.documents
# users = client.documents
# for i in users:
#     print(i)
