
# coding: utf-8

def reverse_bin(x):
  bin(x)
  str_x = str(bin(x))
  reverse_x = str_x[::-1]
  ans_bin = reverse_x[:len(reverse_x)-2]
  return int(ans_bin,2)

x = input("Please enter an integer:")
print("The binary reverse of {} is {}".format(x, reverse_bin(int(x))))
