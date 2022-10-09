from ctypes import sizeof


file = open("cities.txt", "r");
cities =file.readlines();
for city in cities:
    if (city == "Delhi"):
        print("Crazy Python");
    else :
        print("No");
        
#Rock paper scissor game 
def check_win(player,computer):
  print ("You choose "+ player +"Computer choose "+computer)
  if player == computer :
    return "It is a tie"
  elif player == "Rock" :
    if computer == "Paper":
      return "Paper covers the rock"
    else:
      return "Scissors cant cut rock! so player wins"
  elif player == "Paper" :
    if computer == "Rock":
      return "Paper can covers the rock , player wins"
    else:
      return "Scissors can cut Paper! so computer wins "    
  elif player == "Scissors" :
    if computer == "Rock":
      return "Scissors cant cut rock "
    else:
      return "Scissors can cut paper "

message = check_win("Scissors","Rock")
print(message)            