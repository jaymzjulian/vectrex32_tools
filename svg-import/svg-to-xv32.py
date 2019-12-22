from svgpathtools import *
import sys,os,math

paths,attributes = svg2paths(sys.argv[1])
 
# Path types:
#  Line(self,start,end) - unsupported
#  QuadraticBezier(self,start,control,end)  - supported
#  CubicBezier(self,start,control1,control2,end)  - supported
#  Arc(self,start,radius,rotation,large_arc,sweep,end,autoscale_radius=True) - unsupported?

# These are the tunables - this will cause the item to be exactly x * y
target_size_x = 256
target_size_y = 256
# Set target_commands to something super high is you just want to set acceptable_error
# So if you want "no more than N vectors", set target_coomands and acceptable_error to 0.0
# 
# If you want "no more than N error", set target_commands to 0, and acceptable_error to some other value
target_commands = 256
acceptable_error = 0.0

v32commands = []


# Smooth lines - we'll fix it in post ;)
beizer_seg_count = 8

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
iae = acceptable_error
while len(v32commands) > target_commands or (target_commands == 0 and iae == acceptable_error):
  print >>sys.stderr,"Trying error rate of",acceptable_error
  removed = True
  while removed:
    removed = False
    # Remove over-moves first...
    for v in range(len(v32commands)-1):
      if v32commands[v+1][0]=="MoveTo":
        dist_x = v32commands[v][1] - v32commands[v+1][1]
        dist_y = v32commands[v][2] - v32commands[v+1][2]
        dist = math.sqrt(dist_x*dist_x + dist_y*dist_y)
        if dist < acceptable_error:
          #print "Remove",v+1
          removed = True
          del(v32commands[v+1])
          break
    # Having done that, we remove any under-draws which are NOT preceeded by a moveto
    # This causes us to NOT actually remove any lines, which we were totally doing....
    if not removed:
      for v in range(len(v32commands)-1):
        if v32commands[v][0]=="DrawTo":
          dist_x = v32commands[v][1] - v32commands[v+1][1]
          dist_y = v32commands[v][2] - v32commands[v+1][2]
          dist = math.sqrt(dist_x*dist_x + dist_y*dist_y)
          # Break after this, to ensure we don't corrupt the array...
          if dist < acceptable_error:
            removed = True
            #print "Remove",v+1
            del(v32commands[v+1])
            break
  print >>sys.stderr,"Vectors:",len(v32commands)
  acceptable_error += 0.1

print "' final acceptable error:",acceptable_error
print "' final command count:",len(v32commands)
print "function ",sys.argv[2]+"()"
print "  mysprite = { _"
for v in v32commands:
  if v == v32commands[-1]:
    print "    {",v[0],",",v[1],",",0-v[2],"} _"
  else:
    print "    {",v[0],",",v[1],",",0-v[2],"}, _"
print "  }"
print "  return mysprite"
print "endfunction"
