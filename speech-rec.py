import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)

try:
    sel.txt.SetValue(r.recognize_google(audio))

except sr.UnknownValueError:
    print("Google Speech Recognintion could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognotion service; {0}".format(e))
