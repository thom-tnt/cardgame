credentials = { 'a': 'a', 'b': 'b', 'thom': 'homework' }

# print('here is the hash value for thom = %s' % hash('homework'))

def authenticate(id):
    player_valid = False
    player_username = ''
    while player_valid == False:
        print ("Input your account information:")
        player_username = input("Player %s what is your username: " % id)
        if player_username in credentials.keys():
            player_password = input("Password: ")
            print(player_password)
            if player_password == credentials.get(player_username):
                print ("Your account is valid")
                player_valid = True

            else:
                print ("Your password is invalid")

        else:
            print ("Your account is invalid")
    return player_username

# print(credentials.keys())
# print(credentials.get('a'))