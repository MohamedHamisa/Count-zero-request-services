class Solution:
    def countServers(self, n, nums, x, QS):
        ev=[]
        for i in range(len(QS)):ev.append([QS[i]-x,QS[i],i])
        ev.sort()
        nums=sorted(nums,key=lambda b:b[1])
        ans=[0 for q in QS]
        l=0
        r=0
        m=0
        ss=Counter()
        while m<len(ev):
            while r<len(nums) and nums[r][1]<=ev[m][1]:
                ss[nums[r][0]]+=1
                r+=1
            while l<r and nums[l][1]<ev[m][0]:
                ss[nums[l][0]]-=1
                if ss[nums[l][0]]==0:del ss[nums[l][0]]
                l+=1
            ans[ev[m][2]]=n-len(ss)
            m+=1
        return ans
