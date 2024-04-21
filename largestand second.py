def find_second_largest(numbers):
    # Initialize the largest and second largest numbers
    largest = second_largest = float('-inf')
    
    # Iterate through the list
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
            
    return second_largest

# Example usage:
numbers = [3, 5, 7, 2, 8, 5, 9]
print(find_second_largest(numbers))
