def colorize(text, color):
    colors = ('green', 'red', 'blue', 'white')
    if type(text) is not str:
        raise TypeError("Text must be an instance of string")
    if type(color) is not str:
        raise TypeError("Color must be an instance of string")
    if color.lower() not in colors:
        print(f"Available colors : {colors}")
        raise ValueError("Color is invalid color")
    print(f"Printed {text} in {color}.")

c = colorize("Hello", "gray")
