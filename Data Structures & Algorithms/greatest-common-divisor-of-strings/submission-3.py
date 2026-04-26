class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            small = str1
            big = str2
        else:
            small = str2
            big = str1

        for l in range(len(small),0,-1):
            ans = small[:l]
            #valid substr if its lenght can cover both
            if len(small) % l !=0 or len(big) % l != 0:
                continue

            if ans * (len(small) // l) == small and ans * (len(big) // l) == big:
                return ans

        return ''
