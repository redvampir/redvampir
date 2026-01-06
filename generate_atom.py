from PIL import Image, ImageDraw, ImageFilter
import math, random

# Resolution: exact 21:9 (width x height)
W, H = 2520, 1080
cx, cy = W//2, H//2

def radial_glow(base, radius, color, intensity=0.6):
    layer = Image.new("RGBA", base.size, (0,0,0,0))
    draw = ImageDraw.Draw(layer)
    for r in range(radius, 0, -10):
        a = int(255 * (intensity * (1 - r / radius)))
        draw.ellipse((cx-r, cy-r, cx+r, cy+r), fill=color+(a,))
    return layer.filter(ImageFilter.GaussianBlur(radius/6))

img = Image.new("RGBA", (W, H), (6, 10, 25, 255))
# subtle background vignette
bg = Image.new("RGBA", (W, H), (0,0,0,0))
d = ImageDraw.Draw(bg)
for i in range(10):
    alpha = int(80 * (i/10))
    d.ellipse(( -i*200, -i*80, W+i*200, H+i*80), fill=(10,14,40, alpha))
img = Image.alpha_composite(img, bg)

# energy rays layer
rays = Image.new("RGBA", (W, H), (0,0,0,0))
dr = ImageDraw.Draw(rays)
num_rays = 120
for i in range(num_rays):
    angle = (i / num_rays) * math.pi * 2
    length = random.uniform(W*0.35, W*0.6)
    x2 = cx + math.cos(angle) * length
    y2 = cy + math.sin(angle) * length
    a = int(random.uniform(30,90))
    dr.line((cx, cy, x2, y2), fill=(200,220,255,a), width=1)
rays = rays.filter(ImageFilter.GaussianBlur(6))
img = Image.alpha_composite(img, rays)

# draw orbitals
orbits = Image.new("RGBA", (W, H), (0,0,0,0))
do = ImageDraw.Draw(orbits)
orbit_specs = [ (650,220, 0.0), (900,300, math.radians(25)), (1150,380, math.radians(-18)) ]
for a,b,rot in orbit_specs:
    layer = Image.new("RGBA", (W, H), (0,0,0,0))
    dl = ImageDraw.Draw(layer)
    bbox = (cx-a, cy-b, cx+a, cy+b)
    dl.ellipse(bbox, outline=(160,200,255,180), width=3)
    layer = layer.rotate(math.degrees(rot), center=(cx,cy), resample=Image.BICUBIC)
    layer = layer.filter(ImageFilter.GaussianBlur(2))
    orbits = Image.alpha_composite(orbits, layer)
img = Image.alpha_composite(img, orbits)

# electrons on orbits
elecs = Image.new("RGBA", (W, H), (0,0,0,0))
delc = ImageDraw.Draw(elecs)
positions = [ (0.1,0), (2.0,1), (4.0,2) ]
for idx,(a,b,rot) in enumerate(orbit_specs):
    for k in range(3):
        t = random.uniform(0, 2*math.pi)
        # param for rotated ellipse
        theta = rot
        a_r = a
        b_r = b
        x = cx + a_r*math.cos(t)*math.cos(theta) - b_r*math.sin(t)*math.sin(theta)
        y = cy + a_r*math.cos(t)*math.sin(theta) + b_r*math.sin(t)*math.cos(theta)
        r = 14 + idx*3
        delc.ellipse((x-r, y-r, x+r, y+r), fill=(255,240,180,255))
        # small glow
        delc.ellipse((x-r*2, y-r*2, x+r*2, y+r*2), fill=(255,220,120,18))

img = Image.alpha_composite(img, elecs)

# nucleus: layered glow
nuc = Image.new("RGBA", (W, H), (0,0,0,0))
dn = ImageDraw.Draw(nuc)
dn.ellipse((cx-60, cy-60, cx+60, cy+60), fill=(255,200,80,255))
# inner brighter core
dn.ellipse((cx-28, cy-28, cx+28, cy+28), fill=(255,250,220,255))

nuc = nuc.filter(ImageFilter.GaussianBlur(6))
img = Image.alpha_composite(img, nuc)
# add concentrated core
core = Image.new("RGBA", (W, H), (0,0,0,0))
dc = ImageDraw.Draw(core)
dc.ellipse((cx-18, cy-18, cx+18, cy+18), fill=(255,255,230,255))
img = Image.alpha_composite(img, core)

# final color grading
final = Image.new("RGBA", (W, H), (0,0,0,0))
fg = Image.new("RGB", (W, H))
fg.paste(img, (0,0), img)

# save
out_name = "atom_emission_21-9.png"
fg.save(out_name, "PNG")
print(f"Saved {out_name} ({W}x{H})")
