
# This one depends on your artist - the "entiure" scale for the object
scale = 4
# Offsets - this is for if you want your center axis to NOT be the real center
xoffset = 0
yoffset = 0
zoffset = 0  # -61 for my lightcycle to have the tyres be on the ground ;)

# This magic set of constants came from my GBA 3d engine code - 
# To be honest, I cannot remember where they came from, but things looked HORRIBLE without
# them
xscale = 1.0/10
yscale = 1.0/10
zscale = 1.0/10

# cull if not this long
#min_line_length = 0.3
min_line_length = 0.0
# Connect if this close
min_move = 0.00

# Should we try and turn triangles into quads?
# Our algo for this is _incredibly_ simple though, and relies on "well behaved" triangles ;)
#simple_quad_detect = True
simple_quad_detect = False

# Should we map materials to intensities?
# This isn't actually implemented yet, since it needs code
# on the 
use_intensity = False
intensity_material_map = {
  "Chassis": 0.5,
  "Hull": 1.0,
  "Window": 0.25 
}

# Ingore these materials - they're transparent...
ignore_materials = {
  "Window": True
}
