from manim import *

# Configure scene settings
config.background_color = "#141414"
config.pixel_height = 1080
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class PotentialEnergy1(Scene):
    def construct(self):
        Title = Tex(r"Potential Energy in Quantum Mechanics",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B) 
        self.add_foreground_mobject(Formula)
        
        Surrounding_Formula = SurroundingRectangle(
        Formula,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.8
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
        self.add(Logo, Title, Second_Line, Formula, Surrounding_Formula, Page_Number, v_line)
        
class PotentialEnergy2(Scene):
    def construct(self):
        Title = Tex(r"Understanding Potential Energy",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B)
        Formula.next_to(Title, DOWN, buff=1)
        self.add_foreground_mobject(Formula)
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
        
        sur_for = SurroundingRectangle(
        Formula[0][0:3],
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=PURE_GREEN,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        Formula[0][3:].set_opacity(0.5)
        for_tex = Tex(
            r"""
            \parbox[t]{6cm}{This is the \textbf{expectation} value of the potential energy, which gives us the average value of the potential energy of the particle..
            }""", tex_to_color_map={r"\textbf{expectation}": PURE_GREEN}, font_size=72).shift(1*DOWN)
        
        sur_tex = SurroundingRectangle(
        for_tex,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_tex = DashedLine(sur_for.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        self.add(
                 Logo, 
                 Title, 
                 Second_Line,
                 Formula, 
                 Page_Number,
                 v_line,
                 sur_for,
                 sur_tex,
                 for_tex,
                 dash_tex
             )
             
class PotentialEnergy3(Scene):
    def construct(self):
        Title = Tex(r"Understanding Potential Energy",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B)
        Formula.next_to(Title, DOWN, buff=1) 
        self.add_foreground_mobject(Formula)
        N_1 = Tex("3")
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
        Formula[0][:3].set_opacity(0.5)
        Formula[0][5:-2].set_opacity(0.5)
        sur_for = SurroundingRectangle(
        Formula[0][4],
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
        sur_for2 = SurroundingRectangle(
        Formula[0][16:],
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        sur_for2.move_to([5.268, 4, 0])
        for_tex = Tex(
            r"""
            \parbox[t]{6cm}{
             This \textbf{integration} occurs in position space, which occurs across all possible positions of the particle.
            }""", font_size=72).shift(1*DOWN)
        
        sur_tex = SurroundingRectangle(
        for_tex,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_tex = DashedLine(sur_for.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        dash_tex2 = DashedLine(sur_for2.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        self.add(
                 Logo, 
                 Title, 
                 Second_Line,
                 Formula, 
                 Page_Number,
                 v_line,
                 sur_for,
                 sur_for2,
                 sur_tex,
                 for_tex,
                 dash_tex,
                 dash_tex2
             )
             
class PotentialEnergy4(Scene):
    def construct(self):
        Title = Tex(r"Understanding Potential Energy",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B)
        Formula[0][:5].set_opacity(0.5)
        Formula[0][10:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)
        self.add_foreground_mobject(Formula)
        N_1 = Tex("4")
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
        sur_for = SurroundingRectangle(
        Formula[0][5:10],
        buff=0.10,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )     
        for_tex = Tex(
            r"""
            \parbox[t]{6cm}{
             This is the $\psi(x)$ \textbf{complex conjugate} of. In quantum mechanics, we use the complex conjugate of wave functions to calculate probability distributions and expectation values.
            }""", font_size=72, tex_to_color_map={"$\psi(x)$": YELLOW_D, "wave functions": YELLOW_D}).shift(1*DOWN)
        
        sur_tex = SurroundingRectangle(
        for_tex,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_tex = DashedLine(sur_for.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        
        self.add(
                 Logo, 
                 Title, 
                 Second_Line,
                 Formula, 
                 Page_Number,
                 v_line,
                 sur_for,
                 sur_tex,
                 for_tex,
                 dash_tex             
             )
             
class PotentialEnergy5(Scene):
    def construct(self):
        Title = Tex(r"Understanding Potential Energy",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B)
        Formula[0][:10].set_opacity(0.5)
        Formula[0][12:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)
        self.add_foreground_mobject(Formula)
        N_1 = Tex("5")
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
        sur_for = SurroundingRectangle(
        Formula[0][10:12],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=TEAL_B,
        fill_opacity=0.1,
        stroke_width=0.8
        )    
        for_tex = Tex(
            r"""
            \parbox[t]{6cm}{
             This is \textbf{potential energy} operator. This operator represents the function of potential energy applied to the particle.
            }""", font_size=72, tex_to_color_map={"potential energy": TEAL_B}).shift(1*DOWN)
        
        sur_tex = SurroundingRectangle(
        for_tex,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_tex = DashedLine(sur_for.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        
        self.add(
                 Logo, 
                 Title, 
                 Second_Line,
                 Formula, 
                 Page_Number,
                 v_line,
                 sur_for,
                 sur_tex,
                 for_tex,
                 dash_tex            
             )
             
class PotentialEnergy6(Scene):
    def construct(self):
        Title = Tex(r"Understanding Potential Energy",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        Formula = Tex(
        r"$\langle V \rangle = \displaystyle\int \psi^*(x) \hat{V} \psi(x) \, dx$",
        font_size=100,
        color=WHITE
        )
        Formula[0][1].set_color(PURE_GREEN)
        Formula[0][12:16].set_color(YELLOW_D)
        Formula[0][10:12].set_color(TEAL_B)
        Formula[0][:12].set_opacity(0.5)
        Formula[0][16:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)
        self.add_foreground_mobject(Formula)
        N_1 = Tex("6")
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
        sur_for = SurroundingRectangle(
        Formula[0][12:16],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=YELLOW_D,
        fill_opacity=0.1,
        stroke_width=0.8
        )   
        for_tex = Tex(
            r"""
            \parbox[t]{6cm}{
             This is the wave function of the particle. \textbf{Wave function} $\psi(x)$ gives us a probability distribution which tells us what are the chances of a particle being at a given position..
            }""", font_size=72, tex_to_color_map={"Wave function": YELLOW_D, r"$\psi(x)$": YELLOW_D, "wave function": YELLOW_D}).shift(1*DOWN)
        
        sur_tex = SurroundingRectangle(
        for_tex,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_tex = DashedLine(sur_for.get_bottom(), sur_tex.get_top(), dash_length=0.15)
        
        
        self.add(
                 Logo, 
                 Title, 
                 Second_Line,
                 Formula, 
                 Page_Number,
                 v_line,
                 sur_for,
                 sur_tex,
                 for_tex,
                 dash_tex           
             )
             
class PotentialEnergy7(Scene):
    def construct(self):
        Title = Tex(r"Physical Interpretation",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        N_1 = Tex("7")
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
        
        Explain = Tex(
            r"""
            \parbox[t]{6.2cm}{
             The meaning of this formula is that when we find the expectation value of potential energy in any quantum state $\psi(x)$ , we are calculating what will be the average value of the potential energy of the particle if that particle is measured repeatedly in that quantum state.
            }""", font_size=72, tex_to_color_map={r"$\psi(x)$": YELLOW_D})
        sur_exp = SurroundingRectangle(
        Explain,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        self.add(
                 Logo,
                 Title,
                 Second_Line,
                 Page_Number,
                 v_line,
                 sur_exp,
                 Explain
             )
             
class PotentialEnergy8(Scene):
    def construct(self):
        Title = Tex(r"Understanding Expectation Values",font_size=100).move_to(6.46*UP)
        Title.shift(RIGHT*0.3)
        Title.set_width(config.frame_width - 4)
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height()+0.091)
        v_line.shift(0.1*DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        Logo = MathTex(r"\left< \phi\right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        N_1 = Tex("8")
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
        
        Explain = Tex(
            r"""
            \parbox[t]{6.2cm}{
             In quantum mechanics, the exact position or energy of a particle is often uncertain. Instead of pinpointing an exact value, physicists use the concept of an expectation value, which provides the average result of a measurement taken many times. This expectation value helps in predicting a particle’s behavior over multiple observations, giving insight into its probable properties.
            }""", font_size=72)
        sur_exp = SurroundingRectangle(
        Explain,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        self.add(
                 Logo,
                 Title,
                 Second_Line,
                 Page_Number,
                 v_line,
                 sur_exp,
                 Explain
             )
             
class PotentialEnergy9(Scene):
    def construct(self):
        # Title and decorative elements
        Title = Tex(r"Potential Energy Curve with Energy Limit", font_size=100).move_to(6.46 * UP)
        Title.shift(RIGHT * 0.3)
        Title.set_width(config.frame_width - 4)
        
        Second_Line = Line(LEFT, RIGHT, stroke_width=1.1)
        Second_Line.set_width(15 - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        
        v_line = Line(UP, DOWN, stroke_width=0.98)
        v_line.set_height(Title.get_height() + 0.091)
        v_line.shift(0.1 * DOWN)
        v_line.next_to(Title, LEFT, buff=0.5)
        
        Logo= MathTex(r"\left< \phi \right>").set_color(PURPLE_A)
        Logo.next_to(v_line, LEFT, buff=0.5)
        
        N_1 = Tex("9")
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

        # Axes and labels
        axes = Axes(
            x_range=[0, 3, 1],  
            y_range=[0, 5, 1],  
            x_length=8,
            y_length=5,
            axis_config={"color": WHITE, "include_ticks": False}
        )
        
        # Position x_label and y_label precisely near axes
        x_label = axes.get_x_axis_label("x").next_to(axes.x_axis.get_end(), UR, buff=0.2)
        y_label = axes.get_y_axis_label("V(x)").next_to(axes.y_axis.get_top(), RIGHT+UP, buff=0.1)
        axes.shift(2.8 * LEFT + 3 * DOWN)
        x_label.shift(2.8 * LEFT + 3 * DOWN)
        y_label.shift(2.8 * LEFT + 3 * DOWN)

        # Potential energy function and curve
        def potential_energy(x):
            return 0.5 * x**2

        curve = axes.plot(potential_energy, color=BLUE).set_stroke(WHITE, 1)

        # Shaded area under curve
        area = axes.get_area(curve, x_range=[0, 2.7], color=PURPLE_C, opacity=0.30)

        # Energy level text adjustment
        energy_text = MathTex("E", font_size=56).move_to(axes.c2p(0.5, 3.2)).shift(LEFT * 0.2 + UP * 0.3)
        explanation = Tex("Shaded region: Allowed oscillation range", font_size=44).next_to(area, DOWN, aligned_edge=LEFT)

        # Create dashed grid
        grid = VGroup()
        for x in range(0, 4):
            grid.add(DashedLine(start=axes.c2p(x, 0), end=axes.c2p(x, 5), color=WHITE))
        for y in range(6):
            grid.add(DashedLine(start=axes.c2p(0, y), end=axes.c2p(3, y), color=WHITE))
        grid.set_opacity(0.15)

        # Display elements
        self.add_foreground_mobjects(axes, x_label, y_label, curve, energy_text, area, explanation)
        self.add(axes, x_label, y_label, curve, energy_text, area, explanation, grid)
        
        post1 = Tex(
            r"""
            \parbox[t]{3cm}{
             \textbf{Potential Energy Curve}: This curve shows the relation of potential energy with the position of the particle. As the position of the particle changes, the potential energy also changes.
            }""", font_size=48).next_to(Title, DOWN, buff=0.5).shift(1.5*LEFT)
            
        sur_post1 = SurroundingRectangle(
        post1,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        post2 = Tex(
            r"""
            \parbox[t]{4cm}{
             \textbf{Energy Level}: This horizontal line represents the total energy of the particle. In quantum mechanics, if the energy of a particle is less than or equal to a certain value, then the particle can oscillate at that position. This means that it is possible for the particle to remain in the given region.
            }""", font_size=48).next_to(post1, RIGHT, buff=0.5)
        post2.next_to(axes, RIGHT+(UP/2), buff=0.5)
        post2.shift(DOWN*4) 
        sur_post2 = SurroundingRectangle(
        post2,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        
        self.add(
            Logo,
            Title,
            Second_Line,
            Page_Number,
            v_line,
            sur_post1,
            post1,
            sur_post2,
            post2
        )