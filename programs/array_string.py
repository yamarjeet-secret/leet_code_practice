class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #sort the key based on start time
        intervals.sort(key=lambda interval:interval[0])
        merged = []
        for interval in intervals:
            # if nextststart time is greater then curent end time
            if not merged or merged[-1][1]<interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1],interval[1])]
        return merged
    
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        count=1
        ans = ""
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                count +=1
            else:
                ans += chars[i-1] + str(count) if count>1 else chars[i-1]
                count = 1
            
        ans += chars[-1] + str(count) if count>1 else chars[-1]
        #maintain in place 
        for ele in range(0,len(ans)):
            chars[ele]=ans[ele]
        return len(ans)