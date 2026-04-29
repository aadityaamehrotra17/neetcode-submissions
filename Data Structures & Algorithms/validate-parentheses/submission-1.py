class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', ']':'[', '}':'{'}
        store = []

        if len(s) % 2 == 1:
            return False

        for i in s:
            if i not in brackets:
                store.append(i)
            else:
                if not store or brackets[i] != store[-1]:
                    return False
                store.pop()

        return len(store) == 0
    '''
    LIFO - stack
    create empty stack
    traverse thru string
    if opening bracket encountered, push to stack
    else, check if stack top is matching bracket
    if not, return False
    else, pop stack and continue
    once all done, check if stack is empty
    '''