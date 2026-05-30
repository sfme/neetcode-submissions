
class Solution:

    def isValid(self, s: str) -> bool:
        stack_valid = []

        for elem in s:

            if elem in ["(", "{", "["]:
                stack_valid.append(elem) # push

            else:
                if not stack_valid: 
                    # prevent empty stack pop, likely close bracket not have pair!
                    return False

                top_stack = stack_valid.pop()

                if top_stack == "(":
                    if elem != ")":
                        return False

                elif top_stack == "{":
                    if elem != "}":
                        return False

                elif top_stack == "[":
                    if elem != "]":
                        return False

        return len(stack_valid) == 0






        
        