class Solution:
    # use examples
    # use more metadata about string in encoding - size
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return '0#'

        encoded = str(len(strs)) + '#'
        
        for s in strs:
            encoded += str(len(s)) + '@' + s + '#'
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        
        l = int(s.split('#')[0])
        if l == 0: 
            return []
        
        ### 2#5@hello#5@world#
        s = s[len(str(l))+1 : ]
        decoded = []
        for num_str in range(l):
            print('start',s)
            str_len = int(s.split('@')[0])
            s = s[len(str(str_len))+1 : ]

            print('mid',s)
            string = s[:str_len]
            decoded.append(string)
            s = s[str_len+1:]
            print('end',s)
        
        return decoded

        

