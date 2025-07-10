from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die = Die()

results = []
for i in range(1000):
    result = die.roll()
    results.append(result)

f

print(results)
