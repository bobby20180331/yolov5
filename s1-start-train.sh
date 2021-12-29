## train on laptop 3060
python train.py --data pet2k.yaml  --weights yolov5s.pt --img 640

## train on V100s*4 server
# conda activate py397
# python -m torch.distributed.launch --nproc_per_node 4 train.py --batch 128 --data pet2k.yaml --weights yolov5s.pt --img 640  --device 0,1,2,3
