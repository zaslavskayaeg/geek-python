byte_string = b"Hello, world!"
simple_string = "Hello, world!"
byte_array_string = bytearray(byte_string)

print(byte_string)
print(type(simple_string), type(byte_string), type(byte_array_string))

name = "John"
byte_name = name.encode("UTF-8")
print(type(byte_name))
 