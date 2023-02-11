#!/bin/sh

#SBATCH --partition=public-gpu
#SBATCH --gpus=2
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=1-00:00:00

module load GCCcore/8.2.0 Singularity/3.4.0-Go-1.12

OPENPOSE_SIMG=keras-gpu.simg

CMD="python resnet50_lstm_hi_dim_train.py"

srun singularity exec --nv $OPENPOSE_SIMG $CMD
