str = """z,xcnkdjnfsjdnfkj23123123
Account Holder:Leon, Account Data:123, 2123.21,
 asdasd, 123asdkk
 Account Holdent Holder:Marry, Account Data:123, 2456456.21,
 asd12312asasd
  Account Holder:King, Account Data:123, 678678.21,
  asdas"""

import os

# out put name  > 1m
# print str
for s in str.split(os.linesep):
    print s


def main(data):
    n = len(data)
    print 'aaa', n
    accountHolder = 'Account Holder:'
    accountData = 'Account Data:'
    trade = ''
    accountHash = []
    for i in range(n):
        new_account_flag = False
        for j in range(len(accountHolder)):
            if data[i + j] != accountHolder[j]:
                break
            if j == len(accountHolder) - 1:
                print i
                k = i + j + 1
                l = 0
                while data[k + l] != ',':
                    l += 1
                account_name = data[k: k + l]
                accountHash.append(account_name)
                new_account_flag = True
        for m in range(len(accountData)):
            if new_account_flag:
                break
            if data[i + m] != accountData[m]:
                break
            if m == len(accountData) - 1:
                runner = m + i
                while True:
                    if data[runner] == '.' and data[runner + 1].isdigit() and data[runner + 2].isdigit() and data[
                                runner + 3] == ',':
                        break
                    runner += 1
                start = runner
                while True:
                    if data[start] == ' ':
                        break
                    start -= 1
                accountHash.append(data[start+1:runner + 3])
                new_account_flag = False
    return accountHash


# print main(str)
