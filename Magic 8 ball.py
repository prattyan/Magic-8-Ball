#Magic 8 Ball
import random
def rep(str):
    print("Do you want to play again?  Y/N  ")
    user_2=input("Enter your opinion :")
    if user_2=="Y":
        ball(str)
    elif user_2=="N":
        print("Ended ..............  Good Byee..................")
def ball(str):
    outputs=["It is certain", "It is decidedly so", "Without a doubt","Yes - definitely",
         "You may rely on it", "As i see it, yes" ,"Most likely", "Outlook good", "Yes",
         "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now",
         "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no",
         "My sources say no", "Outlook not so good", "Very doubtful"]
    print("""Welcome to Magic 8 ball:
********************************************************************""")
    user=input("Enter your Name :")
    user_input2=input(user + ", Enter your question : ")
    print(random.choice(outputs))
    rep(str)
ball(str)


