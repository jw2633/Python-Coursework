#James Wang
#I210
#HW 4

s = 'abcdefghijklmnopqrstuvwxyz'

#4.13a
print(s[1:3] == 'bc')

#4.13b
print(s[0:14] == 'abcdefghijklmn')

#4.13c
print(s[14:28] == 'opqrstuvwxyz')

#4.13d
print(s[1:-1] == 'bcdefghijklmnopqrstuvwxy')

#4.16
#Requests three strings, print True if in dictionary order; otherwise nothing is printed.

def DictionaryOrder():
    three_words = [input("Enter first word: "),
                   input("Enter second word: "),
                   input("Enter thrid word: ")]
    three_words_sorted = sorted(three_words)
    if three_words == three_words_sorted:
        return True
    else:
        print()



#4.20
sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'
print("From: ",sender,
      "\nTo:",recipient,
      "\nSubject:",subject)

#4.23
def average():
    sentence = input("Enter a sentence: ")
    words_only = sentence.split()
    avg_len = sum(len(word) for word in words_only)/len(words_only)
    print(avg_len)

#4.25
def vowelCount(input):
    print('a,e,i,o and u appear, respectively, '+
          str(input.lower().count('a'))+"," +
          str(input.lower().count('e'))+"," +
          str(input.lower().count('i'))+"," +
          str(input.lower().count('o'))+"," +
          str(input.lower().count('u'))+" times.")

vowelCount("Le Tour de France.")


