from math import factorial

word = input("Enter the word : ").lower()
word_single = sorted("".join(dict.fromkeys(word)))

letters = []
rank = 1

for i in word:
    letters.append([[i],[word_single.index(i)+1,0,[]]])

counter = 0

for pair1 in letters:
    for pair2 in letters[counter:]:
        value1 = pair1[1]
        value2 = pair2[1]

        if value1[0] > value2[0]:
            value1[1] += 1

    counter += 1


counter = 0

for pair1 in letters:
    wordscounted = []
    for pair2 in letters[counter:]:
        if pair2[0][0] not in wordscounted:
            wordscounted.append(pair2[0][0])
            pair1[1][2].append(word.count(pair2[0][0], counter))

    counter += 1


for i, x in zip(letters, range(len(word)-1, -1, -1)):
    pair = i[1]
    numerator = pair[1] * factorial(x)
    denominator = 1 
    for j in pair[2]:
        denominator *= factorial(j)

    rank += numerator/denominator


print("Rank of '{}' is ".format(word.upper()), int(rank))
input()