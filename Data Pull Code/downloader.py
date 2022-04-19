import postDownloader

sanders = [
    ((1593662401, 1597204800), "Data unzipped/sanders_jul_aug.json"),
    ((1591070401, 1593662400), "Data unzipped/sanders_jun_jul.json"),
    ((1588392001, 1591070400), "Data unzipped/sanders_may_jun.json"),
    ((1585800001, 1588392000), "Data unzipped/sanders_apr_may.json"),
    ((1583125201, 1585800000), "Data unzipped/sanders_mar_apr.json"),
    ((1580619600, 1583125200), "Data unzipped/sanders_feb_mar.json")
]

biden = [
    ((1593662401, 1597204800), "Data unzipped/biden_jul_aug.json"),
    ((1591070401, 1593662400), "Data unzipped/biden_jun_jul.json"),
    ((1588392001, 1591070400), "Data unzipped/biden_may_jun.json"),
    ((1585800001, 1588392000), "Data unzipped/biden_apr_may.json"),
    ((1583125201, 1585800000), "Data unzipped/biden_mar_apr.json"),
    ((1580619600, 1583125200), "Data unzipped/biden_feb_mar.json")
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
    ((1582261200, 1582347599), "Data unzipped/politics_feb_21.json"),
    ((1582174800, 1582261199), "Data unzipped/politics_feb_20.json"),
    ((1582088400, 1582174799), "Data unzipped/politics_feb_19.json"),
    ((1582002000, 1582088399), "Data unzipped/politics_feb_18.json"),
    ((1581915600, 1582001999), "Data unzipped/politics_feb_17.json"),
    ((1581829200, 1581915499), "Data unzipped/politics_feb_16.json"),
    ((1581742800, 1581829199), "Data unzipped/politics_feb_15.json"),
    ((1581656400, 1581742799), "Data unzipped/politics_feb_14.json"),
    ((1581570000, 1581656399), "Data unzipped/politics_feb_13.json"),
    ((1581483600, 1581569999), "Data unzipped/politics_feb_12.json"),
    ((1581397200, 1581483599), "Data unzipped/politics_feb_11.json"),
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