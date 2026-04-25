class Solution:
    def compress(self, chars: List[str]) -> int:    
        if not chars:
            return 0

        if len(chars)==1:
            return len(chars)

        # two pointer start at 0
        # move j untill char[i] != char[j]
        # if j-i > 1 then append char[i] and j-1
        # move i = j

        s = []
        i = j = 0
        
        while i < len(chars):
            j = i
            while j < len(chars) and chars[j] == chars[i]:
                j += 1
            
            s.append(chars[i])
            counter = j - i
            if counter > 1:
                for digit in str(counter):
                    s.append(digit)

            i = j
            

        s = ''.join(s)
        for i,c in enumerate(s):
            chars[i] = c
        return len(s)