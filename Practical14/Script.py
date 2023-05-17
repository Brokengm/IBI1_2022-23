from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd
import openpyxl
def count(id):
    number=0
    for a in terms:
        node_id=a.getElementsByTagName('id')[0]
        is_a_id=a.getElementsByTagName('is_a')
        for b in is_a_id:
            id_value=b.firstChild.nodeValue
            if id==id_value:
                number += count(node_id.firstChild.nodeValue) + 1
    return number# design a function to get the number of childnodes
obo=xml.dom.minidom.parse('go_obo.xml') # parse file
root = obo.documentElement
terms=root.getElementsByTagName('term')
list_termname=list()
list_id=list()
list_def=list()
list_childnode=list()# create a list to store data
for x in terms:
    defstr = x.getElementsByTagName('defstr')[0] #get defstr in term
    if 'autophagosome' in defstr.firstChild.nodeValue:
        list_id.append(x.getElementsByTagName('id')[0].firstChild.nodeValue)
        list_termname.append(x.getElementsByTagName('name')[0].firstChild.nodeValue)
        list_def.append(defstr.firstChild.nodeValue)
        list_childnode.append(count(x.getElementsByTagName('id')[0].firstChild.nodeValue))# append each data to its list
dataframe={
    'id':list_id, 'term name':list_termname, 'def':list_def, 'childnodes':list_childnode
}    # integrate all the data
Data=pd.DataFrame(dataframe)
Data.to_excel('Result.xlsx',index=False)# output all data in a excel file