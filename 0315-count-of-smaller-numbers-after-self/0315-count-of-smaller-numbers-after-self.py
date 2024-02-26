class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) == 1:
                return nums

            left = merge_sort(nums[:len(nums)//2])
            right = merge_sort(nums[len(nums)//2:])
            return merge(left, right)


        def merge(left, right):
            nonlocal ans
            combined = []
            rightlessthanleft = 0
            i, j = 0, 0
            
            while i < len(left) and j < len(right):
                if right[j][0] < left[i][0]:
                    combined.append(right[j])
                    rightlessthanleft += 1
                    j += 1
                else:
                    combined.append(left[i])
                    ans[left[i][1]] += rightlessthanleft
                    i += 1
            
            while i < len(left):
                combined.append(left[i])
                ans[left[i][1]] += rightlessthanleft
                i += 1
        
            if j < len(right):
                combined += right[j:]
            
            return combined
        
        ans = [0] * len(nums)
        nums = [(n, i) for i, n in enumerate(nums)]
        merge_sort(nums)
        return ans