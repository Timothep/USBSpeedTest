#!/usr/bin/python3
import sys
import time
import os
import subprocess
from progress.bar import Bar
import pathlib
import shutil

def main(argv):
    SFileSize = 1024
    LFileSize = 10240
    XLFileSize = 51200
    drive = None

    def CreateDummyFile(sizes):
        currentDir = pathlib.Path(os.path.curdir)
        fileArray = []
        for s in sizes:
            dummyFile = currentDir.joinpath(".dummy%s" %s)
            if not dummyFile.exists():
                bar = Bar('Creating %s Mb dummy file' %(s/1000), max=s)
                with dummyFile.open(mode='w') as d:
                    for _ in range(s):
                        d.writelines("Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feu")
                        bar.next()
                    print("\n") # To prevent the next string to be added with no linebreak
            fileArray.append(dummyFile)
        return fileArray

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

    def TestUSBSpeed(filesToCopy, destination):
        for f in filesToCopy:
            source = str(f.absolute())
            target = str(destination.absolute())

            print("Testing...")
            tick = time.perf_counter()
            shutil.copy(source, target)
            elapsedTime = time.perf_counter() - tick
            speed = round(LFileSize/elapsedTime/1000, 2)
            print ("Speed: %s Mb/sec" %speed)

    fileArray = CreateDummyFile([SFileSize,LFileSize,XLFileSize])
    TestUSBSpeed(fileArray, drive)

if __name__ == "__main__":
    main(sys.argv[1:])