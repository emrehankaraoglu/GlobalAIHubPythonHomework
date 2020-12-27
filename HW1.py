input1 = input("Please enter your name :").upper()
input2 = input("What is your favourite city :").upper()
input3 = float(input("What is the pi number :"))
input4 = int(input("What is the year of Atatürk's death :"))
input5 = int(input("How much second occurs a minute :"))

print("the type of {} is {} \n"
      "the type of {} is {} \n"
      "the type of {} is {} \n"
      "the type of {} is {} \n"
      "the type of {} is {} \n".format(input1,type(input1),
                                      input2,type(input2),
                                      input3,type(input3),
                                      input4,type(input4),
                                      input5,type(input5)))

