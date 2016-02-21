import pymongo as pm
import csv
from pprint import pprint
import sys
# from bs4 import BeautifulSoup
# import requests, json

try:
    fName = sys.argv[1]
    print fName
except:
    print "No filename"
    sys.exit(0)
# connect to database
connection = pm.MongoClient('localhost', 27017)
db = connection.demoDB
collection = db['products']

def convert2unicode(mydict):            
    for k, v in mydict.iteritems():
        if isinstance(v, str):
            mydict[k] = unicode(v, errors = 'replace')
        if isinstance(v, int):
            mydict[k] = int(v)
        elif isinstance(v, dict):
            convert2unicode(v)
    return mydict


try:
    with open(fName, 'rb') as f:
        csvfile = csv.DictReader(f, delimiter=',', quotechar='"') 
        for row in csvfile:
            pprint(row)
            row = convert2unicode(row)
            if 'accessories' in row['pic_name'].lower():
                row['category'] = 'Accessory'
            else:
                row['category'] = 'Kleding'
            result = collection.insert(row)
except Exception as e:
    print e
    sys.exit(0)
