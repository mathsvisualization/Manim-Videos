from manim import *

# Configure scene settings
config.background_color = "#141414"
config.pixel_height = 1080
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ThreeParticleEntanglement(Scene):
    def construct(self):
        Title = Tex(r"Del Operator or Nabla Operator",font_size=100).move_to(6.46*UP)
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
        
        Formula = MathTex(
        r"\nabla = \hat{i} \frac{\partial}{\partial x} + \hat{j} \frac{\partial}{\partial y} + \hat{k} \frac{\partial}{\partial z}",
        font_size=100,        
        color=WHITE
        )
        Formula[0][0].set_color(TEAL_D)
        Formula[0][4].set_color(LIGHT_PINK)
        Formula[0][6].set_color(LIGHT_PINK)
        Formula[0][11].set_color(LIGHT_PINK)
        Formula[0][13].set_color(LIGHT_PINK)
        Formula[0][18].set_color(LIGHT_PINK)
        Formula[0][20].set_color(LIGHT_PINK)
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
        
class DelOperator2(Scene):
    def construct(self):
        Title = Tex(r"Understanding Nabla Operator Formula",font_size=100).move_to(6.46*UP)
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
        
        # Formula 
        
        Formula = MathTex(
        r"\nabla = \hat{i} \frac{\partial}{\partial x} + \hat{j} \frac{\partial}{\partial y} + \hat{k} \frac{\partial}{\partial z}",
        font_size=100,        
        color=WHITE
        )
        Formula[0][0].set_color(TEAL_D)
        Formula[0][4].set_color(LIGHT_PINK)
        Formula[0][6].set_color(LIGHT_PINK)
        Formula[0][11].set_color(LIGHT_PINK)
        Formula[0][13].set_color(LIGHT_PINK)
        Formula[0][18].set_color(LIGHT_PINK)
        Formula[0][20].set_color(LIGHT_PINK)
        Formula[0][1:].set_opacity(0.50)
        self.add_foreground_mobject(Formula)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{
            The \textbf{Nabla operator} is defined in vector form, and is used to calculate the spatial derivatives of any function or field.
            }""", tex_to_color_map={r"\textbf{Nabla operator}": TEAL_D}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][0],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=TEAL_D,
        fill_opacity=0.1,
        stroke_width=0.8
        )
                      
        sur_omega = SurroundingRectangle(
        omega_exp,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_omega = DashedLine(sur_for.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        self.add(Logo,
                 Title, 
                 Second_Line, 
                 Page_Number, 
                 v_line,
                 sur_for,
                 Formula,
                 sur_omega,                 
                 sur_omega,
                 omega_exp,
                 dash_omega
            )
            
class DelOperator3(Scene):
    def construct(self):
        Title = Tex(r"Understanding Nabla Operator Formula",font_size=100).move_to(6.46*UP)
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
        
        # Formula 
        
        Formula = MathTex(
        r"\nabla = \hat{i} \frac{\partial}{\partial x} + \hat{j} \frac{\partial}{\partial y} + \hat{k} \frac{\partial}{\partial z}",
        font_size=100,        
        color=WHITE
        )
        Formula[0][0].set_color(TEAL_D)
        Formula[0][4].set_color(LIGHT_PINK)
        Formula[0][6].set_color(LIGHT_PINK)
        Formula[0][11].set_color(LIGHT_PINK)
        Formula[0][13].set_color(LIGHT_PINK)
        Formula[0][18].set_color(LIGHT_PINK)
        Formula[0][20].set_color(LIGHT_PINK)
        Formula[0][0:2].set_opacity(0.50)
        Formula[0][4:9].set_opacity(0.50)
        Formula[0][11:17].set_opacity(0.50)
        Formula[0][18:22].set_opacity(0.50)
        self.add_foreground_mobject(Formula)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{
            These are \textbf{unit} vectors that represent x, y, and z directions.
            }""", tex_to_color_map={r"\textbf{unit}": WHITE}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][2:4],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
        sur_for1 = SurroundingRectangle(
        Formula[0][9:11],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
        sur_for2 = SurroundingRectangle(
        Formula[0][16:18],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=WHITE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
                                                                
        sur_omega = SurroundingRectangle(
        omega_exp,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_omega = DashedLine(sur_for.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        dash_omega1 = DashedLine(sur_for1.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        dash_omega2 = DashedLine(sur_for2.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        self.add(Logo,
                 Title, 
                 Second_Line, 
                 Page_Number, 
                 v_line,
                 sur_for,
                 sur_for1,
                 sur_for2,
                 Formula,
                 sur_omega,
                 omega_exp,
                 dash_omega,
                 dash_omega1,
                 dash_omega2
            )
            
class DelOperator4(Scene):
    def construct(self):
        Title = Tex(r"Understanding Nabla Operator Formula",font_size=100).move_to(6.46*UP)
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
        
        # Formula 
        
        Formula = MathTex(
        r"\nabla = \hat{i} \frac{\partial}{\partial x} + \hat{j} \frac{\partial}{\partial y} + \hat{k} \frac{\partial}{\partial z}",
        font_size=100,        
        color=WHITE
        )
        Formula[0][0].set_color(TEAL_D)
        Formula[0][4].set_color(LIGHT_PINK)
        Formula[0][6].set_color(LIGHT_PINK)
        Formula[0][11].set_color(LIGHT_PINK)
        Formula[0][13].set_color(LIGHT_PINK)
        Formula[0][18].set_color(LIGHT_PINK)
        Formula[0][20].set_color(LIGHT_PINK)
        Formula[0][0:4].set_opacity(0.50)
        Formula[0][8:11].set_opacity(0.50)
        Formula[0][15:18].set_opacity(0.50)
        self.add_foreground_mobject(Formula)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{
            These are \textbf{partial derivatives} which represent the variation of a function along the respective directions (x, y, z).
            }""", tex_to_color_map={r"\textbf{partial derivatives}": LIGHT_PINK}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][4:8],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=LIGHT_PINK,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
        sur_for1 = SurroundingRectangle(
        Formula[0][11:15],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=LIGHT_PINK,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
        sur_for2 = SurroundingRectangle(
        Formula[0][18:22],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=LIGHT_PINK,
        fill_opacity=0.1,
        stroke_width=0.8
        )
        
                                                                
        sur_omega = SurroundingRectangle(
        omega_exp,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.5
        )
        
        dash_omega = DashedLine(sur_for.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        dash_omega1 = DashedLine(sur_for1.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        dash_omega2 = DashedLine(sur_for2.get_bottom(), sur_omega.get_top(), dash_length=0.15)
        
        self.add(Logo,
                 Title, 
                 Second_Line, 
                 Page_Number, 
                 v_line,
                 sur_for,
                 sur_for1,
                 sur_for2,
                 Formula,
                 sur_omega,
                 omega_exp,
                 dash_omega,
                 dash_omega1,
                 dash_omega2
            )
            
class DelOperator5(Scene):
    def construct(self):
        Title = Tex(r"Use of Del Operator in Quantum Mechanics",font_size=100).move_to(6.46*UP)
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
        
        # some example
        
        first = Tex(r"1. \textbf{Gradient} (\textbf{$\nabla$}\textbf{$\psi$}):",
              font_size=82,
              tex_to_color_map={r"\textbf{$\nabla$}": TEAL_D, r"\textbf{$\psi$}": YELLOW}
              )
        first.next_to(Title, DOWN, buff=1)
        first.shift(4*LEFT)
        
        system = Tex(
            r"""
            \parbox[t]{7cm}{If a quantum system has a \textbf{wave function} $\psi$$(x, y, z)$, then we have a gradient of the wave function. It tells how is the spatial variation of the \textbf{wave function} \textbf{$\nabla$}\textbf{$\psi$}, i.e. in which direction its change is more or less..
            }""", tex_to_color_map={r"$\psi$": YELLOW, r"\textbf{$\nabla$}": TEAL_D, r"\textbf{$\psi$}": YELLOW, r"\textbf{wave function}": YELLOW}, font_size=48).set_width(config.frame_width - 3)
        system.next_to(first, DOWN, buff=MED_SMALL_BUFF)
        system.shift(RIGHT*4.18)
        
        system2 = Tex(
            r"""
            \parbox[t]{7cm}{In quantum mechanics, the gradient operator is used to describe how the probability amplitude of the \textbf{wave function } changes in space, revealing the direction and rate at which the wave function's probability distribution evolves..
            
            }""", tex_to_color_map={r"\textbf{wave function }": YELLOW}, font_size=48).match_width(system)
        system2.next_to(system, DOWN, buff=MED_LARGE_BUFF)
        
        
        
        self.add(Logo, Title, Second_Line, Page_Number, v_line,
                 first,
                 system,
                 system2,
                 
              )
              
class DelOperator6(Scene):
    def construct(self):
        Title = Tex(r"Use of Del Operator in Quantum Mechanics",font_size=100).move_to(6.46*UP)
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
        
        # some example
        
        first = Tex(r"2. \textbf{Laplacian} ($\nabla$$^2$):",
              font_size=82,
              tex_to_color_map={r"$\nabla$": TEAL_D}
              )
        first.next_to(Title, DOWN, buff=1)
        first.shift(4*LEFT)
        
        system = Tex(
            r"""
            \parbox[t]{7cm}{This is known as the Laplacian, an important operator which is the second derivative.
            }""", font_size=48).set_width(config.frame_width - 3)
        system.next_to(first, DOWN, buff=MED_SMALL_BUFF)
        system.shift(RIGHT*4.18)
        
        sys_eq = MathTex(r"\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2}").set_width(system.get_width() - 5)
        sys_eq.next_to(system, DOWN, buff=MED_LARGE_BUFF+0.2)
        sys_eq[0][0].set_color(TEAL_D)
        sys_eq[0][3].set_color(LIGHT_PINK)
        sys_eq[0][6].set_color(LIGHT_PINK)
        sys_eq[0][10].set_color(LIGHT_PINK)
        sys_eq[0][13].set_color(LIGHT_PINK)
        sys_eq[0][17].set_color(LIGHT_PINK)
        sys_eq[0][20].set_color(LIGHT_PINK)
        system2 = Tex(
            r"""
            \parbox[t]{7cm}{It is used to represent the kinetic energy operator in the Schrödinger equation. The Laplacian describes the spread or distribution of the \textbf{wave function}, which represents the position probability of the particle.
            
            }""", tex_to_color_map={r"\textbf{wave function}": YELLOW}, font_size=48).match_width(system)
        system2.next_to(sys_eq, DOWN, buff=MED_LARGE_BUFF+0.2)
        
        sur_sys = SurroundingRectangle(
        sys_eq,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#191919",
        fill_opacity=1,
        stroke_width=0.8
        )
        
        self.add(Logo, Title, Second_Line, Page_Number, v_line,
                 first,
                 system,
                 system2,
                 sur_sys,
                 sys_eq
              )
              
class DelOperator7(Scene):
    def construct(self):
        Title = Tex(r"Use of Del Operator in Quantum Mechanics",font_size=100).move_to(6.46*UP)
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
        
        # some example
        
        first = Tex(r"3. \textbf{Divergence} ($\nabla$$\cdot$A):",
              font_size=82,
              tex_to_color_map={r"$\nabla$": TEAL_D}
              )
        first.next_to(Title, DOWN, buff=1)
        first.shift(3.6*LEFT)
        
        system = Tex(
            r"""
            \parbox[t]{7cm}{The \textbf{divergence} operator is used in field theory, and it shows the spread or convergence of a vector field..
            }""", tex_to_color_map={r"\textbf{divergence}": TEAL_D}, font_size=48).set_width(config.frame_width - 3)
        system.next_to(first, DOWN, buff=MED_SMALL_BUFF)
        system.shift(RIGHT*4)
        
        system2 = Tex(
            r"""
            \parbox[t]{7cm}{In quantum mechanics, when \textbf{divergence} is applied to a probability current vector field, it describes the movement or flow of a particle.
            
            }""", tex_to_color_map={r"\textbf{divergence}": TEAL_D}, font_size=48).match_width(system)
        system2.next_to(system, DOWN, buff=MED_LARGE_BUFF)
        
        second = Tex(r"4. \textbf{Curl} ($\nabla$$\times$A):",
              font_size=82,
              tex_to_color_map={r"$\nabla$": TEAL_D}
              )
        second.next_to(system2, DOWN, buff=1)
        second.shift(5.1*LEFT)
        
        system3 = Tex(
            r"""
            \parbox[t]{7cm}{The Curl operator measures the rotation or circulation of a vector field.
            
            }""", font_size=48).match_width(system).next_to(system2, DOWN, buff=1+LARGE_BUFF)
                
        self.add(Logo, Title, Second_Line, Page_Number, v_line,
                 first,
                 system,
                 system2,
                 second,
                 system3
              )