"""A set of exercises with matplotlib"""
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8,6))

def draw_co2_plot():
    """
    Here is some chemistry data

      Time (decade): 0, 1, 2, 3, 4, 5, 6
      CO2 concentration (ppm): 250, 265, 272, 260, 300, 320, 389

    Create a line graph of CO2 versus time, the line should be a blue dashed
    line. Add a title and axis titles to the plot.
    """
    x = np.arange(0,7)
    y = [250,265,272,260,300,320,389]
    ax.plot(x, y, color='green', ls='dashed',label='time and co2')
    
    

    
def draw_equations_plot():
    """
    Plot the following lines on the same plot

      y=cos(x) coloured in red with dashed lines
      y=x^2 coloured in blue with linewidth 3
      y=exp(-x^2) coloured in black

    Add a legend, title for the x-axis and a title to the curve, the x-axis
    should range from -4 to 4 (with 50 points) and the y axis should range 
    from 0 to 2. The figure should have a size of 8x6 inches.
    """
    
    x = np.linspace(-4,4,50)
    y = np.arange(0,2)
    y0 = np.cos(x)
    y1 = np.power(x,2)
    y2 = np.exp(np.power(-x,2))
   
    ax.plot(x, y0, color='red',ls='dashed', label='y = cos(x)')
    ax.plot(x, y1, color='blue', markersize=3, label='y = x^2')
    ax.plot(x, y2, color='black', ls='dashed', label='y=exp(-x^2)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Title')
    ax.legend(loc=1)
    
    
    
draw_co2_plot()
draw_equations_plot()
