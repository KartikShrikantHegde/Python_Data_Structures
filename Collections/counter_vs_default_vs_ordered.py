from collections import Counter
words = ["oranges", "apples", "apples", "bananas", "kiwis", "kiwis", "apples"]
c = Counter(words)
print(c)
print "\n"

from collections import OrderedDict
d = OrderedDict()

for word in words:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

print d

print "\n"
from collections import defaultdict

de = defaultdict(int)

for word in words:
    de[word] = de[word] + 1

print de