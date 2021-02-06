
import os
import shutil
import fire

from sound_items import SoundItems


def main(resource_path):
    all_file_path_list = []
    for path in os.listdir(resource_path):
        for filename in os.listdir(f'{resource_path}/{path}'):
            sound_item = SoundItems(f'{resource_path}/{path}/{filename}')
            sound_item.export(f'result/{path}/{filename}')
    return all_file_path_list


if __name__ == '__main__':
    fire.Fire(main)