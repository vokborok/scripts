from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("running-config.cfg")
#fhand=open('running-config.cfg')
d=dict()
all_children = cisco_cfg.find_all_children('object')
for i in all_children:
        if i.startswith("object"):
            d[i]=cisco_cfg.find_all_children(i)[1:]

for k in d:
   print(k ,d[k])

print(k)


#obj=cisco_cfg.find_objects(r"^object")
#for i in obj:
# i=str(i).split()
# print(i[5], cisco_cfg.find_children(obj))
 #print(cisco_cfg.find_children(i[5]))

 #test GIT
