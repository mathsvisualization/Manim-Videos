from manim import *
import math

hD, vD = 0.75, 0.75 # this feels wrong
hOff, vOff = -4, -1.5

def fibLines(num):
    a, b = 0, 1
    i = 0

    while i < num:
        yield f"{a}+{b}={a+b}"
        a, b = b, a+b
        i += 1

bigFont = 89
smallFont = 55

def alignLines(eq, i):
    return eq.shift(RIGHT * hD * (i+hOff)).shift(DOWN * vD * (i+vOff))

class Fibonacci(Scene):
    def construct(self):
        # Start with title already on screen, and draw the defintition of the Fibonacci numbers
        title = Text("Fibonacci Numbers", font_size=bigFont).to_edge(UP)
        definition = MathTex(r"f_{0} = 0, \ f_{1} = 1, \ f_{n}=f_{n-1}+f_{n-2}", font_size=smallFont).next_to(title, DOWN)
        self.wait()
        self.play(Write(title))
        self.play(Write(definition))

        # Setup all our equations to be drawn
        eqs = []
        reducedEqs = []
        for i, eq in enumerate(fibLines(5)):
            eqs += alignLines(Tex(eq, font_size=smallFont), i)
            reducedEqs += alignLines(Tex(eq.split('=')[1], font_size=smallFont), i)
            print((alignLines(Tex(eq, font_size=smallFont), i)))

        # Draw all the equations on the screen to begin our Fibonacci introduction
        for eq in eqs:
            self.play(Write(eq))

        self.wait(1)

        # reduce from equations to the right hand size numbers
        reduceAnim = list(map(lambda i: Transform(eqs[i], reducedEqs[i]), range(len(eqs))))
        self.play(*reduceAnim)

        # align all our staggered numbers into one clean row
        alignAnim = list(map(lambda i: eqs[i+1].animate.align_to(eqs[0], UP), range(len(eqs)-1)))
        # add the numbers we lopped off the left, and an elipsis on the right
        p1 = Tex("1", font_size=smallFont).next_to(eqs[0], LEFT, buff=hD*2/3) # buff is not correct
        p0 = Tex("0", font_size=smallFont).next_to(p1, LEFT, buff=hD*2/3) # buff is not correct
        n1 = Tex("13", font_size=smallFont).next_to(eqs[-1], RIGHT, buff=hD*2/3).align_to(p0, UP)
        n2 = Tex("21", font_size=smallFont).next_to(n1, RIGHT, buff=hD*2/3).align_to(p0, UP)
        n3 = Tex("34", font_size=smallFont).next_to(n2, RIGHT, buff=hD*2/3).align_to(p0, UP)
        n4 = Tex("55", font_size=smallFont).next_to(n3, RIGHT, buff=hD*2/3).align_to(p0, UP)
        cdots = Tex(r"\ldots", font_size=smallFont).next_to(n4, RIGHT, buff=hD*2/3).align_to(p0, UP).shift(DOWN * 0.25) # This is also not correctly aligned
        eqs = [p0, p1] + eqs + [n1, n2, n3, n4]
        self.play(
            AnimationGroup(
                AnimationGroup(*alignAnim),
                AnimationGroup(Write(p0), Write(p1), Write(n1), Write(n2), Write(n3), Write(n4), Write(cdots)),
                lag_ratio=0.5
            )
        )
       
             
