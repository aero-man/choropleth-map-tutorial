import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load New Zealand coordinates into Geopandas
map_df = gpd.read_file("data/nz-police-district-boundaries.shx")

# Load firearm license data into Pandas
licenses_df = pd.read_csv("data/nz_firearm_licenses.csv")

# Combine both dataframes along their district columns
merged_df = map_df.merge(licenses_df, left_on=["DISTRICT_N"], right_on=["Residence District"])

# Create a Matplotlib plot/map with the combined dataframe. Use the "Licenses" column to decide colors.
merged_df.plot(column="Licenses", cmap="Blues", legend=True)

# Change the title and format of the Matplotlib plot/map
plt.title("Firearm Licenses by Police District in New Zealand (July 2021)", y=1.04)
plt.tick_params(
    axis="both",        # affect both the X and Y
    which="both",       # get rid of both major and minor ticks
    top=False,          # get rid of ticks top/bottom/left/right
    bottom=False,
    left=False,
    right=False,
    labeltop=False,     # get rid of labels top/bottom/left/right
    labelbottom=False,
    labelleft=False,
    labelright=False)
plt.axis("off")
plt.subplots_adjust(right=0.85)

# Save and show the map
plt.savefig("nz_firearm_licenses.png", dpi=300)
plt.show()

