class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        temp=1
        totalProduct = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                totalProduct= totalProduct*nums[i]
            else:
                zero_count+=1
        for i in range(len(nums)):
            if zero_count>1:
                arr.append(0)
            elif zero_count==1:
                if nums[i]==0:
                    arr.append(int(totalProduct))
                else:
                    arr.append(0)
            else:
                temp = totalProduct/nums[i]
                arr.append(int(temp))
        
        
        return arr