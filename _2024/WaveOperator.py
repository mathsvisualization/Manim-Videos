from manim import *

# Configure scene settings
config.background_color = "#141414"
config.pixel_height = 1080
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class ThreeParticleEntanglement(Scene):
    def construct(self):
        Title = Tex(r"Wave Operations in Scattering Theory",font_size=100).move_to(6.46*UP)
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
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=100,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW)
        Formula[0][13].set_color(BLUE)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][18:20].set_color(BLUE)
        
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
        
class ThreeParticleEntanglement1(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW).set_opacity(1)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][2:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{These are the \textbf{wave operators}, which map the free evolution of a particle to its evolution under the potential.
            }""", tex_to_color_map={r"\textbf{wave operators}": YELLOW}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][0:2],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=YELLOW,
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
        
class ThreeParticleEntanglement2(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW).set_opacity(1)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][2:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{These are the \textbf{wave operators}, which map the free evolution of a particle to its evolution under the potential.
            }""", tex_to_color_map={r"\textbf{wave operators}": YELLOW}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][0:2],
        buff=0.1,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=YELLOW,
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

class ThreeParticleEntanglement3(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][:2].set_opacity(0.5)
        Formula[0][3:].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6.4cm}{Represents the \textbf{initial state} of the particle when it is free of any potential (i.e., unaffected by $V$). This state evolves according to $H_0$ in the absence of interaction....
            }""", tex_to_color_map={r"\textbf{initial state}": GOLD_B}, font_size=72).shift(1*DOWN)
        sur_for = SurroundingRectangle(
        Formula[0][2:3],
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=GOLD_B,
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
          
class ThreeParticleEntanglement4(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][11:].set_opacity(0.5)
        Formula[0][0:4].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6.4cm}{This notation signifies the system's behavior as time ($t$) approaches positive or negative infinity. It helps in observing the asymptotic behavior of the particle, whether it is freely moving or influenced by a potential.
            }""", tex_to_color_map={r"$t$": WHITE}, font_size=72).shift(1*DOWN)
            
        sur_for = SurroundingRectangle(
        Formula[0][5:11],
        buff=0.2,
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

class ThreeParticleEntanglement5(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        
        # Formula 
        
        Formula = MathTex(
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][-8:].set_opacity(0.5)
        Formula[0][0:13].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6.4cm}{The \textbf{total Hamiltonian}, representing the overall energy of the system, which includes both the free Hamiltonian $H_0$ and the potential $V$.
    }""", 
            tex_to_color_map={r" Hamiltonian ": BLUE, "$H_0$": BLUE}, 
            font_size=72
        ).shift(1*DOWN)
        sur_for = SurroundingRectangle(
        Formula[0][13:-8],
        buff=0.09,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=BLUE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
                      
        sur_omega = SurroundingRectangle(
        omega_exp,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#141414",
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

class ThreeParticleEntanglement6(Scene):
    def construct(self):
        Title = Tex(r"Breaking Down the Wave Operator Formula",font_size=100).move_to(6.46*UP)
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
        
        # Formula 
        
        Formula = MathTex(
        r"\Omega^\pm \phi = \lim_{t \to \pm \infty} e^{iHt} e^{-iH_0 t} \phi",
        font_size=104,
        color=WHITE
        )                
        self.add_foreground_mobject(Formula)
        Formula[0][0:2].set_color(YELLOW)
        Formula[0][2].set_color(GOLD_B)
        Formula[0][-1].set_color(GOLD_B)
        Formula[0][13].set_color(BLUE)
        Formula[0][18:20].set_color(BLUE)
        Formula[0][-2:].set_opacity(0.5)
        Formula[0][0:18].set_opacity(0.5)
        Formula.next_to(Title, DOWN, buff=1)      
        omega_exp = Tex(
            r"""
            \parbox[t]{6cm}{The \textbf{free Hamiltonian}, which describes the particle's energy and motion without any external potential.
    }""", 
            tex_to_color_map={r"free Hamiltonian": BLUE}, 
            font_size=72
        ).shift(1*DOWN)
        sur_for = SurroundingRectangle(
        Formula[0][18:-2],
        buff=0.09,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color=BLUE,
        fill_opacity=0.1,
        stroke_width=0.8
        )
                      
        sur_omega = SurroundingRectangle(
        omega_exp,
        buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#141414",
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
