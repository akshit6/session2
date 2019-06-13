a = []
for i in range(9):
    a.append(" ")

b = range(1,10)
count = 0

p1 = input("Enter the name of player 1 :")
p2 = input("Enter the name of player 2 :")

def display(c):
    print("\n")
    print(c[0] , "|", c[1] , "|", c[2])
    print("--|---|--")
    print(c[3] , "|", c[4] , "|", c[5])
    print("--|---|--")
    print(c[6] , "|", c[7] , "|", c[8] , "\n")

def winner(a):
    if (a[0]==a[1]==a[2]=='x' or a[3]==a[4]==a[5]=='x' or a[6]==a[7]==a[8]=='x' or a[0]==a[3]==a[6]=='x' or a[1]==a[4]==a[7]=='x' or a[2]==a[5]==a[8]=='x' or a[0]==a[4]==a[8]=='x' or a[2]==a[4]==a[6]=='x'):
        print("CONGRATULATIONS!!! %s" %(p1))
        print("\nYOU won the game\n")
        exit()
    if (a[0]==a[1]==a[2]=='0' or a[3]==a[4]==a[5]=='0' or a[6]==a[7]==a[8]=='0' or a[0]==a[3]==a[6]=='0' or a[1]==a[4]==a[7]=='0' or a[2]==a[5]==a[8]=='0' or a[0]==a[4]==a[8]=='0' or a[2]==a[4]==a[6]=='0'):
        print("CONGRATULATIONS!!! %s" %(p2))
        print("\nYOU won the game\n")
        exit()

def player1(count):
    if count < 9:
        d = int(input("\n%s :  Enter the number : " %(p1)))
        if a[d - 1] == "x":
            print("You already have marked on %d position" % (d))
            print("PLease enter other number")
            player1(count)
        if a[d - 1] == "0":
            print("%s has already  marked on %d position" % (p2,d))
            print("PLease enter other number")
            player1(count)
        if a[d - 1] == " ":
            a[d - 1] = 'x'
            count += 1
        return count

def player2(count):
    if count<9:
        d = int(input("\n%s :  Enter the number : " %(p2)))
        if a[d - 1] == "0":
            print("You already have marked on %d position" % (d))
            print("PLease enter other number")
            player2(count)
        if a[d - 1] == "x":
            print("%s has already  marked on %d position" % (p1,d))
            print("PLease enter other number")
            player2(count)
        if a[d-1] == " ":
            a[d-1] = '0'
            count += 1
    return count

print("The numbering of boxes are as follows:")
display(b)
print("\n%s is: x \n%s is: 0\n" %(p1,p2))

print("Lets start the game!! \n")

display(a)

for i in range(5):
    count = player1(count)
    display(a)
    winner(a)

    if count == 9:
        print("\nThe game is TIED\n")
        break


    count = player2(count)
    display(a)
    winner(a)

    if count == 9:
        print("\nThe game is TIED\n")
        break
