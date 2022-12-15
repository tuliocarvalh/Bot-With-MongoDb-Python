import pymongo
from pymongo import MongoClient
import sys
sys.path.insert(0, 'C:/projects/dbmongo')
from pass_ import *
import random
password = password()
url = f"mongodb+srv://tuliocarvalh:{password}@cluster0.wcppq9v.mongodb.net/?retryWrites=true&w=majority"
cluster = MongoClient(url)
db = cluster["house"]
collection = db["speak_01"]

#falas0 = {"speak": "Olá, Marco"}
#falas1 = {"speak": "olá, marco Túlio"}
#falas2 = {"speak": "olá, senhor"}
#falas3 = {"speak": "olá"}
#falas4 = {"speak": "Diga, Marco"}
#falas5 = {"speak": "Pode dizer"}
#falas6 = {"speak": "Estou aqui, Marco"}
#
#collection.insert_many([falas0, falas1, falas2, falas3, falas4, falas5, falas6])
#print(cluster.list_database_names())
#results = collection.distinct("speak")
def talks() :
    results = collection.distinct("speak")
    #for i in results :
#escolhido = random.choice((results))
    escolhido = random.choice((results))
    return str(escolhido)





