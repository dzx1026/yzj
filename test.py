import pymongo
from bson.objectid import ObjectId

conn = pymongo.MongoClient('172.16.101.118', 27018)
db = conn.kingdeeMongo  #连接mydb数据库，没有则自动创建
my_set = db.fs.chunks  #使用test_set集合，没有则自动创建

condition = {'files_id':ObjectId('5b17b346e4b01c5c8e42ed5f')}
record = my_set.find_one(condition)
for value in my_set.find({'files_id':ObjectId('5b17b346e4b01c5c8e42ed5f')}):
    print(value['data'].decode('utf-8'))


# with open('test.html','rb') as f:
#     record['data']=f.read()

# result = my_set.update(condition,record)
# print(result)