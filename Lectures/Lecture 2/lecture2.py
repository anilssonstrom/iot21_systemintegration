
import requests

response = requests.get('https://api.github.com/helloworld')

print(response.status_code)

if response.status_code == 200:
    print("Success!")
if response.status_code == 404:
    print("Not found!")

if response.status_code:
    print("Success!")
else:
    print("Error!")


class MyClass:
    def __init__(self, value: int = 0):
        self.value = value

    def __bool__(self):
        return self.value != 0


m = MyClass(5)
print(m.value)

if m:
    print("Value is set")
else:
    print("Value is not set")
