from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter
from plotly.offline import plot



def dash(request):
    return render(request, 'dash/dash.html')



