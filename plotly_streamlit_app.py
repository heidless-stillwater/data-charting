


import streamlit as st  
import plotly.express as px   

iris_df = px.data.iris()

st.subheader("iris dataset")
st.dataframe(iris_df)

basic_scatter_fig = px.scatter(iris_df, 
                               x="sepal_width", 
                               y="sepal_length", 
                               color="species", 
                               size="petal_length",
                               symbol="species",
                               hover_data="petal_width"
)

st.subheader("iris dataset: basic scatter plot")
st.plotly_chart(basic_scatter_fig)


######################
# user axis selection
x_axis = st.selectbox("choose var for x-axis", iris_df.columns, index=0)
y_axis = st.selectbox("choose var for y-axis", iris_df.columns, index=1)


#####################
# create bubble chart
#
colored_bubble_hover_fig = px.scatter(iris_df, 
                               x=x_axis, 
                               y=y_axis, 
                               color="species", 
                               size="petal_length",
                               hover_data="petal_width"
)

st.subheader("iris dataset: bubble chart")

colored_bubble_hover_fig.update_layout(
  font_family="Courier New",
  title="Iris Dataset Bubble Chart",
  xaxis_title=x_axis,
  yaxis_title=y_axis,
  legend_title="Species"
)

st.plotly_chart(colored_bubble_hover_fig)

###########################################
# select chart type
#
chart_type = st.radio('select chart type: ', ('Scatter Plot', 'Line Chart', 'Bar Chart', 'Histogram', 'Box Plot', 'Pie Chart', '3D Scatter Plot'))

# visualise the relationship between sepal_length & sepal_width

if chart_type == 'Scatter Plot':
  fig = px.scatter(iris_df,
                   x='sepal_length',
                   y='sepal_width',
                   color='species',
                   title='Iris Scatter Plot'
  )
  st.plotly_chart(fig)

# since line-charts typically require time-series data
# let's simpulate the line chart
elif chart_type == 'Line Chart':
  iris_df_sorted = iris_df.sort_values(by='sepal_length').reset_index()
  fig = px.line(iris_df_sorted,
                x=iris_df_sorted.index,
                y='sepal_length',
                color='species',
                title='Iris Sepal Length Line Chart'
  )
  st.plotly_chart(fig)

elif chart_type == 'Bar Chart':
  avg_sepal_length = iris_df.groupby('species')['sepal_length'].mean().reset_index()
  fig = px.bar(avg_sepal_length,
                x='species',
                y='sepal_length',
                title='Iris Sepal Length Line Chart'
  )
  st.plotly_chart(fig)

elif chart_type == 'Histogram':
  fig = px.histogram(iris_df,
                x='sepal_length',
                title='Iris Sepal Length Distribution'
  )
  st.plotly_chart(fig)

elif chart_type == 'Box Plot':
  fig = px.box(iris_df,
                x='species',
                y='sepal_length',
                title='Iris Sepal Length by Species'
  )
  st.plotly_chart(fig)

elif chart_type == 'Pie Chart':
  species_count = iris_df['species'].value_counts().reset_index()

  # st.write("species_count: ", species_count)
  st.dataframe(species_count)

  fig = px.pie(species_count,
                values='count',
                names='species',
                title='Iris Species Distribution'
  )
  st.plotly_chart(fig)

elif chart_type == '3D Scatter Plot':

  fig = px.scatter_3d(iris_df,
                x='sepal_length',
                y='sepal_width',
                z='petal_length',
                color='species',
                title='3D Scatter Plot'
  )
  st.plotly_chart(fig)


df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")

df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries

st.write(df.head())

fig = px.pie(df, values='pop', names='country', title='Population of European continent')
# fig.show()
st.plotly_chart(fig)



###############
# Graph Objects
#
import plotly.graph_objects as go   
import pandas as pd


# calculate a correlation matrix
corr = iris_df.iloc[:, :4].corr()

st.dataframe(corr)

fig = go.Figure(data=go.Heatmap(
                z=corr,
                x=corr.columns,
                y=corr.columns
))
fig.update_layout(title='heatmap of iris features correlation')
st.plotly_chart(fig)

