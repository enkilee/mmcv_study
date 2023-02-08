#!/bin/bash
module load anaconda/2021.05
module load cuda/11.6
module load gcc/9.3

source activate mmDect
export PYTHONUNBUFFERED=1

python configs/ballon/color_splash.py --out color_splash_gray.mp4 data/test_video.mp4 configs/ballon/mask_rcnn_balloon.py work/mask_rcnn_balloon/latest.pth

