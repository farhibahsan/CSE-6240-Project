import postDownloader

sanders = [
    ((1588392001, 1591070400), "Data/sanders_may_jun.json"),
    ((1585800001, 1588392000), "Data/sanders_apr_may.json")
]

biden = [
    ((1588392001, 1591070400), "Data/biden_may_jun.json"),
    ((1585800001, 1588392000), "Data/biden_apr_may.json")
]

pol = [
    ((1582174800, 1582261199), "Data/politics_feb_20.json"),
    ((1582088400, 1582174799), "Data/politics_feb_19.json"),
    ((1582002000, 1582088399), "Data/politics_feb_18.json"),
    ((1581915600, 1582001999), "Data/politics_feb_17.json"),
    ((1581829200, 1581915499), "Data/politics_feb_16.json"),
    ((1581742800, 1581829199), "Data/politics_feb_15.json"),
    ((1581656400, 1581742799), "Data/politics_feb_14.json"),
    ((1581570000, 1581656399), "Data/politics_feb_13.json"),
    ((1581483600, 1581569999), "Data/politics_feb_12.json"),
    ((1581397200, 1581483599), "Data/politics_feb_11.json")
]

for entry in sanders:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "sandersforpresident", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed sanders: ", entry[1])

for entry in biden:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "JoeBiden", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed biden: ", entry[1])

for entry in pol:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "politics", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed politics: ", entry[1])