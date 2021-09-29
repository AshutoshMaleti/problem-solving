class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={'{':'}','(':')','[':']'}
        p=-1
        
        for i in s:
            if stack == []:
                stack.append(i)
                p+=1
            else:
                try:
                    if dic[stack[p]] == i:
                        stack.pop()
                        p-=1
                    else:
                        stack.append(i)
                        p+=1
                except KeyError:
                    return False

        return True if stack==[] else False