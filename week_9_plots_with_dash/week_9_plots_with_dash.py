import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
import plotly.express as px
import io
import base64

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

df = pd.read_csv('games.csv')

# -------------------------------------------------------------------------------------------------------------- 

#											PART 1: DESIGN PARAMETERS

# --------------------------------------------------------------------------------------------------------------
# Here we will set the colors, margins, DIV height&weight and other parameters

colors = {
		'full-background': 	'#DCDCDC',  
		'block-borders': '#B0B0B0' }


margins = {
		'block-margins': '10px 10px 10px 10px',
		'block-margins': '4px 4px 4px 4px'
}

sizes = {
		'subblock-heights': 300
}



# -------------------------------------------------------------------------------------------------------------- 

#											PART 2: ACTUAL LAYOUT

# --------------------------------------------------------------------------------------------------------------
# Here we will set the DIV-s and other parts of our layout
# We need too have a 2x2 grid
# I have also included 1 more grid on top of others, where we will show the title of the app



# -------------------------------------------------------------------------------------- DIV for TITLE
div_title = html.Div(children =	html.H1('Random charts'),
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'text-align': 'center'
							}
					)

div_hist = dcc.Graph (id = 'histogram-of-age_1',
				figure = {
							'data': [go.Histogram(x=df['turns'])],
							'layout': dict(xaxis={'title': 'TURNS'},
						                yaxis={'title': 'quantity'},
						                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
						                legend= 'True',
						                color_discrete_sequence=['indianred']
						               )
							},
				style = {'margin-right': 20, 'margin-left': 20, 'height': '250px'}
				)

# -------------------------------------------------------------------------------------- DIV for first raw (1.1 and 1.2)
div_1_1 = html.Div(children = ['block 1-1', div_hist],
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights']
					}
				)
div_6 = html.Img(src='chess.png', style={'height':'90%', 'width':'90%'}
		)

div_1_2 = html.Div(children = ['block 1-2', div_6],
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights']
					}
				)

# Collecting DIV 1.1 and 1.2 into the DIV of first raw.
# Pay attention to the 'display' and 'flex-flaw' attributes.
# With this configuration you are able to let the DIV-s 1.1 and 1.2 be side-by-side to each other.
# If you skip them, the DIV-s 1.1 and 1.2 will be ordered as separate rows.
# Pay also attention to the 'width' attributes, which specifiy what percentage of full row will each DIV cover.
div_raw1 = html.Div(children =	[div_1_1,
								div_1_2,
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							})



# -------------------------------------------------------------------------------------- DIV for second raw (2.1 and 2.2)
div_2_1 = html.Div(children = 'block 2-1',
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights'],
					}
				)



buf = io.BytesIO() 
plt.hist(df['white_rating'])
plt.savefig(buf, format = "png")
plt.close()
data = base64.b64encode(buf.getbuffer()).decode("utf8") 
div_count =  "data:image/png;base64,{}".format(data)




div_2_2 = html.Div(children = ['block 2-2', div_count],
					style = {
							'border': '1px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'width': '49%',
							'height': sizes['subblock-heights'],
					}
				)


div_raw2 = html.Div(children =	[div_2_1,
								div_2_2
								],
					style ={
							'border': '3px {} solid'.format(colors['block-borders']),
							'margin': margins['block-margins'],
							'display': 'flex',
							'flex-flaw': 'row-wrap'
							})


# -------------------------------------------------------------------------------------- Collecting all DIV-s in the final layout
# Here we collect all DIV-s into a final layout DIV

app.layout = html.Div(	[
						div_title,
						div_raw1,
						div_raw2
						],
						style = {
							'backgroundColor': colors['full-background']
						}
					)




# -------------------------------------------------------------------------------------------------------------- 

#											PART 3: RUNNING THE APP

# --------------------------------------------------------------------------------------------------------------
# >> use __ debug=True __ in order to be able to see the changes after refreshing the browser tab,
#			 don't forget to save this file before refreshing
# >> use __ port = 8081 __ or other number to be able to run several apps simultaneously
app.run_server(debug=True, port = 8081)