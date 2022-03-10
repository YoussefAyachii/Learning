import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# to check package version use __version__:
pd.__version__

"""
Matplotlib plots data on a Figure which contain one or more Axes.

Artist = (object) everything visible on the Figure is an Artist (even Figure,
Axes, and Axis objects).
When the Figure is displayed, all of the Artists are drawn to the canvas.

Figure = (Class) The whole figure. The Figure keeps track of all the child Axes.

Axes = (Class) an area where points can be specified through their coordinates.
An Axes is an Artist attached to a Figure that contains a region for plotting data.
Each Axes has one or more Axis objects (two Axis when 2d plot: x and y).
Each Axes also has:
    - title (set via set_title())
    - x-label (set via set_xlabel())
    - y-label (set via set_ylabel()).
The Axes contains most of the figure elements: Axis, Tick, Line2D, Text,
Polygon, etc., and sets the coordinate system.

Axis = (Object) set the scale, the limits and generate ticks (the marks on
the Axis) and ticklabels (strings labeling the ticks).
The location of the ticks is determined by a Locator object and the ticklabel
strings are formatted by a Formatter.
The combination of the correct Locator and Formatter gives very fine control
over the tick locations and labels.

Most Artists are tied to an Axes; such an Artist cannot be shared by multiple
Axes, or moved from one to another.

It is often convenient to create the Axes together with the Figure but
it is not mandatory.

"""

# create an empty figure with no Axes
fig = plt.figure()
type(fig)  # matplotlib.figure.Figure

# create a Figure containing a single Axes
# rk: subplots() arguments: nrows, ncols have default=1
fig, ax = plt.subplots(nrows=1, ncols=1)
fig, ax = plt.subplots()
type(ax)  # matplotlib.axes._subplots.AxesSubplot

# create a Figure containing 4 same Axes: axs will be the same for the 4 subf.
fig, ax = plt.subplots(nrows=2,ncols=2)
type(ax)  # numpy.ndarray of shape (2, 2)

# create a Figure with different Axes
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1,ncols=3)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=1,ncols=3)

# plot data on the Axes, i.e. add points on the Axes using x-y coordinates
ax.plot(x, y)

"""
Plotting functions

Common convention is to convert these to numpy.array objects prior to plotting.

Matplotlib needs to execute all the plots commands together in order to build
the corresponding plots.

"""

# covert to np array
a = np.asarray([3, 5, 2, 1])
b = np.asarray([2, 3, 4, 5])
c = np.asarray([3, 2, 3, 4])
d = np.asarray([3, 6, 4, 4])

# specify the whole figure (Figure object) size (in terms of proportions)
# the following lines of code have to be executed simultaneously.
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.5))
ax1.plot(a, b)
ax2.plot(a, c)

# add multiple data on the same graph
fig, ax = plt.subplots()
ax.plot(a, b)
ax.plot(a, c)
ax.plot(a, d)

"""
matplotlib.pyplot`: it is Matplotlib's scripting layer. Each `pyplot` function
makes some change to a figure: e.g., creates a figure, creates a plotting area
in a figure, plots some lines in a plotting area,...
"""

# list of styles for matplotlib.pyplot
plt.style.available

# choose a style to matplot lib
plt.style.use(["ggplot"])

# dataset loading
df = pd.read_excel(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/"+\
    "IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/"+\
    "Canada.xlsx",
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
    )

# filter dataframe by label: set_index is needed
df.set_index("OdName", inplace=True)
df_alg = df.loc["Algeria"]

# plot: best way is to define a function then execute it
def plot_alg():
    plt.plot(df_alg[range(1980, 2013, 1)])
    plt.title("title")
    plt.xlabel("xlab")
    plt.ylabel("ylab")
    plt.text(1985, 5000, '2010 Earthquake')

plot_alg()

# use fig, ax
def fig_alg():
    fig, ax1 = plt.subplots(nrows=1, ncols=1)
    ax1.plot(df_alg[range(1980, 2013, 1)])

fig_alg()

"""
Plots:
Line plot, all of which can be accessed by passing kind keyword to plot().
The full list of available plots are as follows:
-bar for vertical
-barh for horizontal bar plots
-hist for histogram
-box for boxplot
-kde or density for density plots
-area for area plots
-pie for pie plots
-scatter for scatter plots
-hexbin for hexbin plot
"""






