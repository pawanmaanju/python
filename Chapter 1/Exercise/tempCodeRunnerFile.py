import pyttsx3  # Import the text-to-speech library

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Use the engine to say a phrase
engine.say("Hello, world!")

# Run the speech engine to process the voice output
engine.runAndWait()