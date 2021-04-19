

# plotly
import plotly.graph_objs as go
from plotly.offline import plot


color_bar =  ['#F04C5D',  # coral
              '#45AD8F',  # seedling
              '#253C64',  # lapis
              '#FFCE1E',  #yuzu
              '#727193',  # wistaria
              '#ffc990', 
              '#b0dfd2']  # just example here Michael please alter


def plot_bar_horizontal(table, cat_col, val_col, title):
    
    ''' Bar plot '''
    
    table = table.sort_values(val_col)
    
    fig = go.Figure(go.Bar(
            x=table[val_col],
            y=table[cat_col],
            orientation = 'h',
            marker_color = color_bar))
    
    fig.update_layout(
      title = title,
      showlegend = False
    )
      
    div = plot(fig,auto_open=False,include_plotlyjs=False,output_type='div', config={'displayModeBar': False,'showLink':False})     
    return div   
    
    
    
    
def plot_line(table, x_col, y_col, hover_label, title):
    
    ''' Line plot '''
    
    fig = go.Figure()
    
    for c in y_col:
        fig.add_trace(go.Scatter(x = table[x_col], 
                                 y = table[c], 
                                 name = c,
                    line_shape='linear'))

    fig.update_traces(hoverinfo = hover_label, mode='lines+markers')
    fig.update_layout(title = title, legend=dict(y=0.5, traceorder='reversed', font_size=16))
    

    div = plot(fig,auto_open=False,include_plotlyjs=False,output_type='div', config={'displayModeBar': False,'showLink':False})     
    return div      
    
    
    
    
def plot_scatter(table, x_col, y_col, size_col, group_col, title):
    
    ''' Scatter plot '''
    traces = []
    
    for g in table[group_col].unique():
        
        cond = table[group_col] == g
        traces += [go.Scatter(
                x = table.loc[cond, x_col],
                y = table.loc[cond, y_col],
                mode = 'markers',
                name = g,
                marker = dict(size = table.loc[cond, size_col]*6)
                )]
    
    
    layout = go.Layout(
                    title = title,
                    plot_bgcolor = 'rgb(229, 229, 229)',
                    xaxis=go.XAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                    yaxis=go.YAxis(zerolinecolor='rgb(255,255,255)', gridcolor='rgb(255,255,255)'),
                    )
    
    fig = go.Figure(data=traces, layout=layout)    
    

    div = plot(fig,auto_open=False,include_plotlyjs=False,output_type='div', config={'displayModeBar': False,'showLink':False})     
    return div   



