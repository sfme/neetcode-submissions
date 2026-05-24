class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_strings = dict()

        for str_elem in strs:
            hash_map_chars = dict()

            for char_elem in str_elem:
                hash_map_chars[char_elem] = hash_map_chars.get(char_elem, 0) + 1

            # needed to make dict kerys immutable (sorted dict items, then tuple)
            dict_key = tuple(sorted(hash_map_chars.items()))

            if dict_key in hash_strings:
                hash_strings[dict_key].append(str_elem)
            else:
                hash_strings[dict_key] = [str_elem] 

        return list(hash_strings.values())


        