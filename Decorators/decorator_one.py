def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper

@shout
def speak(name):
    return f"Hi, I am {name}"

x = speak("Ashish")
print(x)