import random
choices=["rock","paper","scissor"]
user=input("Pick rock ,paper or scissor:").lower()

com=random.choice(choices)

if user not in choices:
  print("Invalid,try again")
  exit()
print("Computer choses",com)


if user==com:
  print("It's a tie!!!")
elif user=="rock" and com=="scissor":
  print("You win :)")
elif user=="paper" and com=="rock":
  print("You win :)")
elif user=="scissor" and com=="paper":
  print("You win :)")
else:
  print("you lose :(")
  


