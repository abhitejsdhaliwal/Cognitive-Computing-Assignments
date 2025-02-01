"""Q1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80]. i. WAP to add 200 and 300 to L. ii. iii. iv. WAP to remove 10 and 30 from L. WAP to sort L in ascending order. WAP to sort L in descending order."""
L = [10, 20, 30, 40, 50, 60, 70, 80]

L.append(200)
L.append(300)
print("After adding 200 and 300:", L)

L.remove(10)
L.remove(30)
print("After removing 10 and 30:", L)

L.sort()
print("Sorted in ascending order:", L)

L.sort(reverse=True)
print("Sorted in descending order:", L)

"""Q2 Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45) and perform the following operations using tuple functions: i. ii. iii. iv. Identify the highest score and its index in the tuple. Find the lowest score and count how many times it appears. Reverse the tuple and return it as a list. Check if a specific score ‘76’ (input by the user) is present in the tuple and print its first occurrence index, or a message saying it’s not present."""
scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)

highest_score = max(scores)
highest_index = scores.index(highest_score)
print(f"Highest score: {highest_score}, Index: {highest_index}")

lowest_score = min(scores)
lowest_count = scores.count(lowest_score)
print(f"Lowest score: {lowest_score}, Count: {lowest_count}")

reversed_scores = list(scores[::-1])
print(f"Reversed scores as a list: {reversed_scores}")

specific_score = 76
if specific_score in scores:
    first_occurrence_index = scores.index(specific_score)
    print(f"Score {specific_score} is present at index: {first_occurrence_index}")
else:
    print(f"Score {specific_score} is not present in the tuple.")

"""Q3.WAP to create a list of 100 random numbers between 100 and 900. Count and print the: i. ii. iii. All odd numbers All even numbers All prime numbers"""
import random

random_numbers = [random.randint(100, 900) for _ in range(100)]

odd_numbers = []
even_numbers = []
prime_numbers = []

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for number in random_numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    if is_prime(number):
        prime_numbers.append(number)


print("Odd numbers:", odd_numbers)
print("Count of odd numbers: ",len(odd_numbers))
print("Even numbers:", even_numbers)
print("Count of even numbers: ",len(even_numbers))
print("Prime numbers:", prime_numbers)
print("Count of prime numbers: ",len(prime_numbers))

"""Q4.Consider the following two sets, A and B, represen ng scores of two teams in mul ple matches. A = {34, 56, 78, 90} and B = {78, 45, 90, 23} WAP to perform the following opera ons using set func ons: i. Find the unique scores achieved by both teams (union of sets). ii. iii. iv. v. Iden fy the scores that are common to both teams (intersec on of sets). Find the scores that are exclusive to each team (symmetric difference). Check if the scores of team A are a subset of team B, and if team B's scores are a superset of team A. Remove a specific score 𝑋 (input by the user) from set A if it exists. If not, print a message saying it is not present."""
A = {34, 56, 78, 90}
B = {78, 45, 90, 23}

unique_scores = A.union(B)
print(f"Unique scores achieved by both teams (Union): {unique_scores}")

common_scores = A.intersection(B)
print(f"Scores common to both teams (Intersection): {common_scores}")

exclusive_scores = A.symmetric_difference(B)
print(f"Scores exclusive to each team (Symmetric Difference): {exclusive_scores}")

is_subset = A.issubset(B)
print(f"Are the scores of team A a subset of team B? {is_subset}")

is_superset = B.issuperset(A)
print(f"Are the scores of team B a superset of team A? {is_superset}")

X = int(input("Enter a score to remove from team A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from team A. Updated team A: {A}")
else:
    print(f"Score {X} is not present in team A.")

#Q5.Write a program to rename a key city to a location in the following dictionary.
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

old_key = "city"
new_key = "location"

if old_key in sample_dict:
    sample_dict[new_key] = sample_dict[old_key]
    del sample_dict[old_key]
    print(f"Renamed '{old_key}' to '{new_key}'.")
else:
    print(f"Key '{old_key}' not found in the dictionary.")

print("Updated dictionary:",sample_dict)