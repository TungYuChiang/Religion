import pymongo

myclient = pymongo.MongoClient("mongodb+srv://jackson:IM880319@immortal-free.rxzaq.mongodb.net/?retryWrites=true&w=majority") 
db = myclient["myFirstDatabase"]
##連接至database底下的collection 


#for item in collection_name.find():
#   print(item['name'])


#刪除姓名或性別為空白的值
def del_space(col_na):
    space = {'name':''}
    sex_space = {'sex':''}
    col_na.delete_many(space)
    col_na.delete_many(sex_space)

#刪除成員，參數為collection及要刪除成員的name
def del_member(col_name, name):
    tmp = {'name' : name }
    col_name.delete_one(tmp)
    print("成功刪除"+ name)
#更新資訊參數為collection 
def update(col_name, name, attr, val):
    myquery = {'name':name}
    newvalues = { "$set": { attr: val } }
    x = col_name.update_many(myquery, newvalues)
    print(name+attr+'已修改為'+val)
#c_name = ['張法聖', '沈睿賢', '吳昱慧', '賴年盛', '王冠琪', '賴明希', '嚴漢枝', '湯成禧', '張吉宏', '湯成茵','張肯宥']
#for name in c_name:
#    update_light(db.light, name)
#del_member(db.light, '湯熙熊')
#del_space(db.light)
update(db.light, '謝明惠', 'sex', '女')


    


