from slither import Slither
from Detectors.SCRContractAnalysis import ContractAnalysis
from Detectors.SCRFunctionAnalysis import FunctionAnalysis
from LuvAgent import LuvAgent
from UkeAgent import UkeAgent
from utils.largetest import LargeSCP
import re,os
from pathlib import Path
import subprocess
from utils.SolidityVersionAnalyzer import SolidityVersionAnalyzer
import hashlib
from difflib import SequenceMatcher
from collections import Counter,defaultdict
from SCRKB import SCRKnowledgeBase
from absl import app
from absl import flags
import copy
import sys
from math import sqrt

FLAGS = flags.FLAGS
flags.DEFINE_string("filepath", None,"smart contract code ")
flags.DEFINE_string("INPUT_Mode",None,"file or dir or dataset")
flags.DEFINE_string("RUN_Mode",None,"run or debug")

def analyze_defi_project(filepath,INPUT_Mode,RUN_Mode,config_save_path):
    # Stay tuned for more updates

    return True

def main(argv):

    platform = sys.platform

    filepath = FLAGS.filepath
    INPUT_Mode = FLAGS.INPUT_Mode
    RUN_Mode = FLAGS.RUN_Mode

    os_type = None

    config_save_path = "./config_save/"


    if platform.startswith("win"):
        print("System Type: Windows")
        os_type = "win"
    elif platform.startswith("darwin"):
        print("System Type: macOS")
        os_type = "mac"
    elif platform.startswith("linux"):
        print("System Type: Linux")
    else:
        print("System Type: [Unkowned]", platform)
        exit()

    analyze_defi_project(filepath,INPUT_Mode,RUN_Mode,config_save_path)


if __name__ == "__main__":
    app.run(main)