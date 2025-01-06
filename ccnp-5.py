import re

pattern = '.*'

string = '''
+86-411-82866931
86411-82866931
'''

result = re.findall(pattern=pattern, string=string)
print(result)