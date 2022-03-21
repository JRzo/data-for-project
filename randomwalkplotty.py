from random_walks import RandomWalk 
from plotly.graph_objs import Bar, Layout
from plotly import offline
import plotly.express as px

rw = RandomWalk()
rw.fill_walk()

fig = px.scatter(x=rw.x_value,y=rw.y_value)
fig.show()