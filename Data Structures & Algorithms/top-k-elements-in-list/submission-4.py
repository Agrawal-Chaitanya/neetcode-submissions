class Solution:
    from collections import Counter
    from typing import List

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Algo:
        1) Create counter (dict) of the given nums list
        2) Create list named 'bucket' with `len(nums) + 1` empty lists
        3) Populate the buckets list with the help of Counter in step #1. Item with freq 'f' will get appended to index 'f'
        4) Now, start for-loop from backwards on 'buckets' and append the respective num (from buckets) in an empty list named 'result'
        5) Once we get len(result) == k, return the result

        """

        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in counts.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result