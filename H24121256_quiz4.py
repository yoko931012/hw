sequence = input("Enter a sequence of numbers separated by whitespace : ")
sequence = sequence.split(" ")
for i in range(len(sequence)):
    n = sequence[i]
    sequence[i] = int(n)
print(sequence)
temp_LICS = [sequence[0]]
LICS = []

for element in sequence[1:]:
    if element > temp_LICS[-1]:
        temp_LICS.append(element)
    else:
        if len(temp_LICS) > len(LICS):
            LICS = temp_LICS
        temp_LICS = [element]
                    
if len(temp_LICS) > len(LICS):
    LICS = temp_LICS

print("The longest incraesing subsequence is: ", LICS)