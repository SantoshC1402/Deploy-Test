#Beginner activity
    #Anagrams
from collections import Counter  # for character frequency counting

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):  # check length
    print("No")
else:
    if Counter(s1) == Counter(s2):  # compare character counts
        print("Yes")
    else:
        print("No")

      #Prime number or not
import math

n = 11
if n <= 1:
    print(False)
else:
    is_prime = True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(is_prime)

    # Most frequent element in a list
def most_frequent(List):
    return max(set(List), key=List.count)

List = [2, 1, 2, 2, 1, 3]
print(most_frequent(List))

#Task 1
def create_user(users, user_id, name, age, city):
    new_user = {"id": user_id, "name": name, "age": age, "city": city}
    users.append(new_user)
    return users
def read_users(users):
    return users
def update_user(users, user_id, new_name, new_age, new_city):
    for user in users:
        if user["id"] == user_id:
            user["name"] = new_name
            user["age"] = new_age
            user["city"] = new_city
            return users
    return None  # User not found
def delete_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return
    return None  # User not found
def get_user_by_id(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None
users = []
users = create_user(users, 1, "Alice", 30, "New York")
users = create_user(users, 2, "Bob", 25, "London")
users = create_user(users, 3, "Charlie", 35, "Paris")
print("All users:", read_users(users))
# Get a user by ID
user = get_user_by_id(users, 2)
if user:
    print("User with ID 2:", user)
else:
    print("User with ID 2 not found")
# Update a user
updated_users = update_user(users, 1, "Alice Smith", 31, "Los Angeles")
if updated_users:
    print("Updated users:", updated_users)
else:
    print("User with ID 1 not found")
# Delete a user
delete_user(users, 3)
print("Users after deleting user with ID 3:", read_users(users))

#Task 2

import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def is_valid_email(email):
    if(re.fullmatch(regex, email)):
        print("Valid Email: True")
    else:
        print("Invalid Email : False")
is_valid_email("user@domain.com")

#Task 3
import hashlib, uuid

def hash_password(password, salt=None):
    salt = salt or uuid.uuid4().bytes
    hashed_password = hashlib.sha256(salt + password.encode()).digest().hex()
    return hashed_password, salt.hex()

def register_user(users, username, password):
    if username in users: return False
    hashed_password, salt = hash_password(password)
    users[username] = {'hashed_password': hashed_password, 'salt': salt}
    return True

def login_user(users, username, password):
    if username not in users: return False
    stored_user_data = users[username]
    stored_hashed_password = stored_user_data['hashed_password']
    stored_salt = stored_user_data['salt']
    input_hashed_password, _ = hash_password(password, bytes.fromhex(stored_salt))
    return input_hashed_password == stored_hashed_password

def main():
    users = {}
    while True:
        choice = input("\n1. Register\n2. Login\n3. Quit\nChoice: ")
        if choice == '1':
            username, password = input("Username: "), input("Password: ")
            print("Registration " + ("successful!" if register_user(users, username, password) else "failed."))
        elif choice == '2':
            username, password = input("Username: "), input("Password: ")
            print("Login " + ("successful!" if login_user(users, username, password) else "failed."))
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
