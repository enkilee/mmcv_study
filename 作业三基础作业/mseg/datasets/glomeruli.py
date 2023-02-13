# Copyright (c) OpenMMLab. All rights reserved.
from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset

@DATASETS.register_module()
class GlomeruliDataset(BaseSegDataset):
    CLASSES = ('background', 'glomeruili')
    PALETTE = [[128, 128, 128], [151, 189, 8]]
    METAINFO = dict(classes = CLASSES, palette = PALETTE)
    def __init__(self, **kwargs):
        super(GlomeruliDataset,self).__init__(img_suffix='.png', seg_map_suffix='.png', **kwargs)
