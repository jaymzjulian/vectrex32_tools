from svgpathtools import *
import sys,os,math,copy

paths,attributes = svg2paths(sys.argv[1])
 
# Path types:
#  Line(self,start,end) - unsupported
#  QuadraticBezier(self,start,control,end)  - supported
#  CubicBezier(self,start,control1,control2,end)  - supported
#  Arc(self,start,radius,rotation,large_arc,sweep,end,autoscale_radius=True) - unsupported?

# These are the tunables - this will cause the item to be exactly x * y
target_size_x = 512
target_size_y = 512
# Set target_commands to something super high is you just want to set acceptable_error
# So if you want "no more than N vectors", set target_coomands and acceptable_error to 0.0
# 
# If you want "no more than N error", set target_commands to 0, and acceptable_error to some other value
target_commands = 384
acceptable_error = 0.0

partial_commands = []


# Smooth lines - we'll fix it in post ;)
beizer_seg_count = 8

lx = -999
ly = -999
for path in paths:
  for item in path:
    if is_bezier_segment(item):
      myPath = []
      my_commands = []
      for i in range(beizer_seg_count):
        myPath.append(item.point(i/(float(beizer_seg_count)-1)))
      myPath.append(item.point(1.0))
      # Just always do this for now - we'll clean up the mess later when
      # we scale/clip!
      cmd = ['MoveTo', myPath[0].real, myPath[0].imag]
      my_commands.append(cmd)
      lx = myPath[0].real
      ly = myPath[0].imag
      for i in myPath[1:-1]:
        cmd = ['DrawTo', i.real, i.imag]
        my_commands.append(cmd)
        lx = i.real
        ly = i.imag
      partial_commands.append(my_commands)
    else:
      raise "Don't yet know how to handle "+str(type(item))

# Center the object and scale
# This all works on the partial_commands structure now, since that affects our
# intiial origin
minx = 9999999
maxx = -9999999
miny = 999999
maxy = -9999999
for i in partial_commands:
 for v in i:
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

for i in partial_commands:
 for v in range(len(i)):
  i[v][1] += shiftx
  i[v][2] += shifty
  i[v][1] *= scale_x
  i[v][2] *= scale_y

# For our master command list based on lowest move distance
work_commands = copy.copy(my_commands)
v32commands = []
lx = 0
ly = 0
while len(partial_commands) > 0:
  min_d = 999999
  wc = None
  for w in partial_commands:
    dist_x = w[0][1] - lx
    dist_y = w[0][2] - ly  
    d = math.sqrt(dist_x*dist_x + dist_y*dist_y)
    if min_d > d:
      min_d = d
      wc = w
  v32commands.extend(wc)
  partial_commands.remove(wc)
  lx = wc[-1][1]
  ly = wc[-1][2]

# Remove any drawto/moveto combos that are zero :)
removed = True
while removed:
  removed=False
  for v in reversed(range(len(v32commands)-1)):
    if v32commands[v][0] == "DrawTo" and v32commands[v+1][0]=="MoveTo":
      dist_x = v32commands[v][1] - v32commands[v+1][1]
      dist_y = v32commands[v][2] - v32commands[v+1][2]
      dist = math.sqrt(dist_x*dist_x + dist_y*dist_y)
      if dist < 0.01:
        removed = True
        del(v32commands[v+1])
        break

# Now clean up any draws which are less than acceptable error
iae = acceptable_error
while len(v32commands) > target_commands or (target_commands == 0 and iae == acceptable_error):
  print >>sys.stderr,"Trying error rate of",acceptable_error
  removed = True
  while removed:
    removed = False
    # Remove any big draws - if it's a MoveTo, hopefully it'll end up
    # linking up with the end of the next line...
    #
    # We do this backwards to try and encourage it to remove MoveTo commands before DrawTo commands
    for v in reversed(range(len(v32commands)-1)):
      dist_x = v32commands[v][1] - v32commands[v+1][1]
      dist_y = v32commands[v][2] - v32commands[v+1][2]
      dist = math.sqrt(dist_x*dist_x + dist_y*dist_y)
      if dist < acceptable_error:
        #print "Remove",v+1
        removed = True
        del(v32commands[v+1])
        break
  # Remove duplicate MoveTo commands
  removed = True
  while removed:
    removed = False
    for v in reversed(range(len(v32commands)-1)):
      if v32commands[v][0] == "MoveTo" and v32commands[v+1][0] == "MoveTo":
        removed = True
      del(v32commands[v])
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
