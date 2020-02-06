def compress(chars):
    write_idx = 0
    count = 1
    for i in range(1, len(chars) + 1):
        if i == len(chars) or chars[i] != chars[i - 1]: # new char found
			# write the character
            chars[write_idx] = chars[i - 1]
			# write the count
            if count > 1: # only write count if count is more than 1
                for digit in str(count):
                    write_idx += 1
                    chars[write_idx] = digit
            write_idx += 1 
            count = 1 # reset count to one as new character is found
        else: # same char found
            count += 1
    return len(chars[:write_idx])