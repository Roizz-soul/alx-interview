#!/usr/bin/env python3
import sys

def print_stats(total_size, status_counts):
    """Prints the total file size and the count of status codes."""
    print(f"File size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def parse_line(line):
    """Parses a line and returns the status code and file size."""
    try:
        parts = line.split()
        if len(parts) < 7:
            return None, None
        
        # Extract status code and file size
        status_code = parts[-2]
        file_size = parts[-1]
        
        # Convert to integers
        status_code = int(status_code)
        file_size = int(file_size)
        
        return status_code, file_size
    except (ValueError, IndexError):
        return None, None

def main():
    """ Main function to call """
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)
            
            if status_code is not None and file_size is not None:
                total_size += file_size
                if status_code in status_counts:
                    status_counts[status_code] += 1
            
            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
