import pyto

# Code here

def ok() -> None:
  print("Good Bye!")

alert = pyto.Alert.initWithTitle("Hello", message="Hello World!")
alert.addActionWithTitle("Ok", handler=ok)
alert.show()