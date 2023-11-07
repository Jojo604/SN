"""
namn = "joel"
nummer = 5

nummer2 = 4

nummer3 = nummer + nummer2

print("hej")

nummer = input()
nummer2 = input()

print(int(nummer) + int(nummer2))
"""

nummer = int(input())

if nummer < 10:
    print("numret är mindre än 10")

if nummer > 10:
    print("numret är större än 10")

if nummer == 10:
    print("numret är 10")

if nummer < 10:
    print("numret är mindre än 10")
elif nummer > 10:
    print("numret är större än 10")
else:
    print("numret är 10")
