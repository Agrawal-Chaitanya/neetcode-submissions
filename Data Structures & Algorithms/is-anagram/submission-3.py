class Solution:
    from collections import Counter
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = Counter(s)
        c2 = Counter(t)

        if c1 == c2:
            return True
        else:
            return False

# class Solution:
#     from collections import Counter
#     def isAnagram(self, s: str, t: str) -> bool:
# # def isAnagram(s, t):
#         seen = []

#         for i in s:
#             if i in t:
#                 t.strip(i)
#             else:
#                 return False
#         return True