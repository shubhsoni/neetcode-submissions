class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ''

        ans = {} # key-len, value-string
        # sset = set(list(t)) <- cannot use set since duplicates are valid in t
        smap = collections.Counter(t)

        ans_str = ''
        l,r = 0,0

        while l < len(s):
            # Reset state for a new window starting at l
            smap = collections.Counter(t)
            ans_str = ''
            r = l
            
            # Move r to find a valid window
            while r < len(s):
                if s[r] in smap:
                    smap[s[r]] -= 1
                
                ans_str += s[r]
                
                # Check if all requirements in smap are met (all values <= 0)
                if all(v <= 0 for v in smap.values()):
                    ans[len(ans_str)] = ans_str
                    break
                r += 1
            
            l += 1

        answers = [v for _,v in sorted(ans.items(), key = lambda item: item[0])] #O(nlogn)

        return answers[0] if answers else ''