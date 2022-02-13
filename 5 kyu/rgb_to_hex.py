def rgb(r, g, b):
    r, g, b = max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255))
    return f"{r:02x}{g:02x}{b:02x}".upper()

print(rgb(255, 255, 255))