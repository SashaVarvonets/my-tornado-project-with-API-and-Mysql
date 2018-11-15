import requests
import argparse

from data_saver import data_saver

from datetime import date, timedelta

import xml.etree.cElementTree as etree


start, end = date.today() - timedelta(6), date.today()
new_db = False

# Pars arguments if they exist.
parser = argparse.ArgumentParser()
parser.add_argument('--date_ranges')
parser.add_argument('--create_new_db')
namespace = parser.parse_args()
if namespace.date_ranges:
    start, end = namespace.date_ranges.split('_')
if namespace.create_new_db:
    new_db = True


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
    # make dict
    a = item.attrib
    # get children
    appt_children = item.getchildren()
    for appt_child in appt_children:
        a[appt_child.tag] = appt_child.text

    lst.append(a)

if data_saver(lst, new_db):
    print 'Data successfully saved'
else:
    print 'Something goes wrong'
