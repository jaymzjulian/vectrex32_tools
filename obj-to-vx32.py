#!/usr/bin/python
import sys

if len(sys.argv) < 3:
  print "Usage:",sys.argv[0],"[configuration-file] [object-file] [object-name]"
  print "Example:",sys.argv[0],"standard-configuration.py lightcycle-low.kob lightcycle"
  sys.exit(1)
points = []

f = open(sys.argv[2]).readlines()
execfile(sys.argv[1])

lines = []
current_i = 1.0
ignoring = False

for line in f:
  parts=line.split()
  if len(parts) > 0:
    if parts[0] == 'v':
      x=(float(parts[1])+float(xoffset))*float(xscale*scale)
      y=(float(parts[3])+float(yoffset))*float(yscale*scale)
      z=(float(parts[2])+float(zoffset))*float(zscale*scale)
      points.append([float(x),float(y),float(z)])
    elif parts[0] == 'f':
      for c in range(len(parts)-1):
        lines.append([int(parts[1+c].split('/')[0])-1 , int(parts[1+((c+1)%3)].split('/')[0])-1, current_i])
      #print " {MoveTo, %d,%d,%d}, _ " % (int(tripoints[0][0]), int(tripoints[0][1]), int(tripoints[0][2]))
      #for c in range(3):
      #  lines.append([int(tripoints[(c)%3][0]), int(tripoints[(c+1)%3][0])])
      #  print " {DrawTo, %d,%d,%d}, _ " % (int(tripoints[(c+1)%3][0]), int(tripoints[(c+1)%3][1]), int(tripoints[(c+1)%3][2]))
    elif parts[0] == 'usemtl':
      if parts[1].strip() in ignore_materials:
        ignoring = True
      else:
        ignoring = False

# first remove dupes from lines
# both dupe lines and empty draws
nl = []
lines = sorted(lines)
ll=[0,0]
for l in lines:
  if ll!=l:
    if [points[l[0]][0], points[l[0]][1], points[l[0]][2]] != [points[l[1]][0], points[l[1]][1], points[l[1]][2]]:
      nl.append(l)
  ll = l
lines = nl

# Now generate the sprite
lastpoint = -1
last_draw_command = None
print "function "+sys.argv[3]+"()"
print "mysprite={ _"
while len(lines)>0:
  # Try and find something that matches the end of the last endpoint
  line_seg = None
  actual_l = None
  for l in lines:
    if l[0] == lastpoint:
      line_seg = l
      actual_l = l
  # If we didnt find one, try flipped - vectrex dont care!
  if line_seg == None:
    for l in lines:
      if l[1] == lastpoint:
        line_seg = [l[1],l[0]]
        actual_l = l

  # Dont repeat ourselves
  # also this is bad, but we used l below, so we need to shove line seg back into that...
  l = line_seg
  #if l!=None and last_draw_command != [points[l[0]][0], points[l[0]][1], points[l[0]][2], points[l[1]][0], points[l[1]][1], points[l[1]][2]]:
  if 0==0:
    if line_seg == None:
      line_seg = lines[0]
      l = line_seg
      actual_l = l
      print "  {MoveTo,%f,%f,%f}," % (points[l[0]][0], points[l[0]][1], points[l[0]][2]),
    print "  {DrawTo, %f,%f,%f}" % (points[l[1]][0], points[l[1]][1], points[l[1]][2]),
  last_draw_command = [points[l[0]][0], points[l[0]][1], points[l[0]][2], points[l[1]][0], points[l[1]][1], points[l[1]][2]]
  lastpoint = l[1]
  lines = filter(lambda a: a != actual_l, lines)
  if len(lines)>0:
    print ", _" 
    
print "}"
print "  return mysprite"
print "endfunction"
