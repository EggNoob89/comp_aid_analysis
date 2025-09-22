#Coding Problem 1.3
a = 21
previous_value = a/2
arel_error = 100

iteration = 1

while arel_error > 0.5:
    current_value = (previous_value + a/previous_value)/2
    arel_error = abs((current_value - previous_value)/current_value)*100
    previous_value = current_value
    iteration += 1

print(f"Square root of {a} is {round(current_value,3)}")
print(f"We found it on the {iteration}th iteration")
