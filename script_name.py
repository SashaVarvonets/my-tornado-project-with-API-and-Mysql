import sys
import argparse
from datetime import date, timedelta

import requests
import xml.etree.cElementTree as etree


try:
    parser = argparse.ArgumentParser()
    parser.add_argument('--date_ranges')

    namespace = parser.parse_args()

    start, end = namespace.date_ranges.split('_')
except:
    start, end = date.today() - timedelta(7), date.today()



url = 'http://88.214.193.118/ssp_xml.php'
endpoint = 'imonomy_US_EAST_imonomy_native'
apikey = 'qTigpObMPU35vTILorFQ'
params = {
    'endpoint': endpoint,
    'apikey': apikey,
    'start': start,
    'end': end,
}

r = requests.get(url=url, params=params)

tree = etree.fromstring(r.text)
tree = etree.ElementTree(tree)
# tree = etree.ElementTree(file='updated.xml')
# --------------------------------------------------
root = tree.getroot()
# print(root.tag, root.attrib)
# for child in root:
#     print(child.tag,child.attrib)
#     for step_child in child:
#         print(step_child.tag, step_child.text)
# --------------------------------------------------
# iter_ = tree.iter()
#
# for elem in iter_:
#     print(elem.tag, elem.attrib, elem.text)
# --------------------------------------------------

appointments = root.getchildren()

for appointment in appointments:
    print appointment.attrib
    appt_children = appointment.getchildren()
    for appt_child in appt_children:
        print("%s=%s" % (appt_child.tag, appt_child.text))
