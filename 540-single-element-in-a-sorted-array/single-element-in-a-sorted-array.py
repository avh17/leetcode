class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        while l<r:
            m = l+(r-l)//2
            isEven = (True if (r-m)%2==0 else False)
            if nums[m] == nums[m-1]: 
                if isEven: # there are odd number of elements on the left if we skip the duplicate of mid
                    r = m-2
                else:
                    l = m+1
            elif nums[m] == nums[m+1]:
                if isEven: # odd number of ele on the right if we skip duplicate of mid
                    l = m+2
                else:
                    r = m-1
            else:
                return nums[m]

        return nums[l]