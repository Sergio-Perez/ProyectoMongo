def easyLatLng(row):
    of = row.office
    return {
        "longitude":of["coordinates"][0]
        "latitude":of["coordinates"][1],
        
    }
def easyLatLng2(row):
    of = row
    return {
        "longitude":of["coordinates"][0]
        "latitude":of["coordinates"][1],
    }