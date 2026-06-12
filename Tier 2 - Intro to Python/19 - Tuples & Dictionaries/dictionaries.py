info = {
    "NAME": "RAY WONG",
    "AGE": "16",
    "IS_VERIFIED": True
}

print(info["NAME"])
print(info["AGE"])
print(info.get("BIRTHDAY", "June 22 2009"))
info["BIRTHDAY"] = "June 22 2009"