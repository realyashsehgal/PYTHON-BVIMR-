from Signature_folder.Signature import sign
print("Byte Example")

b = bytes([65,66,67,68])
print(b)
print(b[0])
print(b[1])

for byte in b:
    print(byte,end=' ')

print("\n")

ba = bytearray([65,66,67,68])
print(ba)

ba[0] = 97
for byte in ba:
    print(byte,end=' ')
ba.append(1)
print(ba)

print("Converting byte array into byte")
b_converted = bytes(ba)
print(b_converted)

print("Memory view")
b_mv = bytes([65,66,67,68,69])

mv = memoryview(b_mv)
print(mv)

print("Slicing mv")
mv_slice = mv[1:4]
print(mv_slice)

print("Creating byte array of memory value")
ba_mv = bytearray([65,66,67,68,69])
mv_ba = memoryview(ba_mv)

print("modifying the ba_mv element")
mv_ba[0] = 97
print(ba_mv)
sign()