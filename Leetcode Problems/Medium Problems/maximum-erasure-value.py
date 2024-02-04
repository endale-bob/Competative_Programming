class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=0
        maxl=0
        cur=0
        dic={}
        while end<len(nums):
            if nums[end] not in dic:
                dic[nums[end]]=-1
            if dic[nums[end]]==-1:
                dic[nums[end]]=end  #store index position!
                cur+=nums[end]
            elif dic[nums[end]]!=-1 :
                 #repetition found
                 if(cur>maxl):
                     maxl=cur
                 ist=start
                 start=dic[nums[end]]+1
                 for i in range(ist,dic[nums[end]]+1):

                     cur-=nums[i]
                     
                     dic[nums[i]]=-1
                 dic[nums[end]]=end
                 cur+=nums[end]
            end+=1
        if cur>maxl:
            maxl=cur
        return maxl