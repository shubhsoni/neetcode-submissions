class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if len(str1) < len(str2):
        #     small = str1
        #     big = str2
        # else:
        #     small = str2
        #     big = str1

        for l in range( min(len(str1), len(str2)), 0, -1):
            ans = str1[:l]
            #valid substr if its lenght can cover both
            if len(str1) % l !=0 or len(str2) % l != 0:
                continue

            if ans * (len(str1) // l) == str1 and ans * (len(str2) // l) == str2:
                return ans

        return ''
