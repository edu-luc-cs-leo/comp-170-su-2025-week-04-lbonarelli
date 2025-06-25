
words = ['baseball', 'data', 'analytics', 'warehouses', 'products', 'picking'] #List of words to use
def longest_word(words: list[str]) -> str:
  longest = words[0] # Assume the first word is the longest to start with
  for word in words[1:]: # Loop through each word in the list except the first
    if len(word) > len(longest): #If the current word is longer than the assumed longest
      longest = word #Update the longest word
  return longest 
print("The longest word is:", longest_word(words)) # Display the final longest word

def shortest_word(words: list[str]) -> str:
  shortest = words[0] # Start by assuming the first word is the shortest
  for word in words[1:]: # Loop through the rest of the words
    if len(word) < len(shortest):  #If the current word is shorter than the assumed shortest
      shortest = word #Update the shortest word
  return shortest
print("The shortest word is:", shortest_word(words)) # Display the final shortest word

def odd_words(words: list[str]) -> list[str]:
  odd_words_list = [] #Initialize an empty list to store words with an odd number of characters
  for word in words: #Go through each word in the list
    if len(word) % 2 == 1: #Check if the word has an odd length (remainder 1 when divided by 2)
      odd_words_list.append(word) #Add it to the list if it has an odd number of characters
  return odd_words_list
odd = odd_words(words)
print("The list of odd words is:", odd) #Show the final list of odd-length words

def average_words(words: list[str]) -> list[str]: #Define a function that returns words close to the average length
  total_length = 0 # Initialize total character count to 0
  for word in words:
    total_length += len(word) # Add the number of characters in each word to the total
  average = total_length / len(words) # Calculate the average length of all words
  result_average = [] # Create an empty list to store words close to the average length
  for word in words:
    if abs(len(word) - average) <= 1: # Check if the word’s length is within ±1 of the average
      result_average.append(word) # If it is, add it to the result list

  return result_average # Return the list of words that are close to average length
avg_words = average_words(words) # Call the function and store the result in avg_words

print("Words with averages within _+1 of the avg:", avg_words) # Print the final list of near-average-length words

foo = ["what", "how", "just", "when"]
bar = ["why", "whatever", "just", "people"]
def intersect(foo: list[str], bar: list[str]) -> bool:
  for word in foo: # Look at each word in the first list
      if word in bar: # See if that word also exists in the second list
        return True # If it does, return True right away
  return False # If we finish the loop and found no match, return False

print("Do the lists intersect:", intersect(foo, bar)) # Print out whether the two lists have any word in common

#Reflection: After doing this assignment for week 5, I was able to understand better the class material even though I had my doubts that I outlined in the email I sent you after I didn't turn in last week's assingment. I did try my best but I think I never hit the committ button o maybe that's why in the organizations tab in my Github profile it is not visible. Like I mentioned, I have never been very good at coding but as I slowly read and go back to what I am doing wrong I have been able to understand better. With this week's assingment I think I did a whole lot better and was able to problem solve a lot of errors I was getting and that's why I also added my # comments in certain lines. I am excited to see what comes next. 
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# Basic testing. This block validates the logic of the code. Additional 
# requirements such as single return statements are not tested here but 
# must be met anyway.
if __name__ == "__main__":
  testA = ["a", "list", "of", "nearly", "random", "words", "and", "strings"]
  testB = []
  testC = ["a", "be", "cat", "door", 
           "eagle", "galaxy", "forests", "harvests", 
           "important", "journalist"]
  testD = ["Frodo", "Gandalf", "Gollum", "Legolas", "Aragorn", "Rivendell"]
  testE = ["Saruman", "Boromir", "Faramir", "Sauron", "Gollum", "Minas Tirith"]
  testF = None

  # -------- Testing
  print("\nTesting shortest_word")
  if shortest_word(testF) is not None:
    print("shortest_word FAILS null test")
  else:
    print("shortest_word passes null test")

  if shortest_word(testB) is not None:
    print("shortest_word FAILS empty test")
  else:
    print("shortest_word passes empty test")

  if shortest_word(testA) is not testA[0]:
    print("shortest_word FAILS length test")
  else:
    print("shortest_word passes length test")

  # -------- Testing
  print("\nTesting longest_word")
  if longest_word(testF) is not None:
    print("longest_word FAILS null test")
  else:
    print("longest_word passes null test")

  if longest_word(testB) is not None:
    print("longest_word FAILS empty test")
  else:
    print("longest_word passes empty test")

  if longest_word(testA) is not testA[len(testA)-1]:
    print("longest_word FAILS length test")
  else:
    print("longest_word passes length test")
  
  # -------- Testing
  print("\nTesting odd_words")
  if odd_words(testF) is not None:
    print("odd_words FAILS null test")
  else:
    print("odd_words passes null test")
  
  if odd_words(testB) is not None:
    print("odd_words FAILS empty test")
  else:
    print("odd_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if odd_words(testC) != odd_test:
    print("odd_words FAIlS logic test")
  else:
    print("odd words passes logic test")

  # -------- Testing
  print("\nTesting average_words")
  if average_words(testF) is not None:
    print("average_words FAILS null test")
  else:
    print("average_words passes null test")
  
  if average_words(testB) is not None:
    print("average_words FAILS empty test")
  else:
    print("average_words passes empty test")

  odd_test = [testC[i] for i in range(0, len(testC), 2)]
  if average_words(testC) != ['eagle', 'galaxy']:
    print("average_words FAILS logic test")
  else:
    print("average_words words passes logic test")

  # -------- Testing
  print("\nTesting intesect")
  if intersect(testF, testA):
    print("intersect FAILS first null test")
  else:
    print("intersect passes first null test")

  if intersect(testA, testF):
    print("intersect FAILS second null test")
  else:
    print("intersect passes second null test")
  
  if intersect(testB, testA):
    print("intersect FAILS first empty test")
  else:
    print("intersect passes first empty test")

  if intersect(testA, testB):
    print("intersect FAILS second empty test")
  else:
    print("intersect passes second empty test")

  if not intersect(testD, testE):
    print("intersect FAILS logic test for true")
  else:
    print("intersect words passes logic test for true")
  
  if intersect(testA, testE):
    print("intersect FAILS logic test for false")
  else:
    print("intersect words passes logic test for false")
