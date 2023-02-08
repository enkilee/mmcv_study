_base_ = '../mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_1x_coco.py'
model = dict(
    type='MaskRCNN',
    backbone=dict(
        type='ResNet',
        depth=50,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=False),
        norm_eval=True,
        style='caffe',
        init_cfg=dict(
            type='Pretrained',
            checkpoint='configs/ballon/checkpoints/resnet50_msra-5891d200.pth')),
    roi_head=dict(
        bbox_head=dict(num_classes=1),
        mask_head=dict(num_classes=1)))
 
dataset_type = 'COCODataset' 
classes = ('balloon',) 
data = dict(
    train=dict(
        img_prefix='data/balloon/train/',
        classes=classes,
        ann_file='data/balloon/train/annotation_coco.json'), 
    val=dict(
        img_prefix='data/balloon/val/',  
        classes=classes,
        ann_file='data/balloon/val/annotation_coco.json'),
    test=dict(
        img_prefix='data/balloon/val/',  
        classes=classes,
        ann_file='data/balloon/val/annotation_coco.json')) 
 
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)

load_from = '/HOME/scz4239/run/mmdetection/configs/ballon/checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
