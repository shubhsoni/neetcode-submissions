class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force
        #search entire spece- for every string check all other string if anagram
        #maintain a global set to avoid relooking at previously seen string- but does not improve timecomplexity
        # O(N2)

        #better - anagram can be checked in O(N) by counting same characters using dict
        #perform this on sorted list
        # O( M * NlogN )

        #better - without sorting
        #assumption all small letters
        keys_ref = {chr(k):0 for k in range(ord('a'),ord('z')+1)}
        ans = defaultdict(list)
       
        for string in strs:
            keys = keys_ref.copy()
            for s in string:
                keys[s] += 1
            # Convert character counts to a hashable tuple of values to use as a dictionary key
            ans[tuple(keys.values())].append(string)
        return list(v for _,v in ans.items())
