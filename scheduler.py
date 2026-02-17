import os
import shutil
import config
import compression
import encryption
from temperature import calculate_temperature

storage = {}

def schedule():

    for file in os.listdir(config.DEVICE):

        temp = storage.get(file, 700)

        if temp < config.WARM_THRESHOLD:

            shutil.move(config.DEVICE+file, config.CLOUD+file)

            compression.compress_file(file)

            encryption.encrypt_file(file)

            print(file, "moved to CLOUD")

        elif temp < config.HOT_THRESHOLD:

            shutil.move(config.DEVICE+file, config.EDGE+file)

            print(file, "moved to EDGE")

        else:

            print(file, "remains in DEVICE")
