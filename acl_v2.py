from ciscoconfparse import CiscoConfParse
import re
import ipaddress
#####################################################
acl_list=list()
obj_list=list()
obj_dict=dict()
acl_dict=dict()
#####################################################

#подаем на вход скрипту файл running-config
cisco_cfg = CiscoConfParse("running-config.cfg")


# поиск применненных acl на интерфейсах
all_acl = cisco_cfg.find_all_children('access-group')
#network_group=list()
#service_group=list()
#ip_simple=list()

#print ('before cycle', all_acl)


#находим наименование access-листов и создаем массив acl:all aces
for i in all_acl:
    acl_list.append(i.split()[1])
#print('afte loop objects', acl_list)
for acl in acl_list:
    acl_dict[acl]=cisco_cfg.find_all_children('access-list '+ acl)
    #print(acl,'\n\n', acl_dict[acl], '\n\n\n\n')
    for e in acl_dict[acl]:
       #print(e)
       #n=n+1
       #print(n,'\n')
       #print(e)
       ln=re.findall('(?<=object-group\s)(\w+)', e)
       #obj_list=obj_list+ln
       #print('nmegroup   ',ln,'\n')
      # ln=re.findall('([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\s[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)', e)    #[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\s[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*
       obj_list=obj_list+ln
       #print('ipaddres  ',ln,'\n')

obj_list=set(obj_list)
#print(obj_list,len(obj_list))
for obj in obj_list:
    #print(obj)
    #print(cisco_cfg.find_all_children('^object.*%s' %obj))
    temp_list=(cisco_cfg.find_all_children('^object.*%s' %obj)[1:])
    #print(obj,'\n',temp_list,'\n\n\n')
    for id in temp_list:
        print(id,type(id))
        #if id.startswith('description'):
            #print(id)
    #print(obj,'\n\n', obj_dict[obj], '\n\n\n\n')

#for e in obj_list:
#    print(e)
    #if re.match(r'[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\s[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*',e):
    #    e=e.replace(' ','/')
    #    ip_simple.append(e)
    #elif:
         #= cisco_cfg.find_all_children(r'^group'+e)
#print(ip_simple)











#all_obj = cisco_cfg.find_all_children('object')
#for i in all_obj:
#        if i.startswith("object"):
#            d[i]=cisco_cfg.find_all_children(i)[1:]
#print(d)

#print (acl,'\n', d)
#print(d['dmz'],type(d['dmz']))

#for e in d['dmz']:
#    print(e)
#    ln=re.findall('(?<=object-group\s)(\w+)', e)
#    dmz_obj_list=dmz_obj_list+ln
#    ln=re.findall('([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*\s[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)', e)
#    dmz_obj_list=dmz_obj_list+ln
#print (dmz_obj_list,'\n',set(dmz_obj_list),'\n\n')
