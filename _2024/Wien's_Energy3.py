from manim import *
FRAME_X_RADIUS: int = 15
config.pixel_height = 1080 * 11
config.pixel_width = 1080 * 11
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height
config.background_color = "#141414"
class Wiens_Energy(Scene):
    def construct(self):
        Title = Tex(r"Wien's Energy Distribution$^{*}$",font_size=100).move_to(6.46*UP)
        Title_Line = Line(Title.get_left() + DOWN*0.8, Title.get_right() + DOWN*0.8, stroke_width=0.97)
        Second_Line = Line(LEFT, RIGHT, stroke_width=0.8)
        Second_Line.set_width(FRAME_X_RADIUS - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        Logo = MathTex(r"\left<\psi \right>\cdot  \left< \phi\right>").set_color(PURPLE_A).move_to(Second_Line.get_start()+[0.715,-0.4,0])
        
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
        
        Heading = Tex("Understanding the Formula: ")
        Heading.shift(2*LEFT+4*UP)
        Heading.scale(1.6)
        
        ex1 = Tex(r"$\cdot$ $\nu$: Frequency of radiation.")
        ex2 = Tex(r"$\cdot$ $T$: Temperature of the blackbody.}")
        ex3 = Tex(r"\parbox[t]{7.6cm}{$\cdot$ $h$, $c$, $k_B$: Planck’s constant, speed of light, and Boltzmann constant.}",
        tex_to_color_map={r"$h$": GREEN, r"$c$": YELLOW, r"$k_B$": BLUE, "Planck’s constant": GREEN, "speed of light": YELLOW, "Boltzmann constant": BLUE})
        ex4 = Tex(r"\parbox[t]{7.6cm}{$\cdot$ $e^{-{h \nu}/{k_B T}}$: The exponential factor shows that higher frequency photons are less likely at a given temperature.}")
        
        Explain = VGroup(ex1,ex2,ex3,ex4)
        Explain.scale(1.3)
        Explain.arrange(DOWN, aligned_edge=LEFT,buff=0.8)
        Explain.next_to(Heading,DOWN,buff=0.7)
        Explain.shift(2.5*RIGHT)
        self.add(
         Logo,
         Title, 
         Title_Line, 
         Second_Line, 
         Page_Number,
         Heading,
         Explain
         )
        
        
        