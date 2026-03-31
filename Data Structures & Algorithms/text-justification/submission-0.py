class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        res, cur_line, num_of_letters = [], [], 0

        for word in words:
            if len(word) + num_of_letters + len(cur_line) > maxWidth:
                
                for i in range(maxWidth - num_of_letters):
                    cur_line[i%(len(cur_line)-1 or 1)] += " "

                res.append(''.join(cur_line))
                num_of_letters = 0
                cur_line = []
            num_of_letters += len(word)
            cur_line.append(word)
        last_line = ' '.join(cur_line) 
        res.append(last_line + (' '*(maxWidth - len(last_line))))

        return res