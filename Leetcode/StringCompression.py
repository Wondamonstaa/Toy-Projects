class Solution:
    def compress(self, chars: List[str]) -> int:
        write = anchor = 0
        for read, char in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != char:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
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
