from manim import *

class LaTeXJustifiedParagraphExample(Scene):
    def construct(self):
        # Define the LaTeX paragraph function
        def tex_p(latex_text, width):
            paragraph = Tex(latex_text, font_size=24)
            paragraph.set_width(width)
            return paragraph
        latex_text = r"""
        \parbox[t]{4cm}{
            This is an example of a justified paragraph written in LaTeX.
            You can include multiple lines of text and LaTeX formatting within the paragraph.
            The width of this paragraph can be adjusted to fit the desired space.
            This text will be justified to fill the width specified by \texttt{6cm}.
        }
        """

        # Create the paragraph with the desired width
        paragraph = create_latex_paragraph(latex_text, width=2)

        # Add the paragraph to the scene
        self.add(paragraph)
        self.wait()
