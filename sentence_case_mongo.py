import pymongo
from collections.abc import MutableMapping
from mongodict import MongoDict

proper_nouns = MongoDict(host='original.bnijl2q.mongodb.net', port=27017, database='proper_nouns',
                        collection='store', auth=('SeaSpree', '3ZXY7NTMIgPvGSkf'))

proper_nouns["happiness"] = "boo"


print(proper_nouns)