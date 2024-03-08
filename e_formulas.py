from manim import *

config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = config.frame_height * config.pixel_width / config.pixel_height

class eFormulas(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        f1 = MathTex(r"e = \sinh (1) + \sqrt{1+ \sinh (1)^2}")
        f2 = MathTex(r"e = \frac{1}{\cosh (1)-\sinh (1)}")
        f3 = MathTex(r"e = \cosh (1) + \sqrt{\cosh(1)^2 -1}")
        f4 = MathTex(r"e = \frac{1+ \tanh \left( \frac{1}{2} \right)}{1- \tanh \left( \frac{1}{2} \right)}")
        f5 = MathTex(r"e = \sqrt{\frac{1+\tanh (1)}{1-\tanh(1)}}")
        f6 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{2k +1}{(2k)!}")
        f7 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{2k +2}{(2k +1)!}")
        f8 = MathTex(r"e = 2\sum_{k=0}^{\infty}\frac{k +1}{(2k +1)!}")
        f9 = MathTex(r"e =\frac{1}{2}\sum_{k=0}^{\infty}\frac{k +1}{k!}")
        f10 = MathTex(r"e = \left( \sum_{k=0}^{\infty}\frac{(-1)^k}{k!}\right)^{-1}")
        f11 = MathTex(r"e = \left( \sum_{k=0}^{\infty}\frac{1-2k}{(2k)!)}\right)^{-1}")
        f12 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{3-4k^2}{(2k+1)!}")
        f13 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{1}{k!}")
        f14 = MathTex(r"e = \frac{2}{3}\sum_{k=0}^{\infty}\frac{k+1}{2^{k\,\text{mod}\, 2}k!}")
        f15 = MathTex(r"e = \frac{1}{2}\sum_{k=0}^{\infty}\frac{(k+2)^{(k+1)\, \text{mod}\, 2}}{k!}")
        f16 = MathTex(r"e = \frac{1}{2}\sum_{k=0}^{\infty}\frac{(k+2)^{k\, \text{mod}\, 2}}{k!}")
        f17 = MathTex(r"e = \frac{2}{3}\sum_{k=0}^{\infty}\frac{(k+3)^{k\, \text{mod}\, 2}}{2^{k\, \text{mod}\, 2}k!}")
        f18 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{(3k+2)^2+1}{(3k+2)!}")
        f19 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{(3k+1)^2+1}{(3k+1)!}")
        f20 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{(3k)^2+1}{(3k)!}")
        f21 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{(8k-4)\left( 8k^2 +1 \right)+5}{(4k)!}")
        f22 = MathTex(r"e = \sum_{k=0}^{\infty}\frac{3-(2k-1)^2}{(2k)!}")
        f23 = MathTex(r"e = 2\sum_{k=0}^{\infty}\frac{-2k^2+2k+1}{(2k)!}")
        f24 = MathTex(r"e = 3-\sum_{k=0}^{\infty}\frac{k+1}{(k+3)!}")
        f25 = MathTex(r"e = \left( \sum_{k=0}^{\infty}\frac{1}{10^k \cdot k!} \right)^{10}")
        f26 = MathTex(r"e = \left( \sum_{k=0}^{\infty}\frac{4k+3}{(2k+1)!\cdot 2^{2k+1}} \right)^2")
        f27 = MathTex(r"e = \left( \frac{16}{31}\left( 1+\sum_{k=1}^{\infty}\frac{\frac{1}{2}k^3+\frac{1}{2}k+1}{2^k k!} \right) \right)^2").scale(0.8)
        f28 = MathTex(r"e = 2\cdot \prod_{k=1}^{\infty}\left( \prod_{j=1}^{2^{k-1}}\frac{2^k+2j}{2^k+2j-1} \right)^{\frac{1}{2^k}}")
        f29 = MathTex(r"e = 2 + \frac{1}{1 + \frac{1}{2 + \frac{1}{1 + \frac{1}{1 + \frac{1}{4 + \frac{1}{1 + \frac{1}{1+\frac{1}{6+\cdots}}}}}}}}")
        f30 = MathTex(r"e = 3 + \frac{-1}{4 + \frac{-2}{5 + \frac{-3}{6 + \frac{-4}{7 + \frac{-5}{8 +\cdots}}}}}}}}")
        f31 = MathTex(r"e = 2 + \frac{1}{1 + \frac{1}{2 + \frac{2}{3 + \frac{3}{4 + \frac{4}{5 + \frac{5}{6 + \frac{6}{7+\frac{7}{8+\cdots}}}}}}}}")
        f32 = MathTex(r"e = \lim_{n\to \infty}\frac{n}{\sqrt[n]{n!}}")
        f33 = MathTex(r"e = \lim_{n\to \infty}\frac{n!}{!n}")
        f34 = MathTex(r"e = \lim_{n\to \infty}\left( \sqrt[n]{n} \right)^{\pi (n)}")
        f35 = MathTex(r"e = \lim_{n\to \infty}\sqrt[n]{n\#}")
        f36 = MathTex(r"e \approx \sqrt{\frac{158452}{21444}}")
        f37 = MathTex(r"e \approx \frac{58291}{21444}")
        f38 = MathTex(r"e \approx \frac{878}{323}")
        f39 = MathTex(r"e \approx \frac{1457}{536}")
        f40 = MathTex(r"e \approx \frac{49171}{18089}")
        f41 = MathTex(r"e \approx \frac{1084483}{398959}")
        f42 = MathTex(r"e = \lim_{n\to \infty}\left( 1+\frac{1}{n} \right)^n")
        f43 = MathTex(r"e")

        rt = 0.5
        self.play(Write(f1), run_time=1)
        self.play(TransformMatchingShapes(f1, f2), run_time=rt)
        self.play(TransformMatchingShapes(f2, f3), run_time=rt)
        self.play(TransformMatchingShapes(f3, f4), run_time=rt)
        self.play(TransformMatchingShapes(f4, f5), run_time=rt)
        self.play(TransformMatchingShapes(f5, f6), run_time=rt)
        self.play(TransformMatchingShapes(f6, f7), run_time=rt)
        self.play(TransformMatchingShapes(f7, f8), run_time=rt)
        self.play(TransformMatchingShapes(f8, f9), run_time=rt)
        self.play(TransformMatchingShapes(f9, f10), run_time=rt)
        self.play(TransformMatchingShapes(f10, f11), run_time=rt)
        self.play(TransformMatchingShapes(f11, f12), run_time=rt)
        self.play(TransformMatchingShapes(f12, f13), run_time=rt)
        self.play(TransformMatchingShapes(f13, f14), run_time=rt)
        self.play(TransformMatchingShapes(f14, f15), run_time=rt)
        self.play(TransformMatchingShapes(f15, f16), run_time=rt)
        self.play(TransformMatchingShapes(f16, f17), run_time=rt)
        self.play(TransformMatchingShapes(f17, f18), run_time=rt)
        self.play(TransformMatchingShapes(f18, f19), run_time=rt)
        self.play(TransformMatchingShapes(f19, f20), run_time=rt)
        self.play(TransformMatchingShapes(f20, f21), run_time=rt)
        self.play(TransformMatchingShapes(f21, f22), run_time=rt)
        self.play(TransformMatchingShapes(f22, f23), run_time=rt)
        self.play(TransformMatchingShapes(f23, f24), run_time=rt)
        self.play(TransformMatchingShapes(f24, f25), run_time=rt)
        self.play(TransformMatchingShapes(f25, f26), run_time=rt)
        self.play(TransformMatchingShapes(f26, f27), run_time=rt)
        self.play(TransformMatchingShapes(f27, f28), run_time=rt)
        self.play(TransformMatchingShapes(f28, f29), run_time=rt)
        self.play(TransformMatchingShapes(f29, f30), run_time=rt)
        self.play(TransformMatchingShapes(f30, f31), run_time=rt)
        self.play(TransformMatchingShapes(f31, f32), run_time=rt)
        self.play(TransformMatchingShapes(f32, f33), run_time=rt)
        self.play(TransformMatchingShapes(f33, f34), run_time=rt)
        self.play(TransformMatchingShapes(f34, f35), run_time=rt)
        self.play(TransformMatchingShapes(f35, f36), run_time=rt)
        self.play(TransformMatchingShapes(f36, f37), run_time=rt)
        self.play(TransformMatchingShapes(f37, f38), run_time=rt)
        self.play(TransformMatchingShapes(f38, f39), run_time=rt)
        self.play(TransformMatchingShapes(f39, f40), run_time=rt)
        self.play(TransformMatchingShapes(f40, f41), run_time=rt)
        self.play(TransformMatchingShapes(f41, f42), run_time=rt)
        self.play(TransformMatchingShapes(f42, f43), run_time=3*rt)
        self.play(
            self.camera.frame.animate.scale(0.5).move_to(ORIGIN)
        )
        self.wait(2)
