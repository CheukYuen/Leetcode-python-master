import re


class Solution:
    # @param {string[]} strs a list of strings
    # @return {string} encodes a list of strings to a single string
    def encode(self, strs):
        # Write your code here
        for i in range(len(strs)):
            strs[i] = re.sub(r':', '::', strs[i])

        return ':;'.join(strs) + ':;'

        # @param {string} s a string

    # @return {string[]} decodes a single string to a list of strings
    def decode(self, s):
        # Write your code here
        i = 0
        strs = []
        n = len(s)
        while i < n:
            j = s.find(':', i)
            if j == -1:
                break
            if s[j + 1] == ';':
                strs.append(s[i:j])
                i = j + 2
            else:
                strs.append(s[i:j] + s[j + 1:j + 2])
                i = j + 2
                while i+2 <= n and s[i:i + 2] != ':;':
                    if s[i:i + 2] == '::':
                        strs[-1] = strs[-1] + s[i:i + 1]
                        i += 2
                    else:
                        strs[-1] = strs[-1] + s[i]
                        i += 1
                i += 2

        return strs


t = Solution()
s= t.encode([":love;",":;you"])
print s
print t.decode(s)