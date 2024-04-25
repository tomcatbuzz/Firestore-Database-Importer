import json
import random
import faker

# Initialize a Faker object
fake = faker.Faker()
#Define a function to generate only the 10 digit number
def generate_phone_number():
    phone_number = ''.join([str(random.randint(0,9)) for _ in range(10)])
    return phone_number
# Define a function to generate a random member
def generate_member():
    return {
        "id": str(random.randint(100, 999)),
        "lastName": fake.last_name(),
        "firstName": fake.first_name(),
        "email": fake.email(),
        "phoneNumber": generate_phone_number(),
    }

# Generate a list of random members
members = [generate_member() for _ in range(20)]

# Create a dictionary with the members list
data = {"members": members}

# Convert the dictionary to a JSON string
json_data = json.dumps(data, indent=2)

# Print the JSON string
print(json_data)

# If you want to write the JSON string to a file, comment or uncomment the following lines:
with open("random_data.json", "w") as file:
    file.write(json_data)

