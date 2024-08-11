letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]
#1 Using list comprehension and zip, create a dictionary called letter_to_points that has the elements of letters as the keys and the elements of points as the values.
letter_to_points = {}
for keys, values in zip(letters,points):
  letter_to_points[keys] = values
#2 Add an element to the letter_to_points dictionary that has a key of " " and a point value of 0.
letter_to_points.update({" ": 0})
#3 Define a function called score_word that takes in a parameter word
def score_word(word):
  # 4 Inside score_word create a variable called point_total and set it to 0.
  point_total = 0
  
  #5 After defining point_total, create a for loop that goes through the letters in a word and adds the point value of each letter to point_total. You should get the point value from letter_to_points. If the letter you are checking for is not in letter_to_points, add 0 to the point_total.
  for key, value in letter_to_points.items():
    for letter in word:
      if letter == key:
        point_total += value
      elif letter != key:
        point_total += 0
# 6 After the loop is finished, return point_total        
  return point_total
#7 Test the function with BROWNIE 
brownie_points = "BROWNIE"
#8 Should return 15 points
#print(score_word(brownie_points))

# 9 Create a dictionary called player_to_words that maps players to a list of the words they have played. 

player_to_words = {
  "player1":["BLUE", "TENNIS", "EXIT"],
  "wordNerd":["EARTH", "EYES", "MACHINE"], 
  "Lexi Con":["ERASER", "BELLY", "HUSKY"],
  "Prof Reader":["ZAP", "COMA", "PERIOD"]
  }
#print(player_to_words)

#10 Create an empty dictionary called player_to_points
player_to_points = {}
#11 Iterate through the items in player_to_words. Call each player player and each list of words words.
for player, words in player_to_words.items():
  # within your loop, create a variable called player_points and set it to 0
  player_points = 0
  #12 Within the loop, create another loop that goes through each word in words and adds the value of score_word() with word as input. 
  for word in words:
    player_points += score_word(word)
    #13 After the inner loop ends, set the current player to be a key of player to points, with a value of player_points
    player_to_points.update({player : player_points})
    # 14 If you've calculated correctly, wordNerd should be winning by 1 point. 

print(player_to_points)