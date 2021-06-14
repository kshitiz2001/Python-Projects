print("Welcome To My First Game")
name = input("Enter Your Name : ")
age = int(input("Enter Your Age : "))

health = 10
if age >= 10:
    print("You Are Old Enough To Play This Game")

    wants_to_play = input("Do You Want To Play This Game(yes/no)? : ").lower()
    if wants_to_play == "yes":
        print("You Are Starting With Health", health)
        print("Lets Play")

        left_or_right = input("First Choice...Left or Right(left/right)? : ").lower()
        if left_or_right == "left":
            ans = input(
                "Nice,You Follow The Path And Reach A Lake...Do You Want To Swim Across Or Go Around(across/around)? : ").lower()
            if ans == "around":
                print("You Went Around And Reached The Other Side Of Lake.")
                if health == 10:
                    print("You Have Now 10 health")
                else:
                    print("n")
            elif ans == "across":
                print("You Managed To Get Across, But Were Bit By A Snake And Lost 5 Health")
                health = health - 5
                if health <= 5:
                    print("You Have Now 5 Health Left")
                else:
                    print("o")
            ans = input("You Notice A House And A River. Where You Want To Go(house/river)? : ").lower()
            if ans == "river":
                print("You fell In The River And Died ")
                health = health - 5

                if health <= 0:
                    print("You Now Have Zero Health And You Lost The Game...")
                else:
                    print("You Have Survived...You Win!!!")
            elif ans == "house":
                print("You Go To The House And Greeted By The Owner ")
                if health <= 0:
                    print("You Now Have Zero Health And You Lost The Game...")
                else:
                    print("You Have Survived...You Win!!!")
        else:
            print("You Choose Wrong Way...You Loose")

    else:
        print("Cyaa...")

else:
    print("Sorry:( ,You Are Not Old Enough To Play This Game")
    
    
#     by kshitiz
