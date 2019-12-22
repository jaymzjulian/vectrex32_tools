from svgpathtools import *
import sys,os,math

paths,attributes = svg2paths(sys.argv[1])
 
# Path types:
#  Line(self,start,end)  
#  QuadraticBezier(self,start,control,end) 
#  CubicBezier(self,start,control1,control2,end) 
#  Arc(self,start,radius,rotation,large_arc,sweep,end,autoscale_radius=True) 
#  Path(self,*segments,**kw)

# Chunky lines ;)
beizer_seg_count = 4
round_digits = 2
target_size_x = 64
target_size_y = 64
acceptable_error = 1.0

v32commands = []

lx = -999
ly = -999
for path in paths:
  for item in path:
    if is_bezier_segment(item):
      myPath = []
      for i in range(beizer_seg_count):
        myPath.append(item.point(i/(float(beizer_seg_count)-1)))
      myPath.append(item.point(1.0))
      # Just always do this for now - we'll clean up the mess later when
      # we scale/clip!
      cmd = ['MoveTo', myPath[0].real, myPath[0].imag]
      v32commands.append(cmd)
      lx = myPath[0].real
      ly = myPath[0].imag
      for i in myPath[1:-1]:
        cmd = ['DrawTo', i.real, i.imag]
        v32commands.append(cmd)
        lx = i.real
        ly = i.imag
    else:
      raise "Don't yet know how to handle "+str(type(item))

# Center the object and scale
minx = 9999999
maxx = -9999999
miny = 999999
maxy = -9999999
for v in v32commands:
  if v[1] < minx:
    minx = v[1]
  if v[2] < miny:
    miny = v[2]
  if v[1] > maxx:
    maxx = v[1]
  if v[2] > maxy:
    maxy = v[2]
osx = maxx-minx
osy = maxy-miny

shiftx = (0-osx/2) - minx
shifty = (0-osx/2) - miny
scale_x = float(target_size_x)/osx
scale_y = float(target_size_y)/osy

for v in range(len(v32commands)):
  v32commands[v][1] += shiftx
  v32commands[v][2] += shifty
  v32commands[v][1] *= scale_x
  v32commands[v][2] *= scale_y

# Now clean up any draws which are less than acceptable error
removed = True
while removed:
  removed = False
  for v in range(len(v32commands)-1):
    dist_x = v32commands[v][1] - v32commands[v+1][1]
    dist_y = v32commands[v][2] - v32commands[v+1][2]
    dist = math.sqrt(dist_x*dist_x + dist_y*dist_y)
    # Break after this, to ensure we don't corrupt the array...
    if dist < acceptable_error:
      removed = True
      #print "Remove",v+1
      del(v32commands[v+1])
      break

print "function ",sys.argv[2]
for v in v32commands:
  print v
