from manim import *

FRAME_X_RADIUS: int = 15

config.pixel_height = 1080 * 11
config.pixel_width = 1080 * 11
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height
config.background_color = "#141414"

class Wiens_Energy(Scene):
    def construct(self):
        Title = Tex(r"Wien's Energy Distribution$^{*}$", font_size=100).move_to(6.46 * UP)
        Title_Line = Line(Title.get_left() + DOWN * 0.8, Title.get_right() + DOWN * 0.8, stroke_width=0.97)
        Second_Line = Line(LEFT, RIGHT, stroke_width=0.8)
        Second_Line.set_width(FRAME_X_RADIUS - 1)
        Second_Line.to_edge(DOWN, buff=1.3)
        Logo = MathTex(r"\left<\psi \right>\cdot  \left< \phi\right>").set_color(PURPLE_A).move_to(Second_Line.get_start() + [0.715, -0.4, 0])

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
        
        axes = Axes(
            x_range=[0, 40, 5],  # x-axis range: [min, max, step]
            y_range=[0, PI + 1, (PI + 1) / 4],  # y-axis range: [min, max, step], dividing into 4 parts
            axis_config={"color": WHITE,
            "tick_size": 0,  # Removes ticks
            }  
            
        )
        Axes_Label = axes.get_axis_labels(x_label="v(10^{14}Hz)", y_label="u(10^{-16}Jm^{-3}Hz)")
        
        # Define the blackbody radiation formula as a function
        def blackbody_radiation(x, T):
            return ((x**3) / ((PI**2) * (np.exp(2000 * x / T) - 1)) - 0.1)

        # Create plots for different temperatures
        colors = [GREEN,]
        temperatures = [5800]
        plots = VGroup()

        for i, T in enumerate(temperatures):
            plot = axes.plot(lambda x: blackbody_radiation(x, T), x_range=[0.1, 40], color=colors[i])
            plots.add(plot)
            
          
        def blackbody_radiation1(x, T1):
            return (x**3) / ((PI**2) * (np.exp(2000 * x / T1) - 1))
             
        color = [RED]
        temperature = [5800]   
        plots1 = VGroup()  
        for i, T1 in enumerate(temperature):
            plot = axes.plot(lambda x: blackbody_radiation1(x, T1), x_range=[0.1, 40], color=color[i])
            plots1.add(plot)
            

        # Create dashed grid lines, matching the axes' range and divisions
        grid = VGroup(
            # Vertical grid lines from x = 0 to x = 40, stepping by 5
            *[DashedLine(axes.c2p(x, 0), axes.c2p(x, PI + 1), color=WHITE) for x in np.arange(0, 41, 5)],  
            
            # Horizontal grid lines from y = 0 to y = PI + 1, stepping by (PI + 1) / 4
            *[DashedLine(axes.c2p(0, y), axes.c2p(40, y), color=WHITE) for y in np.arange(0, PI + 1 + (PI + 1) / 4, (PI + 1) / 4)]  
        )
        grid.set_opacity(0.2)

        axes.shift(DOWN)
        plots.shift(DOWN)
        plots1.shift(DOWN)
        grid.shift(DOWN)
        Axes_Label.shift(DOWN)
        
        
        Wiens = Tex("Wien's Law")
        Wiens.set_color(RED)
        Wiens.move_to([1,1,0])
        Planck = Tex("Planck's Law $T=4000K$")
        Planck.set_color(GREEN)
        Planck.next_to(Wiens,DOWN,buff=0.3)
        
        Body = Tex("Blackbody Radiation at $T=4000K$")
        Body.scale(1.4)
        Body.shift(LEFT*0.5+4*UP)

        # Add elements to the scene
        self.add(Logo, Title, Title_Line, Second_Line, Page_Number, axes, grid, plots, plots1, Wiens, Planck,Body,Axes_Label)
