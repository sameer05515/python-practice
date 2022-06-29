def print_flat_stars(count):
 for x in range(count):
  for y in range(count):
   print("*",end = "\t")
  print("")
  
def print_increasing_stars(count):
 for x in range(count):
  for y in range(x+1):
   print("*",end = "\t")
  print("")


def print_decreasing_stars(count):
 for x in range(count):
  for y in range(count-x):
   print("*",end = "\t")
  print("")

      
print_flat_stars(5)
print("-------------------")
print_increasing_stars(5)
print("-------------------")
print_decreasing_stars(5)