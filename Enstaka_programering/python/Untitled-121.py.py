import pygal

bar_chart = pygal.StackedBar()
bar_chart.add('Fibonacci 1', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
bar_chart.add('Fibonacci 2', [55, 34, 21, 13, 8, 5, 3, 2, 1, 1, 0])

bar_chart.render_to_file('bar_chart.svg')