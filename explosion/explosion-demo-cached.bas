include "cycle.bai"
include "explosion.bai"

' demo the explosion stuiff
call ScaleSprite(32)
call ReturnToOriginSprite()

' get the object
cm ={0,0,-40}
rm = {0,0,0}
call cameraTranslate(cm)
call ScaleSprite(64, 324 / 0.097)
cycle_object = lightcycle()

' prepare the object for exploding - just expanding variables here for clarity :)
world_scale = 1.0
x_impulse = 2.5
y_impulse = 3.0
z_impulse = 2.5
x_random = 2.5
y_random = 3.0
z_random = 2.5
ce = prepare_explosion(3, cycle_object, world_scale, {0,0, 0}, {x_impulse, y_impulse, z_impulse}, {x_random, y_random, z_random}, 9.8, -2.5, false)

' grab 2 seconds worth of explosion - 40frams @ 20 fps
' Note that generating more than about 10k verticies _will_ break things - for this demo, our object is
' 220 broken vertificies - this means it tkaes 220*30*4 array entries for this, or 26400 array entries for
' this precalc - so on large objects, essentially be careful!  Especially since you need to multiply that also
' out due to them being 4byte floats/ints - so after 52 frames, the v32 runs out of ram in the generation phase.
' I suspect that's also some not-so-great GC, since we use a bunch of deepcopy stuff in there, BUT... still, 
' that's 183kbytes of data at that point, which DOES match with my expectations about what the v32 can handle!
'
' So the short version is, be careful about your frame rates ;)
call fill_cache(ce, 40, 20)


' put it on the screen
lc=Lines3dSprite(ce.dest)
call SpriteClip(lc, {{-500, 500}, {500, -500}})
controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
exploding = false
while controls[1,3] = 0
  if exploding
    ' get new cached data!
    new_data = cached_explosion(ce)
    call SpriteSetData(lc, new_data)
  elseif controls[1,4] = 1
    exploding = true
  endif
  ' wait for next frame :)
  controls =  WaitForFrame(JoystickNone, Controller1, JoystickNone)
  call SpriteRotate(lc, 0, 0, 3)
endwhile

