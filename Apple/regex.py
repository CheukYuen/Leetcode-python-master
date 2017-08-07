import re

f = open('foo.txt', 'rU')

text = f.read()

# Account Holder:Leon, asdfsdfAccount Data:123, 2123.21,
# rank by trade
# output: 'name trade'

tuples = re.findall(r'Account\sHolder:(\w+)[\w,\s]*Account\sData:.*\s(\d+.\d\d)', text)

if not tuples:
    print 'Could,\'t find the year!\n'

name_to_trade = {}

for name_tuple in tuples:
    (name, trade) = name_tuple
    if name not in name_to_trade:
        name_to_trade[name] = trade

sorted_name = sorted(name_to_trade.keys())

ans = []
for name in sorted_name:
    ans.append(name + ' ' + name_to_trade[name])
print ans
