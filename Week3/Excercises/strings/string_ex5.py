ford = "ab0110100"
audi = "EEE 123123"
citroen  = "Zk-3d0300"
honda  = "AV12020"

ford = ford.upper()
audi = audi.replace(" ", "")
citroen = citroen.replace("-", "")
citroen = citroen.upper()
print(f"{ford} {audi} {citroen} {honda}")