class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        info = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L": 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            "P" : 0
        }
        total = 0
        i=0
        while i<len(s):
            roman = (s[i])
            if i+1<len(s):
                next_roman = s[i+1]
            else:
                next_roman = 'P'
            current = info[roman]
            next = info[next_roman]
            value = current
            if current < next :
                value = next - current
                i+=1
            total = total + value
            i+=1
        return total

## I Wrote the above logic myself. but the idea one is below :

total = 0

for i in range(len(s)):
    if i + 1 < len(s) and info[s[i]] < info[s[i+1]]:
        total -= info[s[i]]
    else:
        total += info[s[i]]

return total
            
