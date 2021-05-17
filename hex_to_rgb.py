def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0,2,4))

rgb = hex_to_rgb('FFA501')

print(rgb)