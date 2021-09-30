class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        length=len(strs)
        ans=''
        smallest_string=min(strs, key=len)
        status=False
        
        if length>1:
            for j in range(len(smallest_string)):
                for i in range(length-1):
                    if strs[i][j]==strs[i+1][j]:
                        status=True
                    else:
                        status=False
                        break
                if status==True:
                    ans+=strs[i][j]
                else:
                    break
        else:
            return strs[0]
                
        return ans