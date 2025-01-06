from ciscoconfparse import CiscoConfParse
parse1 = CiscoConfParse('showrun.conf',syntax='ios')

#result = parse1.find_children_w_parents('^router ospf.*','.*')

result = parse1.find_all_children('.*')
print(result)

for i in result:
    print(i)