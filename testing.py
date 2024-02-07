b_data = b'hello'

# bytearray
ba_data = bytearray(b'hello')
ba_data[0] = 65  # Change 'h' to 'A'

# memoryview
mv_data = memoryview(ba_data)
print(mv_data, ba_data, b_data )