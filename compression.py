import os
import gzip
import shutil
import config


def compress_file(filename):

    source = config.CLOUD + filename
    destination = config.COMPRESSED + filename + ".gz"

    # Check if file exists
    if not os.path.exists(source):

        print("Compression skipped. File not found:", filename)
        return


    # Compress file
    with open(source, "rb") as f_in:

        with gzip.open(destination, "wb") as f_out:

            shutil.copyfileobj(f_in, f_out)


    print("Compressed successfully:", filename)
