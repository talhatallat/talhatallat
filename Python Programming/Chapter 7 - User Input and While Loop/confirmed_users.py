# Moving Items from One List to Another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace'] # list
confirmed_users = [] # empty list
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.➋ 
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # takes one at a time from the end of the list 
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    # Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
        print(confirmed_user.title())
