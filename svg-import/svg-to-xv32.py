from svgpathtools import *
import sys,os,math,copy

paths,attributes = svg2paths(sys.argv[1])
OUTPUT_TYPE_FUNCTION = 1
OUTPUT_TYPE_COMMANDS = 2

execfile(sys.argv[2])
 
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
      # Set this to ridiculous values, so that the first
      # result is always new - then since the saved angle is from this,
      # we also _always_ get an endpoint...
      lx = 999
      ly = 999
      la = 999
      for i in range(beizer_seg_count):
        # get our point, and work out the angle of the line we'd draw
        p = item.point(i/(float(beizer_seg_count)-1))
        mx = p.real
        my = p.imag
        ang = math.atan2(my-ly, mx-lx)
        ang_change = abs(la - ang)
        #print "ang change:",ang_change
        # if the angle is changing more than our threashold, create a new
        # point, otherwise adjust the previous one
        if ang_change < angle_error:
          myPath[-1] = item.point(i/(float(beizer_seg_count)-1))
        else:
          myPath.append(item.point(i/(float(beizer_seg_count)-1)))
          lx = mx
          ly = my
          la = ang
      myPath.append(item.point(1.0))
      #print len(myPath)
      #print myPath

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
      #sys.exit(1)
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
if output_type == OUTPUT_TYPE_FUNCTION:
  print "function ",sys.argv[3]+"()"
  print "  mysprite = { _"
  for v in v32commands:
    if v == v32commands[-1]:
      print "    {",v[0],",",v[1],",",0-v[2],"} _"
    else:
      print "    {",v[0],",",v[1],",",0-v[2],"}, _"
  print "  }"
  print "  return mysprite"
  print "endfunction"
else:
  print "sub ",sys.argv[3]+"()"
  print "  call LinesSprite({ _"
  rto_count = 0
  for v in v32commands:
    rto_count += 1
    if v == v32commands[-1] or rto_count == origin_return_commands:
      print "    {",v[0],",",v[1],",",0-v[2],"} _"
    else:
      print "    {",v[0],",",v[1],",",0-v[2],"}, _"
    if rto_count == origin_return_commands and v!=v32commands[-1]:
      print "  })"
      print "  call ReturnToOriginSprite()"
      print "  call LinesSprite({ _"
      print "    {MoveTo,",v[1],",",0-v[2],"}, _"
      rto_count = 0
  print "  })"
  print "endsub"
