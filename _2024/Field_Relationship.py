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
        r"\vec{E} = -\nabla V_e",
        font_size=100,
        color=WHITE
        )
        Formula[0][4:7].set_color(BLUE)
        self.add_foreground_mobject(Formula)
        Surrounding_Formula = SurroundingRectangle(
        Formula,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        N_1 = Tex("1")
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
        
        
        
