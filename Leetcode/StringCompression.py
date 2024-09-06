class Solution:
    def compress(self, chars: List[str]) -> int:
        
        #write = anchor = 0
        write = 0
        anchor = 0

        #O(N)
        for cur_idx, char in enumerate(chars):

            #O(1)
            if cur_idx + 1 == len(chars) or chars[cur_idx + 1] != char:
                ''' 
                The character at the anchor index 
                (which is the start of the sequence) is written to the write position in the array.
                The write pointer is then incremented to the next position.
                '''
                #O(1)
                chars[write] = chars[anchor]
                write += 1

                #O(1)
                if cur_idx > anchor:
                    #O(log10(n)) -> ~O(N)
                    for digit in str(cur_idx - anchor + 1):
                        #O(1) 
                        chars[write] = digit
                        write += 1
                anchor = cur_idx + 1

        #Time complexity: O(N) = 2*O(N) + 4*O(1) = 2*O(N) = ~O(N)
        #Space complexity: O(1) since the algorithm uses a constant amount of extra space regardless of the size of the input chars array.
        return write



class Solution:
    def compress(self, chars: List[str]) -> int:
        
        write_index = 0
        read_index = 0
        n = len(chars)

        while read_index < n:
            current_char = chars[read_index]
            count = 0

            # Count the occurrences of the current character
            while read_index < n and chars[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character
            chars[write_index] = current_char
            write_index += 1

            # Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index
