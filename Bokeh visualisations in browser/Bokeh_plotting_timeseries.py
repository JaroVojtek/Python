from bokeh.plotting import figure, output_file, show
import pandas

df=pandas.read_csv("http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv",parse_dates=["Date"])

p=figure(width=1000,height=500,x_axis_type="datetime",responsive=True)

p.line(df["Date"],df["Close"],color="Orange",alpha=0.5)

output_file("Timeseries.html")
show(p)