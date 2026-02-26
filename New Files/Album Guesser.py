album = ["look to windward",
         "emergence",
         "past self",
         "dangerous",
         "even in arcadia",
         "caramel",
         "provider",
         "damocles",
         "gethsemane",
         "infinite baths"]

score = 0

print("Try and guess every song from the album!")
for x in range(10):
    print("You have",score,"points.")
    guess = input("Enter song guess: ").lower()
    if guess in album:
        score = score + 1
        album.remove(guess)
        print("Correct!")
    else:
        print("Incorrect!")

print("You scored",score,"points.")
if score > 8:
    print("You're an album master!")
elif score > 5:
    print("You're an album adept!")
elif score > 2:
    print("You're an album novice!")
else:
    print("You're an album beginner!")