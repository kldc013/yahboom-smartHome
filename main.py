def doOpen():
    ModuleWorld_PWM.servo(ModuleWorld_PWM.mwServoNum.P1, 270)
    ModuleWorld_PWM.servo(ModuleWorld_PWM.mwServoNum.P2, 90)
def doClosed():
    ModuleWorld_PWM.servo(ModuleWorld_PWM.mwServoNum.P1, 180)
    ModuleWorld_PWM.servo(ModuleWorld_PWM.mwServoNum.P2, 183)
doClosed()
basic.pause(3000)

def on_forever():
    if ModuleWorld_Digital.PIR(ModuleWorld_Digital.mwDigitalNum.P0P1,
        ModuleWorld_Digital.enPIR.OPIR):
        doOpen()
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.WHITE)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(3000)
        doClosed()
        ModuleWorld_PWM.RGB2(ModuleWorld_PWM.enColor.OFF)
        music.play(music.tone_playable(262, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
basic.forever(on_forever)
