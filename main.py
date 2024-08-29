import os
from glob import glob
from pydub import AudioSegment

files = [f for f in glob("*") if os.path.isfile(f) and not f.endswith((".wav", ".py"))]

try:
    for file in files:
        print(f"Converting file: {file}")
        sound = AudioSegment.from_file(file)
        sound.set_channels(1)
        sound.set_frame_rate(1600)
        converted_audio = sound.export(f"{file}.wav", format="wav", codec="pcm_s16le")

except Exception as e:
    print(e)
