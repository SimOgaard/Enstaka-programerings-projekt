import pygal
from pygal.style import Style
custom_style = Style(
    colors=('#ff8000', '#ff4000', '#ff0000'))

b_chart = pygal.Bar(style=custom_style)
b_chart.title = ("Tempratur")
b_chart.add("10:00", [15])
b_chart.add("11:00", [20])
b_chart.add("12:00", [25])
b_chart.render_in_browser()