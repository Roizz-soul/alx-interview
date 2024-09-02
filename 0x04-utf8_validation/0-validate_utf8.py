#!/usr/bin/python3
""" Module for utf8 validation """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    
    # Number of bytes in the current UTF-8 character
    num_bytes = 0
    
    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask >>= 1
            
            # For 1-byte characters (0xxxxxxx), no additional bytes are needed
            if num_bytes == 0:
                continue
            
            # UTF-8 character must be 2-4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this is a continuation byte, it must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        # Decrement the number of bytes to check
        num_bytes -= 1
    
    return num_bytes == 0
