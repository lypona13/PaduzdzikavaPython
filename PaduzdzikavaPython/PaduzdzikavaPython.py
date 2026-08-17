#Task 1
print("Technical task for the traineeship QA Automation. Task 1")

# 1.1: If the entered number is greater than 7, then print "Hello"
number = int(input("Enter a number: "))

if number > 7:
    print("Hello")

# 1.2: If the entered name matches "John", then output "Hello, John", otherwise output "There is no such name"
name = input("Enter a name: ")

if name == "John":
    print("Hello, John")
else:
    print("There is no such name")

# 1.3: There is a numeric array at the input, output array elements that are multiples of 3
array = list(map(int, input("Enter numbers separated by spaces: ").split()))

for num in array:
    if num % 3 == 0:
        print(num)

#Task 2
print("Technical task for the traineeship QA Automation. Task 2")

print("Given bracket sequence: [((())()(())]]")
print("Can this sequence be considered correct?")

sequence = "[((())()(())]]"

def check(seq):
    stack = []
    pairs = {')': '(', ']': '['}

    for i, ch in enumerate(seq, start=1):
        if ch in "([":
            stack.append(ch)
        elif ch in ")]":
            if not stack or stack[-1] != pairs[ch]:
                return False, i
            stack.pop()
        else:
            return False, i

    if stack:
        return False, len(seq) + 1

    return True, None


answer, error_pos = check(sequence)
print("Correct?", answer)
print("First problem position:", error_pos)

#If the answer to the previous question is “no”, then what needs to be changed in it to make it correct? 
# Change the first of the two final ']' symbols to ')'

print ("What needs to be changed in it to make it correct?")

fixed = sequence[:-2] + ")" + sequence[-1]
print("Fixed sequence:", fixed)
print("Fixed correct?", check(fixed)[0])
