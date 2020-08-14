#!/usr/bin/python3
import sys
import time
import os
import subprocess
from progress.bar import Bar
import pathlib
import shutil

def main(argv):
    kiloByteSize = 10240# 5120

    def CreateDummyFile(size):
        currentDir = pathlib.Path(os.path.curdir)
        dummyFile = currentDir.joinpath(".dummy")
        if not dummyFile.exists():
            bar = Bar('Creating %s Mb dummy file' %(size/1000), max=size)
            with dummyFile.open(mode='w') as d:
                for _ in range(size):
                    d.writelines("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feu")
                    bar.next()
                print("\n") # To prevent the next string to be added with no linebreak
        return dummyFile

    try: # Verify Arguments
        driveLetter = argv[0]
        assert len(argv) == 1
        assert len(driveLetter) == 1
        drive = pathlib.Path(driveLetter + ":\\")
    except:
        print("Usage: usbtest.py <USBDriveLetter>")
        sys.exit(2)

    if not drive.exists():
        print ('Invalid input or drive not found')
        sys.exit(2)

    #Create 5Mb local file
    dummyFile = CreateDummyFile(kiloByteSize)
    source = str(dummyFile.absolute())
    target = str(drive.absolute())

    print("Testing...")
    tick = time.perf_counter()
    shutil.copy(source, target)
    elapsedTime = time.perf_counter() - tick
    speed = round(kiloByteSize/elapsedTime/1000, 2)

    #dummyFile.unlink()

    print ("Elapsedtime: %s seconds" %elapsedTime) 
    print ("Speed: %s Mb/sec" %speed)

if __name__ == "__main__":
    main(sys.argv[1:])