import custom

# List of class names
class_names = []
# Open a text file to write
with open("manim_classes_attributes_methods.txt", "w") as file:
    # Create a list to hold the class information
    class_info = []

    # Create formatted information for each class
    class_info.append("\n\n".join(
    f"Attributes and methods in {class_name}:\n{getattr(custom, class_name, None) and dir(getattr(custom, class_name))}"
    for class_name in class_names if getattr(custom, class_name, None) is not None
))

    # Write all class information to the file
    file.write("\n\n".join(class_info) + "\n")

print("Attributes and methods of classes saved to manim_classes_attributes_methods.txt")