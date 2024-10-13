from manim import *

config.pixel_height = 1080 * 4
config.pixel_width = 1080 * 4
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height
config.background_color = "#141414"
class Wiens_Energy(Scene):
    def construct(self):
        Title = Tex(r"Field-Potential Relationship$^{*}$",font_size=100).move_to(6.46*UP)
        Title_Line = Line(Title.get_left() + DOWN*0.8, Title.get_right() + DOWN*0.8, stroke_width=0.97)
        Second_Line = Line(LEFT, RIGHT, stroke_width=0.8)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        Logo = MathTex(r"\left<\psi \right>\cdot  \left< \phi\right>").set_color(PURPLE_A).move_to(Second_Line.get_start()+[0.715,-0.4,0])
        
        Formula = MathTex(
            r"V_e &= K_e \frac{Q}{r} \\",
            r"\frac{dV_e}{dr} &= -K_e \frac{Q}{r^2} \\",
            r"\nabla V &= \left( \frac{dV_e}{dr}, \frac{dV_e}{d\Theta} \right) \\",
            r"\nabla V_e &= -K_e \frac{Q}{r^2} \hat{u}_r \\",
            r"\vec{E} &= -\nabla V_e",
            font_size=56
             # Adjust font size if needed
        ).arrange(DOWN, buff=0.2)
        Formula.scale(1.257)
        Formula[0][0:3].set_color(BLUE)  # V_e in first equation
        Formula[1][1:3].set_color(BLUE)  # V_e in second equation
        Formula[2][5:7].set_color(BLUE)  # V_e in third equation
        Formula[2][12:15].set_color(BLUE)  # V_e in third equati
        Formula[3][1:3].set_color(BLUE)  # V_e in fourth equation
        Formula[4][5:8].set_color(BLUE)  # V_e in fifth equation
        
        
        self.add_foreground_mobject(Formula)
        Surrounding_Formula = SurroundingRectangle(
        Formula[-1],
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        N_1 = Tex("2")
        W_1 = N_1.get_width() + 0.1
        H_1 = N_1.get_height() + 0.2        
        radius = max(W_1, H_1) / 2.0        
        C = Circle(
            radius=radius,
            stroke_width=0.5,
            fill_color="#191919",
            stroke_color=WHITE,
            fill_opacity=1,
        )       
        N_1.move_to(C.get_center())
        Page_Number = VGroup(C, N_1)       
        Page_Number.to_edge(DOWN, buff=0.5)
        self.add(Logo, Title, Title_Line, Second_Line, Formula, Surrounding_Formula, Page_Number)
        
        
        