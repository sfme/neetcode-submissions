class Solution:

    def encode(self, strs: List[str]) -> str:

        send_str = ""

        for elem_str in strs:
            size_str = len(elem_str)
            send_str += f"{str(size_str)}*{elem_str}"

        return send_str

    def decode(self, s: str) -> List[str]:

        str_len = len(s)
        cur_idx = 0
        last_idx = 0

        output = []

        while cur_idx < str_len:
            
            # find delimeter
            while s[cur_idx] != "*":
                cur_idx += 1

            size_sub_str = int(s[last_idx:cur_idx])

            # get string
            sub_str = s[(cur_idx+1): (cur_idx + 1 + size_sub_str)]
            output.append(sub_str)

            # update indexes
            cur_idx = cur_idx + 1 + size_sub_str
            last_idx = cur_idx
            
        return output 

            

                







        
