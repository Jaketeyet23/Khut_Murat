# input integers A and B
A = int(input("Введите A: "))
B = int(input("Введите B: "))
 
# Calculate the count of numbers between A and B
count = B - A + 1
 
# Output the numbers and their count
print(f"The numbers between {A} and {B} are:")
for num in range(A, B + 1):
    print(num, end=" ")
print(f"\nTotal count of numbers: {count}")
