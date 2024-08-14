import pyttsx3
import objc




# Assuming you've installed py3-tts: pip install py3-tts
engine = pyttsx3.init()  # No need to specify `driverName`

engine.say("Hello, world!")
engine.runAndWait()
