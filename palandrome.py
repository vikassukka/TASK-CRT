def can_form_palindrome(string):
    char_count = {}
    
    # Count the frequency of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Count the number of characters with odd frequency
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
    
    # If there is at most one character with odd frequency, return YES, otherwise return NO
    if odd_count <= 1:
        return "YES"
    else:
        return "NO"

# Example usage:
input_string = "aabbccdd"
print(can_form_palindrome(input_string))
