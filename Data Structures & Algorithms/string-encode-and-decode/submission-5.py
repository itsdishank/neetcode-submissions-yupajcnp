class Solution:
    
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.
        Uses the format: length_of_string + '#' + actual_string
        """
        res = ""
        for s in strs:
            # Append length of string, delimiter '#', and the string itself
            res += str(len(s)) + "#" + s
            print(res)  # Debug print to show intermediate encoding
        return res

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single encoded string back into a list of strings.
        """
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Find the position of '#' to extract the length of the next string
            while s[j] != '#':
                j += 1
            length = int(s[i:j])  # Convert length from string to integer
            i = j + 1  # Move to the start of the actual string
            j = i + length  # Determine the end index of the string
            res.append(s[i:j])  # Extract and add the string to the result list
            i = j  # Move to the next encoded string
            
        return res
