#!/bin/bash
module load anaconda/2021.05
module load cuda/11.6
module load gcc/9.3

source activate mmDect
export PYTHONUNBUFFERED=1

python tools/train.py \
       configs/ballon/mask_rcnn_balloon.py \
       --work-dir work/mask_rcnn_balloon
