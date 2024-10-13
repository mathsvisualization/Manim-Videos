from manim import *
import numpy as np
from scipy.integrate import quad

config.background_color = "#000000"
config.pixel_height = 1920 * 1
config.pixel_width = 1080 * 1
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class Fresnel_Integration(Scene):
    def construct(self):
        # Setup
        w = config.frame_width
        h = config.frame_height
        # Axes 
        axes = Axes(
            x_range=[-6, 6, 2],  # Major ticks spacing
            y_range=[-1, 1, 1],
            x_length=7,
            y_length=6,
            axis_config={
                "include_ticks": True,  # Show major tick  # Remove minor ticks
            },
        ).scale(1)
        axes.add_coordinates()
        
        # Graph 
        def fresnel_C(x):
            return quad(lambda t: np.cos(np.pi / 2 * t**2), 0, x)[0]

        def fresnel_S(x):
            return quad(lambda t: np.sin(np.pi / 2 * t**2), 0, x)[0]
            
        C_graph = axes.plot(lambda x: fresnel_C(x), color=BLUE_C)
        S_graph = axes.plot(lambda x: fresnel_S(x), color=YELLOW_A)
        
        # Title 
        Logo = Tex(r"$\mathbb{F} \text{resnel}\; \mathbb{I} \text{ntegral}$").scale(2.1)
        Logo.next_to(axes, UP, buff=0.4)
        Logo.set_color_by_gradient(BLUE_B, PURPLE_A, PURPLE_B)
        
        # Sinx 
        sinx = MathTex(r"S(x) = \int_{0}^{x} sin(t^2) dt")
        sinx.next_to(axes,DOWN, buff=0.8)
        sinx.scale(1)
        sinx.set_color(YELLOW_A)
        
        # Cosx
        cosx = MathTex(r"C(x) = \int_{0}^{x} cos(t^2) dt")
        cosx.next_to(axes,DOWN, buff=0.8)
        cosx.scale(1)
        cosx.set_color(BLUE_C)
        
        equal = MathTex(r"\int_{-\infty}^{+\infty} sin(t^2) dt = \int_{-\infty}^{+\infty} cos(t^2) dt")
        equal.next_to(axes,DOWN, buff=0.8)
        equal.scale(1)
        equal.set_color_by_gradient(YELLOW_A, BLUE_C)
        
        equal2 = MathTex(r"\int_{-\infty}^{+\infty} sin(t^2) dt = \frac{\sqrt{2 \pi}}{2}")
        equal2.next_to(axes,DOWN, buff=0.8)
        equal2.scale(1)
        equal2.set_color_by_gradient(YELLOW_A, BLUE_C)
                
        rec = SurroundingRectangle(equal2,buff=0.2,
        stroke_color=WHITE,
        corner_radius=0.1,
        fill_color="#141414",
        fill_opacity=1,
        stroke_width=0.5)
        
        colors = [YELLOW_A, BLUE_C]  
        
        back = Tex("@maths.visualization")
        back.rotate(30*DEGREES)
        back.scale(1)     
        back.set_opacity(0.3)
        back.shift(2*DOWN)
        self.add(axes, Logo, back)
        self.wait(0.5)
        self.play(FadeIn(sinx, shift=1*UP))
        self.wait(1.6)
        self.play(FadeTransform(sinx, S_graph, path_arc=PI/2))
        self.wait()
        self.play(FadeIn(cosx, shift=1*UP))
        self.wait(1.6)
        self.play(FadeTransform(cosx, C_graph, path_arc=-PI/2))
        self.wait()       
        self.play(Write(equal, shift=1*UP))
        self.wait(2.1)
        self.play(TransformMatchingShapes(equal, equal2))
        self.add_foreground_mobject(equal2)  
        self.play(Write(rec))
        self.wait()
