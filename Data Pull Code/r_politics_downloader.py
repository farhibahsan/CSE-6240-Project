import postDownloader

pol = [
    # ((1593662401, 1597204800), "politics_6.json"),
    # ((1591070401, 1593662400), "politics_5.json"),
    # ((1588392001, 1591070400), "politics_4.json"),
    # ((1585800001, 1588392000), "politics_3.json"),
    # ((1583125201, 1585800000), "politics_2.json"),
    ((1580619600, 1583125200), "politics_1.json")
]

for entry in pol:
    try:
        postDownloader.downloadFromUrl(entry[1], "comment", "politics", entry[0][0], entry[0][1])
    except Exception as err:
        print("Failed politics: ", entry[0])