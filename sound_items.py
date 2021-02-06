
import os
import shutil
from pydub import AudioSegment
from pydub.silence import split_on_silence


class SoundItems():
    def __init__(self, filepath, min_silence_len=900, silence_thresh=-60) -> None:
        audio = AudioSegment.from_mp3(filepath)
        self.audio_items = split_on_silence(
            audio,
            min_silence_len=min_silence_len,
            silence_thresh=silence_thresh
        )
        print(self.audio_items)

    def export(self, savedir_path):
        if os.path.exists(savedir_path):
            shutil.rmtree(savedir_path)
        os.makedirs(savedir_path)

        for idx, audio in enumerate(self.audio_items):
            print(f"{savedir_path}/{idx}.mp3 save.")
            audio.export(f"{savedir_path}/{idx}.mp3")

if __name__ == '__main__':
    sound_items = SoundItems('/Users/k17113kk/Downloads/1400_1_1-100/TG1400_1_Sec01_0001_0016.mp3')
    sound_items.export('sample')
