include "cycle.bai"
include "explosion.bai"

' demo the explosion stuiff
call ScaleSprite(32)
call ReturnToOriginSprite()

' get the object
cm =u{0,0,-40}
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
ce = prepare_explosion(3, cycle_object, world_scale, {0,0, 0}, {x_impulse, y_impulse, z_impulse}, {x_random, y_random, z_random}, 9.8, -2.5, true)


' put it on the screen
lc=LinesSprite(cycle_object)
'call SpriteClip(f, {{-500, 500}, {500, -500}})
controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
exploding = false
while controls[1,3] = 0
  if exploding
    call explode3d(ce)
  elseif controls[1,4] = 1
    exploding = true
  endif
  ' wait for next frame :)
  controls =  WaitForFrame(JoystickNone, Controller1, JoystickNone)
  call SpriteRotate(lc, 0, 0, 3)
endwhile

