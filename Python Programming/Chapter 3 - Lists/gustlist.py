gustList = ['paul', 'john', 'stepthen']#3-4
print("Hi "+gustList[0].title() + ", I am inviting you on a dinner.\n"
      "Hi "+gustList[1].title() + ", I am inviting you on a dinner.\n"
      "Hi "+gustList[2].title() + ", I am inviting you on a dinner.\n" )

changingGustList = gustList.pop() #not coming the take him out of the list 
print(changingGustList.title() + " can't make it to the dinner.")

gustList.append('jack')

print("\nHi "+gustList[0].title() + ", just a reminder that dinner is on my table tonight.\n"
      "Hi "+gustList[1].title() + ", just a reminder that dinner is on my table tonight.\n"
      "Hi "+gustList[2].title() + ", just a reminder that dinner is on my table tonight.\n" )#3-5

print("Hi " + gustList[0].title() +","+ gustList[1].title() +" and " +gustList[2].title() + ", just found a bigger dinner table, so now more space is available. Thining of three more guests to invite to dinner.\n")



gustList.insert(0, 'adam')
gustList.insert(3, 'ali')
gustList.append('usman')


print("\nHi "+gustList[0].title() + ", just a reminder that dinner is on my table tonight. See you later.\n"
      "Hi "+gustList[1].title() + ", just a reminder that dinner is on my table tonight. See you later.\n"
      "Hi "+gustList[2].title() + ", just a reminder that dinner is on my table tonight. See you later.\n" 
      "Hi "+gustList[3].title() + ", just a reminder that dinner is on my table tonight. See you later.\n" 
      "Hi "+gustList[4].title() + ", just a reminder that dinner is on my table tonight. See you later.\n" 
      "Hi "+gustList[5].title() + ", just a reminder that dinner is on my table tonight. See you later.\n")#3-6


print("Hi " + gustList[0].title()+ ", "+gustList[1].title()+ ", "+gustList[2].title()+ ", "+gustList[3].title()+ ", "+gustList[4].title()+ " and "+gustList[5].title() +", just found out that new dinner table won’t arrive in time for the dinner, and you have space for only two guests.")

print("\nSorry " +gustList.pop().title() + ", I can only invite two people to the dinner due to the lack of space.")
print("Sorry " +gustList.pop().title() + ", I can only invite two people to the dinner due to the lack of space.")
print("Sorry " +gustList.pop().title() + ", I can only invite two people to the dinner due to the lack of space.")
print("Sorry " +gustList.pop().title() + ", I can only invite two people to the dinner due to the lack of space.\n")


print("\nHi "+gustList[0].title() + ", you are still invited.\n"
      "Hi "+gustList[1].title() + ", you are still invited.\n")#3-7

del gustList[1]
del gustList[0]

print(gustList)