from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_excel("verlegenhuken.xlsx")

p=figure()
p.title.text="Temperature and Air Pressure"
p.xaxis.axis_label="Temperature (°C)"
p.yaxis.axis_label="Pressure (hPa)"

p.circle(df["Temperature"]/10,df["Pressure"]/10)
show(p)