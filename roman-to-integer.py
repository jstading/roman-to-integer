# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def numerals(self, s):
        numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integers = []
        n = 0
        answer = 0

        for c in s:
            integers.append(numerals.get(c))

        while n+1 < len(s):
            if integers[n] >= integers[n+1]:
                answer = answer + integers[n]
            else:
                answer = answer - integers[n]
            n+=1

        if integers[-1] >= integers[-2]:
            answer = answer + integers[-1]
        else:
            answer = answer - integers[-1]

        return answer

##############################
#s = "III"
#s = "LVIII"
s = "MCMXCIV"
#s = "DCXXI"
#Returns should be 3, 58, 1994, 621
##############################

#s = "CMVII"
Solution = Solution()
print(Solution.numerals(s))
