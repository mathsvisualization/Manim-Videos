import custom
import inspect

all_methods = dir(custom)

# Open a text file to write
with open("manim_classes.txt", "w") as file:
    for method in all_methods:
        # Get the object from the name
        obj = getattr(custom, method)
        
        # Check if the object is a class
        if inspect.isclass(obj):
            file.write(f"{method}\n")  # Write each class to the file

print("Classes saved to manim_classes.txt")