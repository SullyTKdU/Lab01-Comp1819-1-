def check_lucky_id(target_id, file_path="lucky_ids.txt"):
  with open(file_path, "r") as f:
      for bannerId in f:
          if bannerId.strip() == target_id:
              return True
  return False

# Example usage:
your_banner_id = "001312934"  # Replace with your actual Banner ID
result = check_lucky_id(your_banner_id)

if result:
  print(f"Congratulations! Your Banner ID {your_banner_id} is lucky.")
else:
  print(f"Sorry, your Banner ID {your_banner_id} is not listed as lucky.")