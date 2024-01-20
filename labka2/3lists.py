songs = ["Spinning Around", "Desert and Dust", "Natural", "Uninspirational"]
print (*songs, sep="\n")
print (songs[2], "- Third song")

songs[2] = "Neon Lights"
print (songs[2], "- Updated third song")

songs.append("Stop My Plans")
print (songs[-1], "- new song")

songs.insert(1, "I'm tired")
print (songs[1], "- inserted song to index 1")

songs.remove("Uninspirational")
print (songs[-2], ", Uninspirational removed")

print (songs[1:4])

print (len(songs), "many songs")
