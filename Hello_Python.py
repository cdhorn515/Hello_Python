print("Hello Python!")
# end=' ' tells print not to end line with newline character
print("How old are you?", end=' ')
age = input()

print("How tall are you in inches?", end=' ')
height = input()

print("How much do you weigh?", end=' ')
weight = input()

print(f"You're {age} years old, {height} inches tall, and weigh {weight} pounds.")
