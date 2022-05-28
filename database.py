import pymysql, os, json
from pprint import pprint
# read JSON file which is in the next parent folder
#file = "table2.json"
#json_data=open(file).read()
#json_obj = json.loads(json_data)


with open('table2.json', encoding='utf-8') as json_data:
    json_obj = json.loads(json_data.read())
#pprint(json_obj)


#with open('table2.json', encoding='utf8')as json_data:
#    json_obj = json.load(json_data)
#    print(json_data)


# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host = 'localhost',user = 'root',passwd = '0808',db = 'werez')
cursor = con.cursor()


# parse json data to SQL insert
for i, item in enumerate(json_obj):
    imdb = validate_string(item.get("imdb", None))
    title = validate_string(item.get("title", None))
    data = validate_string(item.get("data", None))
    embed = validate_string(item.get("embed", None))

    cursor.execute("INSERT INTO werez (imdb, title,	data, embed) VALUES (%s, %s, %s, %s)", (imdb, title, data, embed))
con.commit()
con.close()
