# string_slicing
# This file demonstrates Python string slicing with examples

# Original string
s = "HELLO PYTHON"

print("Original string:", s)

# Index reference
print("Forward slicing examples:")


print("s[0:5:1] =", s[0:5:1])  # HELLO


print("s[0:4:1] =", s[0:4:1])  # HELL


print("s[:4:1] =", s[:4:1])  # HELL


print("s[:5:] =", s[:5:])  # HELLO

# Reverse slicing examples
print("Reverse slicing examples:")


print("s[4::-1] =", s[4::-1])  # OLLEH


print("s[4:0:-1] =", s[4:0:-1])  # OLLE

# Full reverse
print("\nFull reverse string:")
print("s[::-1] =", s[::-1])  # NOHTYP OLLEH


print("\nDefault behavior examples:")
print("s[:] =", s[:])  # full string
print("s[::1] =", s[::1])  # full string
print("s[::2] =", s[::2])  # skip every second character

print("\nProgram finished successfully.")
