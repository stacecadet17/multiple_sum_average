# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

def integer(num):
  if num >= 100:
    print ("That's a big number!")
  else:
    print ("that's a small number")

# ****************************************************************************
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."


def sentence(str):
    if len(str) > 50:
      print ("Thats a long sentence")
    else:
      print ("That's a short sentence")

# ****************************************************************************
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."


def list_length(list):
  if len(list) > 10:
    print ("big list!")
  else:
    print ("small list")

a = ["bunny", 4, 6, 1, "monkey", "tiger"]
list_length(a)
