from lisbonpose.lisbonpose import Lisbon
import cv2
from pathlib2 import Path

def run_OP(vidpath, pointspath):
    pointpath.mkdir(exist_ok=True)
    model_folder = '--model_folder ~/deep_learning/openpose/models/'
    p = Popen('~/deep_learning/openpose/build/examples/openpose/openpose.bin '+model_folder+' --video '+str(vidpath)+' --write_json '+str(pointspath)+' --number_people_max 1', 
            shell=True)
    p.wait()
    p.communicate()


datapath = Path('Data/clean/Y/')
peoplepaths = [(e) for e in datapath.iterdir()]
conditions = ['LAC', 'LAP', 'LSC', 'LSP']

for p in peoplepaths:
    for c in conditions:
        walkpaths = p / c
        walks = [e for e  in walkpaths.iterdir()]
        for w in walks:
            vids = [e for e  in w.iterdir()]
            for v in vids: 
                if v.suffix == '.mp4':
                    vidpath = v
                    vidname = v.stem
                    pointspath = v.parent / 'Points'
                    run_OP(vidpath, pointspath)


