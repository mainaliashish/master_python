def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you")
        fn()
        print("Have a good day.")
    return wrapper

@be_polite
def greet():
    print("My name is Ashish")

@be_polite
def rage():
    print("I hate you.")


# greet_me = be_polite(greet)
# polite_rage = be_polite(rage)

greet()
# rage()