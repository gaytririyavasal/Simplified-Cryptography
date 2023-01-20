#  File: Cipher.py

#  Description: This program is designed to encrypt and decrypt strings based off of a 2-D list that is a perfect square.

#  Student Name: Gaytri Riya Vasal

#  Course Name: CS 313E

#  Unique Number: 86439

#  Date Created: 6/6/2022

#  Date Last Modified: 6/8/2022

import sys
import math

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string

# The following function encrypts a string using a 2-D list.

def encrypt (strng):
  # Store the length of the string in L
  L = len(strng)

  # The minimum value of M is L
  M = L
  while (math.sqrt(M) != int(math.sqrt(M))):
  # If necessary, increment M until it is a square number
    M += 1  

  # Add the required number of asterisks to the end of the string
  for i in range(M - L):
    strng = strng + '*'

  # Create a K X K 2-D list filled with dashes, where K is the square root of M
  lst = [['-' for x in range(int(math.sqrt(M)))] for y in range(int(math.sqrt(M)))]

  # Instantiate and begin index of string at 0
  index = 0

  # For each column, replace the dashes with the characters in the string, going from the top to the bottom of the column
  # Begin at the last column
  for c in range(len(lst) - 1, -1, -1):
    for r in range(len(lst)):
      lst[r][c] = strng[index]
      index += 1

  # Read the 2-D list row by row from left to right, starting at the first row and ultimately storing the encrypted result in a new string
  incryptedstring = ''
  for r in range(len(lst)):
    for c in range(len(lst)):
      if lst[r][c] != '*':
        incryptedstring = incryptedstring + lst[r][c]

  # Return the encrypted string
  return incryptedstring

# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string

# The following function decrypts a string utilizing a 2-D list.

def decrypt (strng):
  # Store the length of the string in L
  L = len(strng)

  # The minimum value of M is L
  M = L
  while (math.sqrt(M) != int(math.sqrt(M))):
  # If necessary, increment M until it is a square number
    M += 1

  # Create a K X K 2-D list filled with dashes, where K is the square root of M
  paddedlist = [['-' for x in range(int(math.sqrt(M)))] for y in range(int(math.sqrt(M)))]

  # Determine the number of asterisks required
  asterisks = M - L

  # Instantiate list that will store asterisks
  lstasterisks = []
  # Append the required number of asterisks to the list
  for i in range(asterisks):
    lstasterisks.append('*')

  # Replace the dashes with the asterisks in the above list, starting at the bottom of each column
  # Begin at the first column
  for c in range(len(paddedlist)):
    for r in range(len(paddedlist) - 1, -1, -1):
      # Once there are no more asterisks left in the list, asterisks will stop being added to the padded list
      if lstasterisks != []:
         paddedlist[r][c] = lstasterisks.pop()

  # Instantiate and begin index of string at 0
  index = 0

  # Starting at the first row and going from left to right, replace every dash (thus keeping all asterisks) with the characters in the string
  for r in range(len(paddedlist)):
    for c in range(len(paddedlist)):
      if paddedlist[r][c] != '*':
        paddedlist[r][c] = strng[index]
        index += 1

  # Read the 2-D list, starting at the last column, traversing from the top to the bottom of each column, and storing every character (while omitting asterisks) in a new string
  decryptedstring = ''
  for c in range(len(paddedlist) - 1, -1, -1):
    for r in range(len(paddedlist)):
      if paddedlist[r][c] != '*':
        decryptedstring = decryptedstring + paddedlist[r][c]
        
  # Return the decrypted string
  return decryptedstring

def main():
  
  # Read the strings P and Q from standard input
  lines = sys.stdin.read()

  # Split the lines into a list, with string P as the first element and string Q as the second element
  lst = lines.split("\n")

  # Encrypt the string P and print
  print(encrypt(lst[0]))

  # Decrypt the string Q and print
  print(decrypt(lst[1]))
          
if __name__ == "__main__":
  main()
