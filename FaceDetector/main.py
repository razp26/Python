import json
import detector
from Models.conf import ConfigurationFile

def main():
    conf = ConfigurationFile.get()
    detector.start(conf.frontalFace)

if __name__ == "__main__":
    main()
