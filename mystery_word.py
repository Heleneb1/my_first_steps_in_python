#Version après correction
player_life = 7
player_score = 0
mystery_word = "mystery"
player_word = "_" * len(mystery_word)

while player_life > 0 and mystery_word!= player_word:
    letter = input("Enter your letter: ")

    if len(letter) == 0:  # Si aucun mot n'est entré
        print("You did not enter a letter:")
        continue  # Redemande un mot sans passer à la suite

   

    # Comparer chaque lettre du mot entré avec le mot mystère
    if letter in mystery_word:
      for i in range(len(mystery_word)): 
           if mystery_word[i] == letter:
            player_word = player_word[:i] + letter + player_word[i + 1:]
    else:
            player_life-=1
    # Vérifier si le joueur a deviné le mot
    if player_word == mystery_word:
        player_score += 1
        print(f"You're win! player_score = {player_score}")
        break  # Le joueur a gagné, on sort de la boucle
    elif player_life == 0:
    # Si le mot n'est pas trouvé, diminuer la vie et afficher le score
    
        print(f"You're lose, player_life = {player_life}, player_score = {player_score}")
    else:
        print(f"You have {player_life} lives left.")
        print(f"Current word: {player_word}")

#Version avant correction effectuer sur codesandbox   

# player_life = 7
# player_score = 0
# mystery_word = "mystery"
# player_word = "_" * len(mystery_word)

# while player_life > 0:
#     word = input("Enter your word: ")

#     if len(word) == 0:  # Si aucun mot n'est entré
#         print("You did not enter a word.")
#         continue  # Redemande un mot sans passer à la suite

#     if len(word) < 7:  # Si le mot est trop petit
#         print("The word is too small.")
#         player_life -= 1
#         continue  # Redemande un mot sans passer à la suite

#     # Comparer chaque lettre du mot entré avec le mot mystère
#     for i in range(len(mystery_word)):
#         if word[i] == mystery_word[i]:
#             player_word = player_word[:i] + word[i] + player_word[i + 1:]
    
#     # Vérifier si le joueur a deviné le mot
#     if word == mystery_word:
#         player_score += 1
#         print(f"You're win! player_score = {player_score}")
#         break  # Le joueur a gagné, on sort de la boucle

#     # Si le mot n'est pas trouvé, diminuer la vie et afficher le score
#     player_life -= 1
#     print(f"You're lose, player_life = {player_life}, player_score = {player_score}")
