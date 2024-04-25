from manim import *

import manim
config.pixel_height = 1080
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height


class TitleExample(Scene):
    def construct(self):
        Equ = MathTex(r"\frac{\partial u}{\partial t} + \left ( u\cdot \triangledown  \right )u=\frac1\rho \triangledown p + v \triangledown^2 u")
        Equ.scale(1.17)
        
        self.add(Equ)
