# Dimensions of the color watcih display
width = 240
height = 240

# Total number of pixels
total_pixels = width * height
print('Total Pixels:', total_pixels)

# Total number of bits (since 1 pixel = 16 bit)
total_bits = 16 * total_pixels

# Convert bits to bytes (1 byte = 8 bits)
total_bytes = total_bits / 8

# Convert bytes to kilobytes (1 kilobyte = 1024 bytes)
total_kilobytes = total_bytes / 1024
print('Total Kilobytes:', total_kilobytes)

print('rows of 16:', total_kilobytes / 16)
