#!/usr/bin/python
import sys,math

if len(sys.argv) < 3:
  print "Usage:",sys.argv[0],"[configuration-file] [object-file] [object-name]"
  print "Example:",sys.argv[0],"standard-configuration.py lightcycle-low.kob lightcycle"
  sys.exit(1)
points = []

f = open(sys.argv[2]).readlines()
execfile(sys.argv[1])

lines = []
surfaces = []
current_i = 1.0
round_digits = 3
ignoring = False

print >> sys.stderr, "'loading obj data...."
for line in f:
  parts=line.split()
  if len(parts) > 0:
    if parts[0] == 'v':
      x=(float(parts[1])+float(xoffset))*float(xscale*scale)
      y=(float(parts[2])+float(yoffset))*float(yscale*scale)
      z=(float(parts[3])+float(zoffset))*float(zscale*scale)
      points.append([float(x),float(y),float(z)])
    elif parts[0] == 'l':
      for c in range(len(parts)-2):
        lines.append([int(parts[1+c]), int(parts[2+c])])
    elif parts[0] == 'f':
      if not ignoring:
        my_surface = []
        for c in range(len(parts)-1):
          my_surface.append(int(parts[1+c].split('/')[0])-1)
        surfaces.append(my_surface)
      #print " {MoveTo, %d,%d,%d}, _ " % (int(tripoints[0][0]), int(tripoints[0][1]), int(tripoints[0][2]))
      #for c in range(3):
      #  lines.append([int(tripoints[(c)%3][0]), int(tripoints[(c+1)%3][0])])
      #  print " {DrawTo, %d,%d,%d}, _ " % (int(tripoints[(c+1)%3][0]), int(tripoints[(c+1)%3][1]), int(tripoints[(c+1)%3][2]))
    elif parts[0] == 'usemtl':
      if parts[1].strip() in ignore_materials:
        ignoring = True
      else:
        ignoring  = False


for j in range(len(points)):
  for k in range(len(points)):
    if j!=k:
      differ = False
      for c in range(3):
        if round(points[j][c], round_digits) != round(points[k][c], round_digits):
           differ = True
      if not differ:
        print >>sys.stderr, "Points",points[j],"are the same as",points[k],"currently we dont dedupe this, but we should!"

# Find any obvious quads via a terrible, terribly slow algorythm
# What we're looking for here, is surfaces which share a common
# line between them - i.e. not just a point, but an entire line, which
# is also oriented the same way.  We can then assume that that line is
# superflous...
if simple_quad_detect:
  print >>sys.stderr, "'detecting quads...."
  found_quads = True
  while found_quads:
    found_quads = False
    for s1 in surfaces:
      for s2 in surfaces:
        if (not found_quads) and s1!=s2 and len(s1)==3 and len(s2)==3 and len(set(s1))==3 and len(set(s2))==3:  
          for c1 in range(3):
            for c2 in range(3):
              if s1[c1] == s2[c2] and (s1[(c1+1)%3] == s2[(c2+1)%3] or s1[(c1+1)%3] == s2[(c2-1)%3]):
                # Find all of our line segments
                my_lines = []
                for ql in range(3):
                  if ql!=c1:
                    my_lines.append([s1[ql], s1[(ql+1)%3]])
                for ql in range(3):
                  if (((s1[(c1+1)%3] == s2[(c2+1)%3]) and ql!=c2) or
                     ((s1[(c1+1)%3] == s2[(c2-1)%3]) and ql!=((c2-1)%3))):
                    my_lines.append([s2[ql], s2[(ql+1)%3]])
                #print s1,s2,"is a quad of ",my_lines
                surfaces.remove(s1)
                surfaces.remove(s2)
                # Just output them straight to the line list, rather than trying to
                # turn them back into a poly!
                lines+=my_lines
                found_quads = True

# Turn the remaining surfaces into lines
print >>sys.stderr, "Loading surfaces..."
for s in surfaces:
  for c in range(len(s)):
    lines.append([s[c], s[(c+1)%len(s)]])


# first remove dupes from lines
# both dupe lines and empty draws
nl = []
lines = sorted(lines)
ll=[0,0]
print >>sys.stderr, "Eliminating lines.... starting with",len(lines)
for l in lines:
  # also cull too short lines
  lx = points[l[0]][0] - points[l[1]][0]
  ly = points[l[0]][1] - points[l[1]][1]
  lz = points[l[0]][2] - points[l[1]][2]
  llength = math.sqrt(lx*lx+ly*ly+lz*lz)
  if llength > min_line_length and ll!=l:
    if [points[l[0]][0], points[l[0]][1], points[l[0]][2]] != [points[l[1]][0], points[l[1]][1], points[l[1]][2]]:
      dupe = False
      for ol in nl:
        if sorted(ol) == sorted(l):
          dupe = True
      if dupe:
        print >>sys.stderr, "Eliminated",l,"due to match in draw list!"
      else:
        nl.append(l)
    else:
      print >>sys.stderr, "Eliminated",l,"due to previous point being identical"
  else:
    if ll==l:
      print >>sys.stderr, "Eliminated",l,"due to too dupe with",ll
    else:
      print >>sys.stderr, "Eliminated",l,"due to too short at",llength
  ll = l
lines = nl
print >>sys.stderr,"... ending with",len(lines)

# Now generate the sprite
lastpoint = -1
last_draw_command = None
print "function "+sys.argv[3]+"()"
print "mysprite={ _"
first_move = True
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
      # choose the closest item, in an attempt to avoid pen drift!  Instead, right now we're just choosing
      # an arbitary one...
      min_d = 99999.0
      for l in lines:
        my_d = 0
        for c in range(3):
          my_d += (points[l[0]][c]-points[lastpoint][c])**2
        if my_d < min_d:
          line_seg = l
          min_d = my_d
      # shove things into holding places
      l = line_seg
      actual_l = l
      if min_d >= min_move or first_move:
        first_move = False
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
