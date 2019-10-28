
cm = {0,0,-80}
rm = {0,0,0}
call cameraTranslate(cm)
call ScaleSprite(64, 324 / 0.097)
lc = Lines3DSprite(lightcycle())
controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
while controls[1,3] = 0
  controls = WaitForFrame(JoystickNone, Controller1, JoystickNone)
  rem cm[3] = cm[3] - 1
  rem call cameraTranslate(cm)
  call SpriteRotate(lc, 0, 0, 6)
endwhile

function lightcycle()
mysprite={ _
  {MoveTo,1.095366,2.185300,3.811200},   {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.095366,2.185300,3.811200} , _
  {DrawTo, 1.095366,0.696658,2.547060} , _
  {DrawTo, 1.098336,-3.106800,-5.447660} , _
  {DrawTo, 1.095366,0.696658,2.547060} , _
  {DrawTo, 1.095366,2.598780,-5.445520} , _
  {DrawTo, 1.098336,-3.106800,-5.447660} , _
  {DrawTo, 1.095366,-3.107120,3.293160} , _
  {DrawTo, 1.095366,0.696658,2.547060} , _
  {DrawTo, 1.095366,-3.107120,3.293160} , _
  {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.095366,2.185300,7.058660} , _
  {DrawTo, 1.095366,2.185300,3.811200} , _
  {MoveTo,1.339774,2.330880,5.123040},   {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, 1.355596,-0.202222,2.102200} , _
  {DrawTo, 1.339774,2.330880,5.123040} , _
  {DrawTo, -1.351492,2.330880,5.121420} , _
  {DrawTo, -1.351008,-0.202760,2.102720} , _
  {DrawTo, -1.351490,1.657954,-8.363520} , _
  {DrawTo, -1.351492,2.330880,5.121420} , _
  {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, 1.339774,2.330880,5.123040} , _
  {MoveTo,0.786902,1.611488,5.886720},   {DrawTo, -0.779340,2.245080,6.265640} , _
  {DrawTo, -0.779338,4.107460,-0.379262} , _
  {DrawTo, 0.785762,4.113960,-0.375442} , _
  {DrawTo, 0.786902,3.389100,-0.375776} , _
  {DrawTo, 0.786902,1.611488,5.886720} , _
  {DrawTo, 0.785762,4.113960,-0.375442} , _
  {DrawTo, 0.786902,1.611488,5.886720} , _
  {DrawTo, -0.778194,1.604948,5.882960} , _
  {DrawTo, -0.778192,3.382220,-0.379542} , _
  {DrawTo, -0.779338,4.107460,-0.379262} , _
  {DrawTo, -0.778194,1.604948,5.882960} , _
  {DrawTo, -0.779338,4.107460,-0.379262} , _
  {DrawTo, 0.785762,2.251580,6.269460} , _
  {DrawTo, -0.779338,4.107460,-0.379262} , _
  {DrawTo, -0.779340,2.245080,6.265640} , _
  {DrawTo, -0.778194,1.604948,5.882960} , _
  {DrawTo, -0.779340,2.245080,6.265640} , _
  {DrawTo, 0.786902,1.611488,5.886720} , _
  {DrawTo, 0.785762,2.251580,6.269460} , _
  {DrawTo, 0.785762,4.113960,-0.375442} , _
  {DrawTo, 0.785762,2.251580,6.269460} , _
  {DrawTo, 0.786902,1.611488,5.886720} , _
  {MoveTo,0.785762,2.251580,6.269460},   {DrawTo, -0.779340,2.245080,6.265640} , _
  {DrawTo, 0.785762,2.251580,6.269460} , _
  {MoveTo,1.095366,2.185300,7.058660},   {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.095366,0.696658,2.547060} , _
  {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.095366,-3.107120,3.293160} , _
  {DrawTo, 1.095366,-3.119180,7.065980} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, 1.095366,-3.107120,3.293160} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.095366,0.321378,7.058660} , _
  {DrawTo, 1.095366,2.185300,7.058660} , _
  {DrawTo, 1.095366,0.321378,7.058660} , _
  {DrawTo, -1.090778,2.185300,7.058660} , _
  {DrawTo, 1.095366,2.185300,7.058660} , _
  {MoveTo,0.005566,1.979804,7.072320},   {DrawTo, 0.603038,1.130370,7.072320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, -0.598450,-0.987424,9.076320} , _
  {DrawTo, -0.598450,1.130370,7.072320} , _
  {DrawTo, 0.005566,1.979804,7.072320} , _
  {DrawTo, -0.598450,-0.987424,9.076320} , _
  {DrawTo, 0.005566,1.979804,7.072320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, -0.598450,-3.125640,7.072320} , _
  {DrawTo, -0.598450,-0.987424,9.076320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, 0.005566,1.979804,7.072320} , _
  {MoveTo,0.603038,1.130370,7.072320},   {DrawTo, 0.603038,-0.987424,9.076320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, 0.005566,-1.095558,3.956680} , _
  {DrawTo, -0.598450,-1.067990,4.960880} , _
  {DrawTo, -0.598450,-3.125640,7.072320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, 0.603038,-0.987424,9.076320} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, -0.598450,-1.067990,4.960880} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, -0.598450,-3.125640,7.072320} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, 0.005566,-0.982452,10.000000} , _
  {DrawTo, 0.603038,1.130370,7.072320} , _
  {MoveTo,1.095366,0.321378,7.058660},   {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, -1.090778,0.321378,7.058660} , _
  {DrawTo, -1.090778,2.185300,7.058660} , _
  {DrawTo, 1.095366,0.321378,7.058660} , _
  {DrawTo, -1.090778,0.321378,7.058660} , _
  {DrawTo, -1.090778,2.185300,3.811200} , _
  {DrawTo, -1.090778,2.185300,7.058660} , _
  {DrawTo, -1.090778,0.321378,7.058660} , _
  {DrawTo, 1.095366,0.321378,7.058660} , _
  {MoveTo,0.406022,-0.300482,7.072320},   {DrawTo, 0.406022,-1.050812,6.414860} , _
  {DrawTo, 0.406022,-1.023954,7.702940} , _
  {DrawTo, 0.406022,-0.300482,7.072320} , _
  {MoveTo,-0.401436,-0.300482,7.072320},   {DrawTo, -0.401436,-1.023954,7.702940} , _
  {DrawTo, -0.401436,-1.694798,7.072320} , _
  {DrawTo, -0.401436,-1.077666,6.414860} , _
  {DrawTo, -0.401436,-1.023954,7.702940} , _
  {DrawTo, -0.401436,-1.077666,6.414860} , _
  {DrawTo, -0.401436,-0.300482,7.072320} , _
  {MoveTo,-1.090778,0.321378,7.058660},   {DrawTo, -1.090778,-1.018774,6.004700} , _
  {DrawTo, -1.090778,2.185300,3.811200} , _
  {DrawTo, -1.090778,0.321378,7.058660} , _
  {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, 1.095366,-3.119180,7.065980} , _
  {DrawTo, -1.090778,-3.119180,7.061140} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, -1.090778,-3.119180,7.061140} , _
  {DrawTo, -1.089342,-2.300340,7.061880} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, -1.089342,-2.300340,7.061880} , _
  {DrawTo, -1.090778,-3.119180,7.061140} , _
  {DrawTo, -1.090778,-3.107120,3.293160} , _
  {DrawTo, -1.090778,2.185300,3.811200} , _
  {DrawTo, -1.090778,-1.018774,6.004700} , _
  {DrawTo, -1.090778,0.321378,7.058660} , _
  {MoveTo,-1.090778,-1.018774,6.004700},   {DrawTo, -1.090778,-3.107120,3.293160} , _
  {DrawTo, -1.090778,0.696658,2.547060} , _
  {DrawTo, -1.090778,2.185300,3.811200} , _
  {DrawTo, -1.090778,-3.107120,3.293160} , _
  {DrawTo, -1.090778,-3.107120,-5.445520} , _
  {DrawTo, -1.090778,0.696658,2.547060} , _
  {DrawTo, -1.090778,-3.107120,-5.445520} , _
  {DrawTo, -1.085936,2.598780,-5.445520} , _
  {DrawTo, -1.090778,0.696658,2.547060} , _
  {DrawTo, -1.090778,-3.107120,3.293160} , _
  {DrawTo, -1.089342,-2.300340,7.061880} , _
  {DrawTo, -1.090778,-1.018774,6.004700} , _
  {DrawTo, 1.095366,-1.017698,6.004700} , _
  {DrawTo, -1.090778,-1.018774,6.004700} , _
  {DrawTo, 1.096802,-2.300880,7.061340} , _
  {DrawTo, -1.090778,-1.018774,6.004700} , _
  {DrawTo, -1.089342,-2.300340,7.061880} , _
  {DrawTo, -1.090778,-3.107120,3.293160} , _
  {DrawTo, -1.090778,-1.018774,6.004700} , _
  {MoveTo,0.406022,-1.050812,6.414860},   {DrawTo, 0.406022,-1.694798,7.072320} , _
  {DrawTo, 0.406022,-1.023954,7.702940} , _
  {DrawTo, 0.406022,-1.050812,6.414860} , _
  {MoveTo,0.603038,-1.094848,4.960880},   {DrawTo, 0.005566,-1.095558,3.956680} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, 0.603038,-0.987424,9.076320} , _
  {DrawTo, 0.603038,-3.125640,7.072320} , _
  {DrawTo, 0.005566,-1.095558,3.956680} , _
  {DrawTo, 0.603038,-3.125640,7.072320} , _
  {DrawTo, 0.005566,-3.975080,7.072320} , _
  {DrawTo, 0.603038,-3.125640,7.072320} , _
  {DrawTo, 0.603038,-1.094848,4.960880} , _
  {MoveTo,1.355596,-0.202222,2.102200},   {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, -1.351492,2.330880,5.121420} , _
  {DrawTo, -1.351492,3.709460,-0.521120} , _
  {DrawTo, -1.351492,2.330880,5.121420} , _
  {DrawTo, -1.351490,1.657954,-8.363520} , _
  {DrawTo, 1.339776,1.657954,-8.363520} , _
  {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, 1.339776,1.657954,-8.363520} , _
  {DrawTo, 1.355596,-0.200452,-4.141720} , _
  {DrawTo, 1.355596,-0.202222,2.102200} , _
  {MoveTo,1.339776,3.709460,-0.521120},   {DrawTo, -1.351490,1.657954,-8.363520} , _
  {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, 1.355596,-0.200452,-4.141720} , _
  {DrawTo, 1.339776,3.709460,-0.521120} , _
  {DrawTo, -1.351492,3.709460,-0.521120} , _
  {DrawTo, 1.339776,3.709460,-0.521120} , _
  {MoveTo,-1.351492,3.709460,-0.521120},   {DrawTo, -1.351490,1.657954,-8.363520} , _
  {DrawTo, -1.351492,3.709460,-0.521120} , _
  {MoveTo,-0.778192,2.495960,-5.906840},   {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, -0.778192,1.631930,-8.218920} , _
  {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, 0.786902,1.631870,-8.219020} , _
  {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, 0.785762,1.764256,-8.921880} , _
  {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, -0.778192,2.495960,-5.906840} , _
  {DrawTo, -0.778192,1.631930,-8.218920} , _
  {DrawTo, 0.786902,1.631870,-8.219020} , _
  {DrawTo, 0.785762,1.764256,-8.921880} , _
  {DrawTo, 0.786902,1.631870,-8.219020} , _
  {DrawTo, 0.786902,2.502500,-5.903080} , _
  {DrawTo, 0.785762,1.764256,-8.921880} , _
  {DrawTo, 0.786902,2.502500,-5.903080} , _
  {DrawTo, 0.785762,3.197300,-6.243320} , _
  {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, -0.779338,3.190820,-6.247140} , _
  {DrawTo, -0.779338,1.757762,-8.925700} , _
  {DrawTo, 0.785762,3.197300,-6.243320} , _
  {DrawTo, 0.785762,1.764256,-8.921880} , _
  {DrawTo, 0.785762,3.197300,-6.243320} , _
  {DrawTo, -0.779338,3.190820,-6.247140} , _
  {DrawTo, -0.778192,2.495960,-5.906840} , _
  {MoveTo,0.023106,1.979964,-6.742460},   {DrawTo, -2.149420,1.194588,-6.742460} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, -2.149420,-3.328580,-7.680980} , _
  {DrawTo, 0.023106,-4.113960,-7.680980} , _
  {DrawTo, -2.149420,-3.328580,-7.680980} , _
  {DrawTo, -2.149420,-1.707870,-4.596260} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, 0.023106,-4.113960,-7.680980} , _
  {DrawTo, 2.154020,-3.328580,-7.680980} , _
  {DrawTo, 0.023106,-4.113960,-7.680980} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, 2.154020,-3.328580,-7.680980} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, -2.149420,-1.707870,-4.596260} , _
  {DrawTo, -2.149420,1.194588,-6.742460} , _
  {DrawTo, 0.023106,1.979964,-6.742460} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, 2.154020,-1.707870,-4.596260} , _
  {DrawTo, 2.154020,-3.328580,-7.680980} , _
  {DrawTo, 2.154020,-0.287086,-9.058300} , _
  {DrawTo, 2.154020,1.194588,-6.742460} , _
  {DrawTo, 2.154020,-1.707870,-4.596260} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, 0.023106,1.979964,-6.742460} , _
  {DrawTo, 2.154020,-1.707870,-4.596260} , _
  {DrawTo, 0.023106,1.979964,-6.742460} , _
  {DrawTo, 2.154020,1.194588,-6.742460} , _
  {DrawTo, 0.023106,1.979964,-6.742460} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, 0.023106,-4.113960,-7.680980} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, 2.154020,-3.328580,-7.680980} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, 2.154020,-0.287086,-9.058300} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, 2.154020,1.194588,-6.742460} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, 0.023106,1.979964,-6.742460} , _
  {MoveTo,-2.149420,1.194588,-6.742460},   {DrawTo, -2.149420,-0.287086,-9.058300} , _
  {DrawTo, -2.149420,-3.328580,-7.680980} , _
  {DrawTo, 0.023106,-1.734422,-3.615360} , _
  {DrawTo, -2.149420,1.194588,-6.742460} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, -2.149420,-0.287086,-9.058300} , _
  {DrawTo, 0.023106,-4.113960,-7.680980} , _
  {DrawTo, -2.149420,-0.287086,-9.058300} , _
  {DrawTo, 0.023106,-0.286682,-10.000000} , _
  {DrawTo, -2.149420,1.194588,-6.742460} , _
  {MoveTo,-1.139380,-0.300320,-6.742460},   {DrawTo, -1.139380,-1.025368,-6.109100} , _
  {DrawTo, -1.139380,-1.694630,-6.742460} , _
  {DrawTo, -1.139380,-1.015030,-7.385440} , _
  {DrawTo, -1.139380,-1.025368,-6.109100} , _
  {DrawTo, -1.139380,-1.015030,-7.385440} , _
  {DrawTo, -1.139380,-0.300320,-6.742460} , _
  {MoveTo,1.143968,-0.300320,-6.742460},   {DrawTo, 1.143968,-1.015030,-7.385440} , _
  {DrawTo, 1.143968,-1.694630,-6.742460} , _
  {DrawTo, 1.143968,-1.025368,-6.109100} , _
  {DrawTo, 1.143968,-1.015030,-7.385440} , _
  {DrawTo, 1.143968,-1.025368,-6.109100} , _
  {DrawTo, 1.143968,-0.300320,-6.742460} }
  return mysprite
endfunction
