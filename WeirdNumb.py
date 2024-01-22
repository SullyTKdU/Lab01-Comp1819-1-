def check_weirdness(n):
  if n % 2 == 1:
      print("Weird")
  elif 2 <= n <= 5 or n > 20:
      print("Not Weird")
  else:
      print("Weird")

# Input validation
while True:
  n = int(input("Enter a positive integer (1 <= n <= 100): "))
  if 1 <= n <= 100:
      break
  else:
      print("Invalid input. Please enter a number within the specified range.")

# Check weirdness
check_weirdness(n)
