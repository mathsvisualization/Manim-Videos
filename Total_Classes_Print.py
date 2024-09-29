import custom 

# Get the list of methods in manim
method = dir(custom)

# Save the methods to a text file
with open("manim_methods.txt", "w") as file:
    file.write("\n".join(method))