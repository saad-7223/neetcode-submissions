class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left_pt = 0
        right_pt = k
        max_window = []
        while right_pt <= len(nums):
            max_window.append(max(nums[left_pt:right_pt]))
            left_pt += 1
            right_pt += 1

        return max_window
