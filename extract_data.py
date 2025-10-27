import os

token = os.getenv("TOKEN")
print(f"Token = ${token}")

if token=="1234":
    print("valid")
else:
    print("invalid")
