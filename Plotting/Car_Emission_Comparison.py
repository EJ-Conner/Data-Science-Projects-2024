import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cars.csv', usecols=[0, 1, 4])

ford_df = df[df['Car'] == 'Ford']
merc_df = df[df['Car'] == 'Mercedes']

ford_avg_emission = ford_df['CO2'].mean()
merc_avg_emission = merc_df['CO2'].mean()

fig, ax = plt.subplots(1, 2)

# Ford plot
ax[0].plot(ford_df['Model'], ford_df['CO2'], 'o', color='b', label='Ford CO$_2$', linestyle='-')
ax[0].axhline(y=ford_avg_emission, color='gray', linestyle='--', label='Average')
ax[0].set_title("Ford CO$_2$ Emissions")
ax[0].legend(loc='upper right')
ax[0].set_xlabel('Model')
ax[0].set_ylabel('CO$_2$')
ax[0].set_ylim(50, 150)
 

ax[1].plot(merc_df['Model'], merc_df['CO2'], 'o', color='r', label='Mercedes CO$_2$', linestyle='-')
ax[1].axhline(y=merc_avg_emission, color='gray', linestyle='--', label='Average')
ax[1].set_title("Mercedes CO$_2$ Emissions")
ax[1].legend(loc='upper right')
ax[1].set_xlabel('Model')
ax[1].set_ylabel('CO$_2$')
ax[1].set_ylim(50, 150)


plt.show()