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
            bar = Bar('Creating Dummy File', max=size)
            with dummyFile.open(mode='w') as d:
                for _ in range(size):
                    d.writelines("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feu")
                    bar.next()
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

    tick = time.perf_counter()
    print("Copying file...")
    shutil.copy(source, target)
    elapsedTime = time.perf_counter() - tick
    speed = kiloByteSize/elapsedTime

    dummyFile.unlink()

    print("Filesize: " + str(kiloByteSize) + " Kb")
    print("Elapsedtime: " + str(elapsedTime) + " seconds") 

    print ("Your disk drive speed is %s Kb/sec" %speed)

if __name__ == "__main__":
    main(sys.argv[1:])