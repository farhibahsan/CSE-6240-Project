import postDownloader

sanders = [
    ((1583125201, 1585800000), "Data unzipped/sanders_mar_apr.json"),
    ((1580619600, 1583125200), "Data unzipped/sanders_feb_mar.json")
]

biden = [
    ((1583125201, 1585800000), "Data unzipped/biden_mar_apr.json"),
    ((1580619600, 1583125200), "Data unzipped/biden_feb_mar.json")
]

pol = [
    ((1581310800, 1581397199), "Data unzipped/politics_feb_10.json"),
    ((1581224400, 1581310799), "Data unzipped/politics_feb_9.json"),
    ((1581138000, 1581224399), "Data unzipped/politics_feb_8.json"),
    ((1581051600, 1581137999), "Data unzipped/politics_feb_7.json"),
    ((1580965200, 1581051599), "Data unzipped/politics_feb_6.json"),
    ((1580878800, 1580965199), "Data unzipped/politics_feb_5.json"),
    ((1580792400, 1580878799), "Data unzipped/politics_feb_4.json"),
    ((1580706000, 1580792399), "Data unzipped/politics_feb_3.json"),
    ((1580619600, 1580705999), "Data unzipped/politics_feb_2.json")
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