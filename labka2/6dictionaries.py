FavAlbums = {
    "AJR": "The Maybe Man",
    "ajr": "Ok Orchestra",
    "5SOS": "CALM",
    "Imagine Dragons": "Origins",
    "X Ambassadors": "The Beautiful Liar"
}

print (FavAlbums.get("5SOS"))

FavAlbums["5SOS"] = "5SOS5"
print (FavAlbums.get("5SOS"))

FavAlbums["Saint Motel"] = "saintmotelevision"
print (FavAlbums.get("Saint Motel"))

print(FavAlbums.get("ajr"))
FavAlbums.pop("ajr")
print(FavAlbums.get("ajr"))

FavAlbums.clear()
print (FavAlbums.get("AJR"))
