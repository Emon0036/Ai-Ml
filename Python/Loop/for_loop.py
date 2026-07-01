# count how many times the i occurs on that word
word = "Artificial intelegence"

# count = 0

# for i in word:
#     if(i == 'i'):
#         count +=1;

# print("Count of i=",count);

# count = 0
# for i in range(10): just like that for(int i=0 ; i<10 ; i++)
#     if(word[i] == 'i'):
#         count +=1;

# print("Count of i=",count)


for ch in word:
    if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        print(ch)
