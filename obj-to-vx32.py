#!/usr/bin/python
import sys,math

if len(sys.argv) < 3:
  print "Usage:",sys.argv[0],"[configuration-file] [object-file] [object-name]"
  print "Example:",sys.argv[0],"standard-configuration.py lightcycle-low.kob lightcycle"
  sys.exit(1)
points = []
normals = []

f = open(sys.argv[2]).readlines()
execfile(sys.argv[1])

lines = []
surfaces = []
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
    elif parts[0] == 'vn':
      x=float(parts[1])
      y=float(parts[3])
      z=float(parts[2])
      normals.append([float(x),float(y),float(z)])
    elif parts[0] == 'f':
      if not ignoring:
        my_surface = []
        for c in range(len(parts)-1):
          if include_normals:
            my_surface.append([int(parts[1+c].split('/')[0])-1, int(parts[1+c].split('/')[2])-1])
          else:
            my_surface.append([int(parts[1+c].split('/')[0])-1, 0])
        surfaces.append(my_surface)
      #print " {MoveTo, %d,%d,%d}, _ " % (int(tripoints[0][0]), int(tripoints[0][1]), int(tripoints[0][2]))
      #for c in range(3):
      #  lines.append([int(tripoints[(c)%3][0]), int(tripoints[(c+1)%3][0])])
      #  print " {DrawTo, %d,%d,%d}, _ " % (int(tripoints[(c+1)%3][0]), int(tripoints[(c+1)%3][1]), int(tripoints[(c+1)%3][2]))
    elif parts[0] == 'usemtl':
      if parts[1].strip() in ignore_materials:
        ignoring = True
      else:
        ignoring = False

# if we're calculating normals, do it here...
new_norm_list = []
new_surfaces = []
# Turn the remaining surfaces into lines
# this, of course, onyl works for correctyly wound vectors
if calculate_normals:
  for s in surfaces:
    if len(s) != 3:
      raise "Can only calculate normals for triangls right noe..."
    p1 = [points[s[0][0]][0], points[s[0][0]][1], points[s[0][0]][2]]
    p2 = [points[s[1][0]][0], points[s[1][0]][1], points[s[1][0]][2]]
    p3 = [points[s[2][0]][0], points[s[2][0]][1], points[s[2][0]][2]]
    va = [p2[0]-p1[0], p2[1]-p1[1], p2[2]-p1[2]]
    vb = [p3[0]-p1[0], p3[1]-p1[1], p3[2]-p1[2]]
    n1 = va[1]*vb[2] - va[2]*vb[1]
    n2 = va[2]*vb[0] - va[0]*vb[2]
    n3 = va[0]*vb[1] - va[1]*vb[0]
    nn = [n1, n2, n3]
    normal_id = -1
    d=0
    # Find this in the normal list :)
    for n in new_norm_list:
      if round(n[0],2) == round(nn[0],2) and round(n[1],2) == round(nn[1],2) and round(n[2],2) == round(nn[2],2):
        normal_id = d
      d+=1
    if normal_id == -1:
      normal_id = len(new_norm_list)
      new_norm_list.append(nn)
    s[0][1] = normal_id
    s[1][1] = normal_id
    s[2][1] = normal_id
    new_surfaces.append(s)
  # and copy our floppy
  normals = new_norm_list
  surfaces = new_surfaces

# Find any obvious quads via a terrible, terribly slow algorythm
# What we're looking for here, is surfaces which share a common
# line between them - i.e. not just a point, but an entire line, which
# is also oriented the same way.  We can then assume that that line is
# superflous...
if simple_quad_detect:
  qf=0
  found_quads = True
  while found_quads:
    found_quads = False
    for s1 in surfaces:
      for s2 in surfaces:
        if (not found_quads) and s1!=s2 and len(s1)==3 and len(s2)==3: # and len(set(s1[0]))==3 and len(set(s2[0]))==3:  
          for c1 in range(3):
            for c2 in range(3):
              # only do anything if the normal is the same - differeing normals = not quads :)
              if (not found_quads) and s1[c1][0] == s2[c2][0] and (s1[(c1+1)%3][0] == s2[(c2+1)%3][0] or s1[(c1+1)%3][0] == s2[(c2-1)%3][0]) and s1[0][1] == s2[0][1]:
                # Find all of our line segments
                my_lines = []
                for ql in range(3):
                  if ql!=c1:
                    my_lines.append([s1[ql][0], s1[(ql+1)%3][0], s1[ql][0]])
                for ql in range(3):
                  if (((s1[(c1+1)%3][0] == s2[(c2+1)%3]) and ql!=c2) or
                     ((s1[(c1+1)%3][0] == s2[(c2-1)%3]) and ql!=((c2-1)%3))):
                    my_lines.append([s2[ql][0], s2[(ql+1)%3][0], s2[ql][0]])
                #print s1,s2,"is a quad of ",my_lines
                surfaces.remove(s1)
                surfaces.remove(s2)
                # Just output them straight to the line list, rather than trying to
                # turn them back into a poly!
                lines+=my_lines
                found_quads = True
                qf+=1


# Turn the remaining surfaces into lines
for s in surfaces:
  for c in range(len(s)):
    # This is obviously wrong :)
    # but it's proabbly good enough for demo....
    normal_id = s[c][1]
    lines.append([s[c][0], s[(c+1)%len(s)][0], normal_id])



# first remove dupes from lines
# both dupe lines and empty draws
nl = []
lines = sorted(lines)
ll=[0,0,0]
for l in lines:
  # also cull too short lines
  lx = points[l[0]][0] - points[l[1]][0]
  ly = points[l[0]][1] - points[l[1]][1]
  lz = points[l[0]][1] - points[l[1]][1]
  llength = math.sqrt(lx*lx+ly*ly+lz*lz)
  # split into left hand side and right hand side, to ignore differnet normals
  lsc = ll
  rsc = l
  # If we're ignoring them, slice off the last part of the line
  if ignore_differing_normals:
    lsc = lsc[:-1]
    rsc = rsc[:-1]
  if llength > min_line_length and lsc != rsc:
    if [points[l[0]][0], points[l[0]][1], points[l[0]][2]] != [points[l[1]][0], points[l[1]][1], points[l[1]][2]]:
      nl.append(l)
  ll = l
lines = nl

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
        line_seg = [l[1],l[0],l[2]]
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
        if include_normals:
          print "  {MoveTo,%f,%f,%f,%f,%f,%f}," % (points[l[0]][0], points[l[0]][1], points[l[0]][2],
              normals[l[2]][0], normals[l[2]][1], normals[l[2]][2]),
        else:
          print "  {MoveTo,%f,%f,%f}," % (points[l[0]][0], points[l[0]][1], points[l[0]][2]),
    if include_normals:
      print "  {DrawTo, %f,%f,%f,%f,%f,%f}" % (points[l[1]][0], points[l[1]][1], points[l[1]][2],
                            normals[l[2]][0], normals[l[2]][1], normals[l[2]][2]),
    else:
      print "  {DrawTo, %f,%f,%f}" % (points[l[1]][0], points[l[1]][1], points[l[1]][2]),

  last_draw_command = [points[l[0]][0], points[l[0]][1], points[l[0]][2], points[l[1]][0], points[l[1]][1], points[l[1]][2]]
  lastpoint = l[1]
  lines = filter(lambda a: a != actual_l, lines)
  if len(lines)>0:
    print ", _" 
    
print "}"
print "  return mysprite"
print "endfunction"
