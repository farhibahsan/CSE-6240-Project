import postDownloader

sanders = [
    ((1593662401, 1597204800), "Data unzipped/sanders_jul_aug.json"),
    ((1591070401, 1593662400), "Data unzipped/sanders_jun_jul.json")
]

biden = [
    ((1593662401, 1597204800), "Data unzipped/biden_jul_aug.json"),
    ((1591070401, 1593662400), "Data unzipped/biden_jun_jul.json")
]

pol = [
    ((1583038800, 1583125199), "Data unzipped/politics_mar_2.json"),
    ((1582952400, 1583038799), "Data unzipped/politics_mar_1.json"),
    ((1582866000, 1582952399), "Data unzipped/politics_feb_28.json"),
    ((1582779600, 1582865999), "Data unzipped/politics_feb_27.json"),
    ((1582693200, 1582779599), "Data unzipped/politics_feb_26.json"),
    ((1582606800, 1582693199), "Data unzipped/politics_feb_25.json"),
    ((1582520400, 1582606799), "Data unzipped/politics_feb_24.json"),
    ((1582434000, 1582520399), "Data unzipped/politics_feb_23.json"),
    ((1582347600, 1582433999), "Data unzipped/politics_feb_22.json"),
    ((1582261200, 1582347599), "Data unzipped/politics_feb_21.json")
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