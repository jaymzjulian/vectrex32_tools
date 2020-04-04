include "cycle.bai"
include "explosion.bai"

' demo the explosion stuiff
call ScaleSprite(32)
call ReturnToOriginSprite()

' get the object
cm = {0,0,-40}
rm = {0,0,0}
call cameraTranslate(cm)
call ScaleSprite(64, 324 / 0.097)
cycle_object = lightcycle()

' prepare the object for exploding - just expanding variables here for clarity :)
world_scale = 1.0
x_impulse = 2.5
y_impulse = 2.5
z_impulse = 2.5
x_random = 2.5
y_random = 2.5
z_random = 2.5
ce = prepare_explosion(3, cycle_object, world_scale, {0,0, 0}, {x_impulse, y_impulse, z_impulse}, {x_random, y_random, z_random}, 9.8, -10, false)


' put it on the screen
'f=LinesSprite(rose_explosion.dest)
'call SpriteClip(f, {{-500, 500}, {500, -500}})
lc = Lines3dSprite(ce.dest)
controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
while controls[1,3] = 0
  call explode3d(ce)
  ' wait for next frame :)
  controls =  WaitForFrame(JoystickNone, Controller1, JoystickNone)
  call SpriteRotate(lc, 0, 0, 6)
endwhile

