#Allison Banegas
#Peaks

dataset = [18,9,21,41,20,28,17,31,89,67,40,48]

print("Dataset: {dataset}")
print("-----------")


if dataset[0] > dataset[1]:
    print(f"peak detected: Value {dataset[0]} index 0")

for i in range(10):

    if dataset[1+i] > dataset[i] and dataset[1+i] > dataset[i+2]:
        print(f"peak detected: Value {dataset[1+i]} index {1+i}")

if dataset[11] > dataset[10]:
    print(f"Peak detected: Value {dataset[11]} at index 11")








