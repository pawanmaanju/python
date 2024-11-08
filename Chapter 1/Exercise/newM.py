# Not Work This code 
import pyttsx4

# Initialize the speech engine
engine = pyttsx4.init()

# Set the rate (optional, to check if the engine works properly)
engine.setProperty('rate', 150)  # You can adjust the rate of speech

# Set the volume (optional)
engine.setProperty('volume', 1)  # Maximum volume (0.0 to 1.0)

# Set voice (optional, to ensure voice is recognized)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use the first voice (usually male)

# Speak the text
engine.say('This is an English text-to-voice test.')

# Run the speech engine
engine.runAndWait()






