import matplotlib.pyplot as plt
import geopandas

filename = 'custom.geo.json'
with open(filename) as f:
    df = geopandas.read_file(f)
    print(df.head())
    df = df.rename(columns={'geometry': 'borders'})
    print(df.shape)
    df.insert(1, "test", "default")
    df['test'][1] = "change"
    print(df.head())

    # df.plot()
    # plt.show()