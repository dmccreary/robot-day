# Dimensions of the display
width = 128
height = 64

# Total number of pixels
total_pixels = width * height
print('Total Pixels:', total_pixels)

# Total number of bits (since 1 pixel = 1 bit)
total_bits = total_pixels

# Convert bits to bytes (1 byte = 8 bits)
total_bytes = total_bits / 8

# Convert bytes to kilobytes (1 kilobyte = 1024 bytes)
total_kilobytes = total_bytes / 1024
print('Total Kilobytes:', total_kilobytes)
