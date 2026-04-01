class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##clarify
        #duplicate chars allowed? seen in example
        # are numbers there?-no see constraints only english lowercase
        # fits in memeory?

        #valid ex
        # rrccaae

        #bruteforce
        # use dict
        #search through entire string in 2 for loop and keep count of every char
        # s = list(s)
        # t = list(t)
        if len(s) != len(t):
            return False

        #initialize dict
        seen = {s_char:0 for s_char in s} 
        seen.update(
            {t_char:0 for t_char in t}
        )

        # {j:0, a:0, r:0, m:0}
        #update dict
        for s_char, t_char in zip(s,t):
            seen[s_char] += 1
            seen[t_char] -= 1

        #check each key should have 0
        for key,value in seen.items():
            if value != 0:
                return False
        return True

        




        