import pyrebase
import json 
from datetime import datetime 

class DBhandler:
    def __init__(self):
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()


    def insert_user(self, data, pw):
        user_info = {
            "id": data['id'],
            "pw": pw,
            "email": data['email'],
            "phone": data['phone']
        }

        if self.user_duplicate_check(str(data['id'])):
            self.db.child("user").push(user_info)
            print(data)
            return True
        else:
            return False

    def user_duplicate_check(self, id_string):
        users = self.db.child("user").get()
        print("users###",users.val())

        if str(users.val()) == "None": # first registration
            return True
        else:
            for res in users.each():
                value = res.val()

                if value['id'] == id_string:
                    return False
            return True
    
    def find_user(self, id_, pw_):
        users = self.db.child("user").get()
        target_value=[]
        for res in users.each():
            value = res.val()
            if value['id'] == id_ and value['pw'] == pw_:
                return True
        return False
    

    #review 
    def get_reviews(self):
         reviews = self.db.child("review").get().val()
         return reviews

    def insert_review(self, title, data, img_path,user_id):
        review_info = {
            "writer": user_id,
            "product": data["product"],
            "title": data["title"],
            "content": data["content"],
            "payment": data["payment"],
            "rating": data["rating"],
            "img_path": img_path,
            "date": datetime.now().strftime("%Y-%m-%d"),  # 현재 날짜를 문자열로 포맷
        }

        self.db.child("review").child(title).set(review_info)
        return True    
    def get_review_bytitle(self, title):
        reviews = self.db.child("review").get()
        for res in reviews.each():
            if res.key() == title:
                return res.val() 
        return None  
           

    # item
    def get_items(self):
        items = self.db.child("item").get().val()
        return items
    
    def insert_item(self, title, data, user_id, img_path):
        item_info ={
            "seller": user_id,
            "price" : data["price"],
            "addr": data['addr'],
            "phone": data['phone'],
            "card": data['card'],
            "payment" : data["payment"],
            "condition": data['condition'],
            "description" : data["description"],
            "img_path": img_path
        }
        self.db.child("item").child(title).set(item_info)
        print(data,img_path)
        return True
        
    def get_item_byname(self, name):
        items = self.db.child("item").get()
        target_value=""
        print("##########", name)
        for res in items.each():
            key_value = res.key()

            if key_value == name:
                target_value = res.val()
        return target_value
    
    # group
    def get_groups(self):
        groups = self.db.child("group").get().val()
        return groups
    
    def insert_group(self, title, data, user_id):
        group_info ={
            "writer": user_id,
            "phone": data['phone'],
            "category": data['category'],
            "description" : data["description"],
            "status" : "모집중"
        }
        self.db.child("group").child(title).set(group_info)
        return True

    def get_group_bytitle(self, title):
        items = self.db.child("group").get()
        target_value=""
        print("##########", title)
        for res in items.each():
            key_value = res.key()
            
            if key_value == title:
                target_value = res.val()
        return target_value
    
    
    #좋아요
    def get_heart_byname(self, uid, name):
        hearts = self.db.child("heart").child(uid).get()
        target_value=""
        if hearts.val() == None:
            return target_value

        for res in hearts.each():
            key_value = res.key()

            if key_value == name:
                target_value=res.val()
        return target_value

    def update_heart(self, user_id, isHeart, item):
        heart_info ={
        "interested": isHeart
        }
        self.db.child("heart").child(user_id).child(item).set(heart_info)
        return True   