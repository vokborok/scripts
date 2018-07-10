import ipaddress
import re
int_list=list()
name = input('inter migrated interfaces ip whith prefix , format x.x.x.x/x, write \'done\' at the end\n')
while name != 'done':
    name=ipaddress.ip_interface(name)
    int_list.append(name)
    name = input('one more?\n')
print('interfaces ip:',int_list)

#test
