function doOpen() {
    ModuleWorld_PWM.Servo(ModuleWorld_PWM.mwServoNum.P1, 270)
    ModuleWorld_PWM.Servo(ModuleWorld_PWM.mwServoNum.P2, 90)
}

function doClosed() {
    ModuleWorld_PWM.Servo(ModuleWorld_PWM.mwServoNum.P1, 180)
    ModuleWorld_PWM.Servo(ModuleWorld_PWM.mwServoNum.P2, 183)
}

doClosed()
basic.pause(3000)
basic.forever(function on_forever() {
    if (ModuleWorld_Digital.PIR(ModuleWorld_Digital.mwDigitalNum.P0P1, ModuleWorld_Digital.enPIR.OPIR)) {
        doOpen()
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.White)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        basic.pause(3000)
        doClosed()
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
        music.play(music.tonePlayable(262, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
    }
    
})
