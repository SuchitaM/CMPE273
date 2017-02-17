import psutil
from collections import namedtuple

from operator import itemgetter, attrgetter

nc=psutil.net_connections()
#print nc
attributeList=[]
SocketConn=namedtuple('sconn', ['fd', 'family', 'type', 'laddr', 'raddr', 'status', 'pid'])


my_list2=[]
my_list3=[]
my_list4=[]

for i in nc:
   a=SocketConn(*i)
   #print a
   attributeList.append(a.pid)
   attributeList.append(a.laddr)
   attributeList.append(a.raddr)
   attributeList.append(a.status)
   #df=pd.DataFrame({'pid':a.pid,'laddr':a.laddr,'raddr':a.raddr,'status':a.status})
print sorted(attributeList)

def getattribute(a,attributelist):
    my_dict={}
    for attribute in attributeList:
        my_dict[attribute]=[]
    for line in range(len(a)):
        for element in line:
            my_dict[element].append(line.get(element))

   



#print my_list1
#print sorted(my_list1)
#print my_list2
#print my_list3
#def getKey(my_list1):
#    return my_list1[0]
#print sorted(my_list2, key=getKey)

