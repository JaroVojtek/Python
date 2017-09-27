from bokeh.plotting import figure, output_file, show

p=figure(plot_width=500, plot_height=400)

p.title.text="Earthquake"
p.title.text_color="Orange"
p.title.text_font="times"
p.title.text_font_style="italic"

p.yaxis.minor_tick_line_color=None

p.xaxis.axis_label="Time"
p.yaxis.axis_label="Value"

p.circle([1,2,3,4,5],[5,6,4,5,3],size = [8,12,14,15,20], color="red", alpha=0.5)

output_file("Scatter_plotting.html")
show(p)