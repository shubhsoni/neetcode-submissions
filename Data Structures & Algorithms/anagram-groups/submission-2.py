class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        def sorted_char(w):
            return ''.join(sorted(w))
            
        for word in strs:
            ans[sorted_char(word)].append(word)

        return ans.values()