from manim import *

config.background_color = "#000000"
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class GegenbauerPolynomials(Scene):
    def construct(self):
        # Title
        title = Tex(r"$\mathbb{G} \text{egenbauer}\;  \mathbb{P} \text{olynomials}$").set_width(config.frame_width - 2).shift(3.5*UP).set_color_by_gradient(BLUE, PURPLE_B)
        
        back = Tex("@maths.visualization")
        back.rotate(30*DEGREES)
        back.scale(1)     
        back.set_opacity(0.3)
        back.shift(2.4*DOWN)

        # First equation
        equation_1 = MathTex(
            r"C_n^{(\alpha)}(z) = \frac{1}{\Gamma(\alpha)}\sum_{m=0}^{\left\lfloor \frac{n}{2} \right\rfloor} "
            r"(-1)^m \frac{\Gamma(\alpha + n - m)}{m!(n - 2m)!} (2z)^{n - 2m}"
        ).set_width(config.frame_width - 2).set_color_by_gradient(BLUE, PURPLE_B)

        # Second equation
        equation_2 = MathTex(
            r"C_n^{(0)}(z) = \sum_{m=0}^{\left\lfloor \frac{n}{2} \right\rfloor} "
            r"(-1)^m \frac{(n - m - 1)!}{m!(n - 2m)!} (2z)^{n - 2m}"
        ).set_width(config.frame_width - 2).set_color_by_gradient(BLUE, PURPLE_B)

        # Positioning
        vg_equation = VGroup(equation_1, equation_2)
        vg_equation.arrange(DOWN, buff=0.25)
        
        vg_rec = SurroundingRectangle(vg_equation ,buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#141414",
        fill_opacity=1,
        stroke_width=0.5)             
        #self.add_foreground_mobject(vg_equation)
        #self.add(title, vg_equation, vg_rec)
        
        axes = Axes(
            x_range=[-1, 1, 0.5],  # Major ticks spacing
            y_range=[-1, 1, 1],
            x_length=8,
            y_length=8,
            axis_config={
                "include_ticks": False,  # Show major tick  # Remove minor ticks
            },
        ).scale(0.868)
        axes.shift(1*DOWN)
        axes.add_coordinates()
        self.add_foreground_mobject(back)
        self.add(title, back)
        self.play(Write(vg_equation, run_time=4))
        self.add_foreground_mobject(vg_equation)
        self.play(Write(vg_rec))
        self.wait(2)
        self.remove_foreground_mobject(vg_equation)
        self.play(FadeTransform(vg_equation, axes), FadeOut(vg_rec))
        
        equation0 = lambda x: 0.5
        equation1 = lambda x: x
        equation2 = lambda x: x**2
        equation3 = lambda x: x**3
        equation4 = lambda x: x**4
        equation5 = lambda x: x**5
        
        # Colors for different graphs
        color1 = RED
        color2 = GREEN
        color3 = YELLOW
        color4 = PURPLE
        color5 = ORANGE
        
        # Labels ko create karna
        
        label0 = MathTex("C_0^1,").set_color_by_gradient([BLUE, PURPLE_B])
        label1 = MathTex("C_1^1,").set_color_by_gradient([BLUE, PURPLE_B])
        label2 = MathTex("C_2^1,").set_color_by_gradient([BLUE, PURPLE_B])
        label3 = MathTex("C_3^1,").set_color_by_gradient([BLUE, PURPLE_B])
        label4 = MathTex("C_4^1,").set_color_by_gradient([BLUE, PURPLE_B])
        label5 = MathTex("C_5^1").set_color_by_gradient([BLUE, PURPLE_B])
        
        

        # Labels ko arrange karna horizontally
        VGroup(label0, label1, label2, label3, label4, label5).arrange(RIGHT, buff=0.5).next_to(axes, DOWN, buff=0.5)
        
        graph0 = axes.plot(equation0, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph0), Write(label0), run_time=1.3)
        self.wait(1.5)
        
        graph1 = axes.plot(equation1, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph1), Write(label1), run_time=1.3)
        self.wait(1.5)

        graph2 = axes.plot(equation2, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph2), Write(label2), run_time=1.3)
        self.wait(1.5)

        graph3 = axes.plot(equation3, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph3), Write(label3), run_time=1.3)
        self.wait(1.5)

        graph4 = axes.plot(equation4, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph4), Write(label4), run_time=1.3)
        self.wait(1.5)

        graph5 = axes.plot(equation5, x_range=[-1, 1]).set_color_by_gradient([BLUE, PURPLE_B])
        self.play(Create(graph5), Write(label5), run_time=1.3)
        self.wait(2)
       