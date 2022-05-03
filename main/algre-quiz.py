from operator import truediv


score = 0
q1 = input("1. What is Larry's superhero name?\nA Minnesota Cuke\nB Larryboy\nC Supercuke\nD Green Larry")
a1 = "B"
q2 = input("2. What bible story does Veggietales portray in the Sweet Sweet Petunia in Duke and the Great Pie War episode?\nA Ruth and Boaz\nB Rahab and the spies\nC David and Goliath\nD Adam and Eve\nPlease, just type the letter and not the whole answer>>")
a2 = "A"
q3 = input("3. What is the name of the computer?\nA Asdf\nB Qwerty\nC Uiop\nD Ghjkl\nPlease, just type the letter and not the whole answer>>")
a3 = "B"
q4 = input("4. What type of vegetable is Petunia?\nA Radish\nB Broccoli\nC Rhubarb\nD Asparagus\nPlease, just type the letter and not the whole answer>>")
a4 = "C"
q5 = input("5. Who sang the song ‘Pizza Angel’?\nA Bob\nB Larry\nC Petunia\nD Pa Grape\nPlease, just type the letter and not the whole answer>>")
q6 = input("6. Who sang the song ‘Lance the Turtle’?\nA Bob\nB Larry\nC Petunia\nD Archibald\nPlease, just type the letter and not the whole answer>>")
q7 = input("7. Finish the sentence: “We are the pirates...”\nA who don’t do anything.\nB who sail the seven seas.\nC who are searching for the whale.\nD who crashed their ship.\nPlease, just type the letter and not the whole answer>>")
q8 = input("8. Who is the Supper Hero?\nA Archibald\nB Larry\nC Jerry\nD Jimmy\nPlease, just type the letter and not the whole answer>>")
q9 = input("9. Who played Jonah in Jonah: A Veggietales Movie?\nA Jerry\nB Bob\nC Pa Grape\nD Archibald\nPlease, just type the letter and not the whole answer>>")
q10 = input("10. Who is the very model of a modern major general?\nA Jerry\nB Bob\nC Pa Grape\nD Archibald\nPlease, just type the letter and not the whole answer>>")
q11 = input("11. Who played the angel in Gideon the Tuba Warrior?\nA Petunia\nB Pa Grape\nC Madame Blueberry\nD Archibald\nPlease, just type the letter and not the whole answer>>")
q12 = input("12. How did Toto (Junior) save the land of Woe in Lord of the Beans?\nA He tosses the bean into the dry well.\nB He fights off all the sporks.\nC He sells grape soda to all the people in town.\nD He wishes for eternal riches and gives a portion to each veggie in the land.\nPlease, just type the letter and not the whole answer>>")
QUESTIONS = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12]
ANSWERS = [a1, a2, a3, a4, ]

print("And now it's time for the veggietales quiz, the part of your day when you test your knowledge of veggietales(Not the reboot). Welcome.")
for i in range(QUESTIONS):
    #if i == :
    #    print()
    for j in range(ANSWERS):
        if i in j:
            print("Correct")