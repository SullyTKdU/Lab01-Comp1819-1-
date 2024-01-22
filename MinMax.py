def minmax(sequence):
  if not sequence:
      return None  # Return None for an empty sequence

  # Initialize min and max with the first element of the sequence
  min_val, max_val = sequence[0], sequence[0]

  # Iterate through the sequence to find the min and max values
  for num in sequence:
      if num < min_val:
          min_val = num
      if num > max_val:
          max_val = num

  # Return the result as a tuple
  return min_val, max_val

# Example usage:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = minmax(numbers)
print("Min and Max:", result)