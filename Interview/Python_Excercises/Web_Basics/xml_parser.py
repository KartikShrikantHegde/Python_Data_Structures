'''
Input format:

6 4
<tag5>
    <tag1 value="abc">
        <tag2 name="xyz">
        </tag2>
    </tag1>
</tag5>
<tag16>
<tag18 name="afs">
</tag18>

tag5.tag1~value
tag5.tag1.tag2~name
tag1~name
tag3~value

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from xml.etree import ElementTree as ET

my_input = raw_input()
lines = int(my_input.split()[0])
cond = int(my_input.split()[1])


my_str = "<root>"
#my_str = ''
for i in range(lines):
    each_line = raw_input()
    my_str = my_str + each_line

my_str += "</root>"
try:
    root = ET.fromstring(my_str)
    # print root.tag, root.attrib
    my_arr = []
    for query in range(cond):
        each_query = raw_input()
        my_arr.append("root."+each_query)

    for my_query in my_arr:
        new_q = my_query.split('~')
        if '.' not in new_q[0]:
            if new_q[0] == root.tag:
                if new_q[1] in root.attrib.keys():
                    print root.attrib[new_q[1]]
                else:
                    print "Not Found!"
            else:
                print "Not Found!"
        else:
            my_str = ''
            new_arr = new_q[0].split('.')
            for val in range(1,len(new_arr)):
                my_str = my_str + '/' + new_arr[val]
            x = root.findall("."+my_str)
            if not x:
                print "Not Found!"
            for val in x:
                if new_q[1] in val.attrib.keys():
                    print val.attrib[new_q[1]]
                else:
                    print "Not Found!"
except:
    print "Not Found!"