# A-2 CodeCogsを使ってWEBブラウザに数式を表示する例

import urllib
import webbrowser
from sympy import *

x,y = symbols('x y')

z = x**2 / sqrt(2*y**3 - 1)

webbrowser.open("https://latex.codecogs.com/svg.image?" + urllib.parse.quote(latex(z)))
