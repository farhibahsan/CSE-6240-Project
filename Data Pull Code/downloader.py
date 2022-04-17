import postDownloader

sanders = [
    # ((1584322981, 1587001381), "sanders_apr_may.json"),
    # ((1581820980, 1584322980), "sanders_mar_apr.json"),
    ((1580619600, 1581820979), "sanders_feb_mar.json")
]

biden = [
    ((1593662401, 1597204800), "biden_jul_aug.json"),
    ((1591070401, 1593662400), "biden_jun_jul.json"),
    ((1588392001, 1591070400), "biden_may_jun.json"),
    ((1585800001, 1588392000), "biden_apr_may.json") #,
    # ((1583125201, 1585800000), "biden_mar_apr.json"),
    # ((1580619600, 1583125200), "biden_feb_mar.json")
]

for entry in sanders:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "sandersforpresident", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed sanders: ", entry[0])

for entry in biden:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "JoeBiden", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed biden: ", entry[0])