import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


map_df = gpd.read_file("data/nz-police-district-boundaries.shx")
licenses_df = pd.read_csv("data/nz_firearm_licenses.csv")

merged_df = map_df.merge(licenses_df, left_on=["DISTRICT_N"], right_on=["Residence District"])

merged_df.plot(column="Licenses", cmap="Blues", legend=True)

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

plt.savefig("nz_firearm_licenses.png", dpi=300)
plt.show()

