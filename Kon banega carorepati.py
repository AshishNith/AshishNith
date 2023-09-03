print("Welcome To Kaun Banega Carorepati\n")

score = 0
correct_answer = 0

Q1 = '''
Current Railway Minister of India is

A. Mamta Banarjee

B. Ram Vilash

C. Ashwini Vaishnaw

D. Piyush Goyal \n'''

print(Q1)
A1 = input("Enter the correct option")
if A1 == "C" or "c":
    score = score + 10000
    correct_answer = correct_answer +1

Q2 = '''

Which god is also known as ‘Gauri Nandan’?

A. Agni

B. Indra

C. Hanuman

D. Ganesha

'''
print(Q2)
A2 = input("Enter the correct option")
if A2 == "D" or "d":
    score = score + 10000
    correct_answer = correct_answer +1


Q3 = '''
What does not grow on tree according to a popular Hindi saying?

A. Money

B. Flowers

C. Leaves

D. Fruits

'''
print(Q3)
A3 = input("Enter the correct option")
if A3 == "A" or "a":
    score = score + 10000
    correct_answer = correct_answer +1


Q4 = '''When is the National Hindi Diwas celebrated?

A. 13 September

B. 14 September

C. 14 July

D. 15 August 

'''

print(Q4)
A4 = input("Enter the correct option")
if A4 == "B" or "b":
    score = score + 10000
    correct_answer = correct_answer +1


Q5 = '''Which Indian city hosts Indian movie industry?

A. Goa

B. Mumbai

C. Chennai

D. Calcutta

'''

print(Q5)
A5 = input("Enter the correct option")
if A5 == "B" or "b":
    score = score + 10000
    correct_answer = correct_answer +1


Q6 = ''' 
Who was the first Indian woman to win a medal in the Olympics?

A. P.T.Usha

B. Kunjarani Devi

C. Bachendri Pal

D. Karnam Maleshwari

'''

print(Q6)
A6 = input("Enter the correct option")
if A6 == "D" or "d":
    score = score + 10000
    correct_answer = correct_answer +1


Q7 = '''Who wrote Vande Mataram?

A. Sarat Chandra Chattopadhyay

B. Rabindranath Tagore

C. Bankim Chandra Chatterjee

D. Ishwar Chandra Vidyasagar

'''
print(Q7)
A7 = input("Enter the correct option")
if A7 == "D" or "d":
    score = score + 10000
    correct_answer = correct_answer +1

print('''You have completed the quiz''')
print(f"You gave total {correct_answer} correct answer out of 7 question")
print(f"Total price won by you is {score}")















