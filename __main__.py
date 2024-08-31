import os
from glob import glob
from pydub import AudioSegment
import numpy as np

def convert_to_wav(files):
    try:
        for file in files:
            print(f"Converting file: {file} to compatible wav")
            sound = AudioSegment.from_file(file)
            sound.set_channels(1)
            sound.set_frame_rate(1600)
            converted_audio = sound.export(f"{file}.wav", format="wav", codec="pcm_s16le")

    except Exception as e:
        print(e)

def convert_to_npy(files):
    try:
        for file in files:
            print(f"Converting file: {file} to compatible wav")
            sound = AudioSegment.from_file(file)
            sound.set_channels(1)
            sound.set_frame_rate(1600)
            numpy_array = np.array(sound.get_array_of_samples()).T.astype(np.float32)

            with open(f"{file}.npy", "wb") as file:
                np.save(file, numpy_array, allow_pickle=False)

    except Exception as e:
        print(e)


files = [f for f in glob("*") if os.path.isfile(f) and not f.endswith((".npy", ".md", ".txt", ".py"))]

convert_to_npy(files)