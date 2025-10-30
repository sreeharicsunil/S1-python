word = str(input("Enter a string of word :"))
word_list = list(word)
word_set = set(word)
count_list=[]

for i in word_set:
    count = 0
    for j in word_list:
        if i == j:
            count += 1
    count_list.append(count)

for i in range(len(word_set)):
        print(f"{list(word_set)[i]} : {count_list[i]} ")