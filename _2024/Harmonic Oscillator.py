from manim import *

class SpringMassSystemAnimated(Scene):
    def construct(self):
      
        # Wall
        wall = Rectangle(width=0.2, height=3).set_fill(GRAY, opacity=1).shift(4*LEFT).scale(1.2)

        # Position Tracker for Mass
        mass_position = ValueTracker(2)

        # Mass
        mass = always_redraw(lambda: Square(side_length=1).set_fill(BLUE, opacity=0.7).move_to(RIGHT*mass_position.get_value()).scale(1.2)
                )
        mass_label = always_redraw(lambda: MathTex(r"m").move_to(mass.get_center()))
        

        line = always_redraw(lambda: Line(wall.get_right(), mass.get_left()).add_tip().shift(1 * UP))
        line.set_color(WHITE)
        line.set_stroke(WHITE, 2)

        spring = always_redraw(
            lambda: self.create_spring(
                start=wall.get_right(),
                end=mass.get_left(),
                coils=10,
                amplitude=0.2
            )
        )

        force_arrow = always_redraw(
            lambda: Arrow(
                start=mass.get_right(),
                end=mass.get_right() + RIGHT * 2,
                buff=0.1,
                color=BLUE
            )
        )
        force_label = always_redraw(
            lambda: MathTex(r"F = -kx")
            .scale(0.7)
            .next_to(force_arrow, UP, buff=0.1)
            .shift(0.1 * RIGHT)
        )

        
        disp_label = always_redraw(
            lambda: MathTex(r"x")
            .next_to(line, UP, buff=0.2)
        )
        
        self.add(wall, mass, mass_label, spring, force_arrow, force_label, disp_label, line)

        total_duration = 10
        loop_duration = 3
        loops = total_duration // loop_duration
      
        for _ in range(int(loops)):
            self.play(
                mass_position.animate.set_value(-2),
                rate_func=there_and_back,
                run_time=loop_duration
            )

    def create_spring(self, start, end, coils=10, amplitude=0.2):
        """
        Creates a spring-like shape between two points.
        """
        points = []
        direction = np.array(end) - np.array(start)
        length = np.linalg.norm(direction)
        unit_dir = direction / length
        perpendicular = np.array([-unit_dir[1], unit_dir[0], 0])

        for i in range(coils * 2 + 1):
            t = i / (coils * 2)
            offset = amplitude if i % 2 == 1 else -amplitude
            points.append(
                np.array(start)
                + t * direction
                + offset * perpendicular
            )
        points[-1] = np.array(end)

        return VMobject().set_points_as_corners(points).set_color(WHITE).set_stroke(width=3)
