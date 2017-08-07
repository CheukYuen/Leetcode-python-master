import re
import collections


class Solution:
    # @param {string} input an abstract file system
    # @return {int} return the length of the longest absolute path to file
    def lengthLongestPath(self, input):
        # Write your code here
        dict = collections.defaultdict(lambda: '')
        lines = input.split("\n")

        n = len(lines)
        result = 0
        for i in xrange(n):
            count = lines[i].count("\t")

            lines[i] = dict[count - 1] + re.sub(r"\t+", "/", lines[i])
            if "." in lines[i]:
                result = max(result, len(lines[i]))
            dict[count] = lines[i]

        return result

text = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
s = Solution()
print s.lengthLongestPath(text)