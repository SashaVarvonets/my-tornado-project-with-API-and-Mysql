import data_save

import mysql.connector
import sys
import argparse
from datetime import date, timedelta

import requests
import xml.etree.cElementTree as etree


# Parse additional argument
try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--date_ranges')

    namespace = parser.parse_args()

    start, end = namespace.date_ranges.split('_')
except:
    start, end = date.today() - timedelta(7), date.today()


# Data for SQL queries
my_db = mysql.connector.connect(
        host="localhost",
        user="sasha",
        passwd="admin",
        database="imonomy_db"
    )


# Data for API
url = 'http://88.214.193.118/ssp_xml.php'
endpoint = 'imonomy_US_EAST_imonomy_native'
apikey = 'qTigpObMPU35vTILorFQ'
params = {
    'endpoint': endpoint,
    'apikey': apikey,
    'start': start,
    'end': end,
}

# API call
r = requests.get(url=url, params=params)
tree = etree.fromstring(r.text)
tree = etree.ElementTree(tree)
root = tree.getroot()
items = root.getchildren()


lst = []
for item in items:
    a = item.attrib

    appt_children = item.getchildren()
    for appt_child in appt_children:
        a[appt_child.tag] = appt_child.text

    lst.append(a)

if data_save.save_data(lst, my_db):
    print 'Data successfully saved'
else:
    print 'Something goes wrong'
