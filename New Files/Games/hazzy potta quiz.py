import time

print("Welcome to my hazzy potta quiz")
score = 0
answer = ""
try:
    print("\n"*3)
    answer = int(input("Question 1: How tall is Snape in fathoms? "))
    if answer == 67:
        score += 5
    print("The answer was 67 fathoms.")
        
    print("\n"*3)
    answer = input("Question 2: What is the name of the dog that appears for 7 frames (0.6 seconds) in the background of the extended cut of Prisoner of Azcaban? ").lower()
    if answer == "alberto rodriguez montecarlo bonjour bonjour frederique the 3rd":
        score += 5
    print("The answer was Alberto Rodriguez Montecarlo Bonjour Bonjour Frederique the 3rd.")
        
    print("\n"*3)
    answer = input("Question 3: What gender is Albus Dumbledore? ").lower()
    if answer == "dead":
        score += 5
    print("The answer was 'dead'.")
        
    print("\n"*3)
    answer = input("Question 4: What spell causes you to go instantly bankrupt? ").lower()
    if answer == "potentius hmrcus":
        score += 5
    print("The answer was Potentius HMRCus.")
        
    print("\n"*3)
    answer = int(input("Question 5: How many torch sconces are there around the entirety of the Hogwarts campus? "))
    if answer == 12446:
        score += 5
    print("The answer was 12,446.")
        
    print("\n"*3)
    answer = input("Question 6: What does IJUHGYF stand for? ").lower()
    if answer == "beef boullion":
        score += 5
    print("The answer was Beef Boullion.")
        
    print("\n"*3)
    answer = input("Question 7: How many bones would you break if you decided to complete martial combat with a centaur? ").lower()
    if answer == "all of them":
        score += 5
    print("The answer was 'all of them'.")
        
    print("\n"*3)
    answer = input("Question 8: In the blockbuster 2001 movie Legally Blonde, what is the chemical discovered to dissolve in the heat of a shower that is used in the prosecuted's perm? ").lower()
    if answer == "ammonium thioglycolate":
        score += 5
    print("The answer was Ammonium Thioglycolate.")
        
    print("\n"*3)
    answer = input("Question 9: True or False: The 1932 International Confederation of Wizards Supreme Mugwump Election took place in Eyrie, Bhutan. ").lower()
    if answer == "true":
        score += 5
    print("The answer was True.")
        
    print("\n"*3)
    answer = int(input("Question 10: What is the average caloric density of a Mad-Eye Moody series Chocolate Frog? "))
    if answer == 1230:
        score += 5
    print("The answer was 1230 calories.")

    print("\n"*3)
    answer = input("Question 11: Nicolas Flamel was French. Is that problematic? ").lower()
    if answer == "yes":
        score += 5
    print("The answer was 'Yes'.")
        
    print("\n"*3)
    answer = input("Question 12: What is the correct way to make a 3-dose Saradmon Brew in the hit MMORPG Runescape? ").lower()
    if answer == "mix cleaned toadflax with a crushed birdnest in a vial of water":
        score += 5
    print("The answer was 'Mix cleaned toadflax with a crushed birdnest in a vial of water'.")    

    print("\n"*3)
    answer = input("Question 13: Ents are magical beings inhabiting trees. What is their preferred wood type? ").lower()
    if answer == "adriatic hawthorn":
        score += 5
    print("The answer was Adriatic Hawthorn.")

    print("\n"*3)
    answer = input("Question 14: What Crayola colour is the closest to Hufflepuff's main motif? ").lower()
    if answer == "banana mania":
        score += 5
    print("The answer was Banana Mania.")

    print("\n"*3)
    answer = input("Question 15: Was Ron Weasley ever in ketosis? ").lower()
    if answer == "no":
        score += 5
    print("The answer was 'No'.")

    print("\n"*3)
    answer = input("Question 16: The core of the wand decides its properties and is unique to each owner. How is the core of an average Durmstrang students' wand often described as smelling? ").lower()
    if answer == "herbacious":
        score += 5
    print("The answer was 'Herbacious'.")

    print("\n"*3)
    answer = input("Question 17: What burns hotter: the Incendio spell or Naphthalene? ").lower()
    if answer == "naphthalene":
        score += 5
    print("The answer was Naphthalene.")

    print("\n"*3)
    answer = input("Question 18: True or False: Hermione Granger's Timeturner has the same ability as the stand 'The World', belonging to Dio Brando from the Japanese animated series 'JoJos Bizarre Adventure: Battle Tendency'. ").lower()
    if answer == "false":
        score += 5
    print("The answer was False.")

    print("\n"*3)
    answer = input("Question 19: One of the main ingredients in high-end perfumes is ambegris, which also exists in the Hazzy Potta universe. What effect does ambegris have on a Polyjuice Potion? ").lower()
    if answer == "death":
        score += 5
    print("The answer was 'Death'.")

    print("\n"*3)
    answer = input("Final question: Who was the HALF BLOOD PRINCE? ").lower()
    if answer == "orlando bloom":
        score += 20
    print("The answer was Orlando Bloom.")
except:
    print("You put in a silly answer so I'm skipping the rest of the question, you oaf.")

print("Quiz over! Let's work out which character you are based on your score! ")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
print("...")
time.sleep(2)
if score < 10:
    print("Your character is Makeup Artist 14.")
elif score < 20:
    print("You are Dobby (Pre-animation(tennis ball on stick)).")
elif score < 30:
    print("You are Grimbus the phoenix (not Albus').")
elif score < 40:
    print("You are Squickwink Thimblegrock the banker!")
elif score < 50:
    print("You are Anchovy Pete, renowned Hogwarts chef!")
elif score < 60:
    print("You are Lantovic Dyrzchownovak - winner of the Juniors' edition Tri Wizard Tournament!")
elif score < 70:
    print("You are Slimy Moody; Mad-Eye Moody covered in slime!")
elif score < 80:
    print("You are A Particularly Handsome Dog!")
elif score < 90:
    print("You are Polytonius Dewitt, inventor of the Jollyjuice Potion!")
elif score < 100:
    print("You are Galvinised Dumbledore - Albus' body after he had cast iron poured on him!")
elif score > 100:
    print("You are Parry Hotter! Daniel Radcliffe's insanely jacked brother. Well done!")
    
input("Press enter to cast the spell that closes the quiz lol")