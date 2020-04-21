def easyLatLng(row):
    of = row.office
    return {
        "latitude":of["coordinates"][1],
        "longitude":of["coordinates"][0]
    }
def easyLatLng2(row):
    of = row
    return {
        "latitude":of["coordinates"][1],
        "longitude":of["coordinates"][0]
    }