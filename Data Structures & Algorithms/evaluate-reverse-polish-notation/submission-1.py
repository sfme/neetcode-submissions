import operator

class Solution:

   op_map = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
   }
      
   def evalRPN(self, tokens: List[str]) -> int:

      stack = []

      for elem in tokens:
         if elem not in self.op_map:
            stack.append(int(elem))

         else:
            _x1 = stack.pop()
            _x2 = stack.pop()

            _res = int(self.op_map[elem](_x2,_x1))
            stack.append(_res)

      return stack.pop()

        

        