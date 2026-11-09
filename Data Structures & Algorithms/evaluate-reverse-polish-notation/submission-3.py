class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # maintain a queue
        # walk tokens
        # once we find an operation do that on the stack, clear the queue
        ops = ['+','-','*','/']
        stack = [] 
        for tok in tokens:  
            if tok in ops:
                s, f = stack.pop(), stack.pop()
                match tok:
                    case '+':
                        temp = f + s
                    case '-':
                        temp = f - s
                    case '*':
                        temp = f * s
                    case '/':
                        temp = int(f/s)
                stack.append(temp)
            else:
                stack.append(int(tok))
        return stack[0]
