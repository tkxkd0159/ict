import matplotlib.pyplot as plt
import geopandas


filename = 'custom.geo.json'
with open(filename) as f:
    df = geopandas.read_file(f)
    print(df.head())
    print(df.shape)

    df.insert(1, "test", "default")
    # df = df.rename(columns={'test': 'new_test'})

    df['test'][1] = "change"
    print(df.head())

    # df.to_file('.\\my.json', driver="GeoJSON")
    # df.plot()
    # plt.show()

with open('my.json') as f2:
    df2 = geopandas.read_file('my.json')
    print(df2["iso_a3"])