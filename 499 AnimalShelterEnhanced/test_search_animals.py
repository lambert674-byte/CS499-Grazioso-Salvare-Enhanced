
from CRUD_Python_Module import AnimalShelter

db = AnimalShelter()

# Test 1: Filter birds
birds = db.search_animals(
    {"Animal Type": "Bird"},
    limit=10
)

print("TEST 1 - Bird filtering")
print("Records returned:", len(birds))
print("All birds:", all(
    animal["Animal Type"] == "Bird"
    for animal in birds
))

# Test 2: Pagination
page1 = db.search_animals(
    {"Animal Type": "Bird"},
    limit=5,
    skip=0
)

page2 = db.search_animals(
    {"Animal Type": "Bird"},
    limit=5,
    skip=5
)

print("\nTEST 2 - Pagination")
print("Page 1:", len(page1))
print("Page 2:", len(page2))
print("Different pages:", page1 != page2)

# Test 3: Invalid filter
print("\nTEST 3 - Validation")

try:
    db.search_animals({"Invalid Field": "Test"})
    print("FAIL: Invalid field accepted")
except ValueError:
    print("PASS: Invalid field rejected")

db.client.close()
