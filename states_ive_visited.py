import matplotlib.pyplot as plt
import matplotlib.cm

from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

# Size of the map
fig, ax = plt.subplots(figsize=(20,20))

# Making the boder of the U.S and the states within
m =  Basemap(resolution='l', #c, l, i, h, f or None
             projection='lcc',
             lat_1=33, lat_2=45, lon_0=-95,
             llcrnrlon=-119, llcrnrlat=22, urcrnrlon=-64, urcrnrlat=49)
m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
m.drawcoastlines()
m.readshapefile('st99_d00', name= 'states', drawbounds= True)


state_names = []
for shape_dict in m.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance

# Use a while loop to continue asking ? or strip the ,
print('Have you been to any states? (yes or no)')
decision = input().lower()
while decision != 'no':
    if decision == 'yes':
        print('What states have you been to?')
        answer = input().title()

        # Coloring of the states
        seg = m.states[state_names.index(answer)]
        poly = Polygon(seg, color='purple', fill=True)
        ax.add_patch(poly)

        print('Have you been to anymore states? (yes or no)')
        decision = input().lower()
        if decision == 'no':
            print('Here is your map.')
            break

plt.title("States I've Visited")
plt.show()


