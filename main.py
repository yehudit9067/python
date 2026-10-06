#1
word = input("enter a word:")
num = int(len(word)/2)
i = 0
j = -1
while i < num:
    if word[i] != word[j]:
        print("the word is not polindrome!😒")
        break
    else:
        j -= 1
        i += 1
if i == num:
    print("the word is polindrome!😄")

#2
sen = input("enter a sentence:")
i = 0
count = 0
while i < len(sen):
    if sen[i] == " ":
        count += 1
    i = i + 1
print("the number of words is", count+1)

#3
sen = input("enter a sentence:")
i = 1
initial = sen[0]
while i < len(sen):
    if sen[i] == " ":
        if sen[i+1] != " ":
            initial += sen[i+1]
    i +=1
print("the initial word is", initial)
