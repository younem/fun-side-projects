"""
Written By Madeline Younes
Date: 28/11/2020
Program that listens to audio and trys to guess the song that you're singing.
"""

import speech_recognition as sr
from googlesearch import search
import wave
import time
import pyaudio

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()
pa = pyaudio.PyAudio()
#pa.get_default_host_api_info()

mode = input("Do you want to read in from a wav file? [y/n]: ")

if mode == 'y':
    filename = input("Enter file name in the format 'file.wav': ")
    try:
        wf = wave.open(filename, 'rb')
    except (wave.Error, EOFError):
        raise OSError("Error reading the audio file. Only WAV files are supported.")

    with sr.AudioFile(filename) as source:
        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)

    except:
         print('Sorry.. run again...')

    # define callback (runs the callback in a seperate thread)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)

    # open stream using callback (3)
    stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)

    # start the stream (4)
    stream.start_stream()

    # wait for stream to finish (5)
    while stream.is_active():
        time.sleep(0.1)

    # stop stream (6)
    stream.stop_stream()
    stream.close()
    wf.close()

    # close PyAudio (7)
    pa.terminate()

else:
    stream_in = pa.open(
    rate=48000,
    channels=2,
    format=pyaudio.paInt16,
    input=True,                   # input stream flag
    input_device_index=1,         # input device index
    frames_per_buffer=1024
    )

    # read 5 seconds of the input stream
    input_audio = stream_in.read(5 * 48000)



"""
with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)
"""
