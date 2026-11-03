class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            j=i+1
            k=n-1
            while(j<k):
                total= nums[i]+nums[j]+nums[k]

                if total < 0:
                    j +=1
                elif total > 0:
                    k -=1
                else:
                    nu=[nums[i],nums[j],nums[k]]
                    if nu not in num:
                        num.append(nu)
                    j +=1
                    k -=1

        return num