from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
client.drop_database('facbook_data')
db = client['facbook_data']

users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

users_data= [
    { 'user_id': 1, 'name': "Nguyen Van A", 'name': "a@gmail.com", 'age': 25 },
    { 'user_id': 2, 'name': "Tran Thi B", 'name': "b@gmail.com", 'age': 30 },
    { 'user_id': 3, 'name': "Le Van C", 'name': "c@gmail.com", 'age': 22 }
]

post_data = [
    { 'post_id': 1, 'user_id': 1, 'content': "Hom nay that dep troi!", 'created_at': datetime(2024,10,1) },
    { 'post_id': 2, 'user_id': 2, 'content': "Minh vua xem mot bo phim hay!", 'created_at': datetime(2024, 10,2)},
    { 'post_id': 3, 'user_id': 1, 'content': "Chuc moi nguoi mot ngay tot lanh!", 'created_at': datetime(2024,10,3)}
]
comments_data=[
    { 'comment_id': 1, 'post_id': 1, 'user_id': 2, 'content': "Thật tuyệt vời!", 'created_at': datetime(2024,10,1) },
    { 'comment_id': 2, 'post_id': 2, 'user_id': 3, 'content': "Mình cũng muốn xem bộ phim này!", 'created_at': datetime(2024,10,2) },
    { 'comment_id': 3, 'post_id': 3, 'user_id': 1, 'content': "Cảm ơn bạn!", 'created_at': datetime(2024,10,3) }
]

comments_collection.insert_many(comments_data)

users_collection.insert_many(users_data)


posts_collection.insert_many(post_data)

user_ = users_collection.find()
for users in user_:
    print(users)
    
com = comments_collection.find({ 'post_id': 1 })
for cm in com:
    print(cm)
    
uss= users_collection.find({'age': {'$gt': 25 } })
for us in uss:
    print(us)
    
post= posts_collection.find({'created_at': {'$gte': datetime(2024,10,1), '$lt': datetime(2024,11,1) } })
for ps in post:
    print(ps)
    
posts_collection.update_one({ 'post_id': 1 }, { '$set': { 'content': "Hôm nay thời tiết thật đẹp!" } })
for poss in posts_collection.find():
    print(poss)
    
comments_collection.delete_one({'comment_id': 2 })
for i in comments_collection.find():
    print(i)
    
client.close()
