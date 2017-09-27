import datetime
from bokeh.plotting import show, figure, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime.datetime(2016,11,1)
end=datetime.datetime(2017,3,10)

df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)

p=figure(x_axis_type="datetime",width=1000, height=300, responsive=True)
p.title.text="Candle stick charts"
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000

def inc_dec(o,c):
    if o<c:
        value="Increase"
    elif o>c:
        value="Decrease"
    else:
        value="Equal"
    return value

df["Status"]=[inc_dec(o,c) for o,c in zip(df.Open,df.Close)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(df.index[df.Status=="Increase"], df.Middle[df.Status=="Increase"] , hours_12,
       df.Height[df.Status=="Increase"],fill_color="#CCFFFF",line_color="black")

p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"], hours_12,
       df.Height[df.Status=="Decrease"], fill_color="#FF3333", line_color="black")

script1, div1 = components(p)
cdn_js=CDN.js_files
cdn_css=CDN.css_files

output_file("CS.html")
show(p