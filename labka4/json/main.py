import json
import texttable

file = open(r"labka4\json\sample-data.json", "r")

jsonfile = json.loads(file.read())
print(jsonfile["totalCount"])


print("Interface Status")
print("="*100)

mytable = texttable.Texttable(200)
mytable.add_row([
    "DN", "Description", "Speed", "MTU"
])
mytable.set_deco(texttable.Texttable.HEADER)

mytable.add_row([
    "-"*45, "-"*15, "-"*10, "-"*5
])

imdata = jsonfile["imdata"]
for onedata in imdata:
    onedata_attri = onedata["l1PhysIf"]["attributes"]
    mytable.add_row([onedata_attri["dn"], onedata_attri["descr"], onedata_attri["speed"], onedata_attri["mtu"]])

print(mytable.draw())