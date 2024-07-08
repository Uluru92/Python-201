# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(example_list):
  maximun_list = max(example_list)
  minimun_list = min(example_list)
  average_list = sum(example_list)/len(example_list)
  print("Maximun number:",maximun_list)
  print("Minimum number:",minimun_list)
  print("Average number:",average_list)

# call the function below here

stats(example_list)