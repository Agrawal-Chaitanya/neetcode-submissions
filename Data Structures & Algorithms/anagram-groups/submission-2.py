class Solution:
    from collections import defaultdict
    from typing import List
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dt = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            dt[key].append(word)

        return list(dt.values())