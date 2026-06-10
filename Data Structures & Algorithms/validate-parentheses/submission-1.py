class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in brackets:
                if len(stack) == 0:
                    return False
                if stack.pop() != brackets[c]:
                    return False
                else:
                    continue
            stack.append(c)
            
        if len(stack) != 0:
            return False
        
        return True