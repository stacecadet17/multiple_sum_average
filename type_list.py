my_list = [1, "hi", 3, 4, 5]

def typeabc(l):

  my_sum = 0 #initilaizes a variable to store added elements if they are integers
  my_string="" #initilaizes a string to push elements to if they are strings
  my_type ="" #initializes a variable to store a string we can print later that will denote the type
  print_me="" #variable that stores either the sum or the concatenated string(or both) we will want to print

  for ele in l:
    if (type(ele) is int or type(ele) is float): #determine if element type is an integer, if so, add to my_sum
      my_sum += ele
  elif (type(ele) is str): # determine if element type is string, if so, add to my_string
      my_string += ele

  if (my_sum > 0 and my_string == ""): #if we did add to the sum, but the string is empty, the list type will be integers
    my_type = "integer"
    print_me = str(my_sum)
  if (my_sum == 0 and my_string != ""): # if we did NOT add to the sum and the string is not empty, list type is string
    my_type = "string"
    print_me = my_string
  if (my_sum != 0 and my_string != ""): # if we did add to the sum anf string is also not empty, list type contains both
    my_type = "mixed"
    print_me = str(my_sum) + " " + my_string

  print ("this is a list type of" + " " + my_type)
  print print_me

typeabc(my_list)
