#!/bin/sh

N=1
OUTPUT_DIR="/tmp/model"
TRAIN_FILE="../data/train.txt"
VALID_FILE="../data/valid.txt"

CUDA_VISIBLE_DEVICES=$N

python ../src/run_clm.py \
    --output_dir=$OUTPUT_DIR \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --train_file $TRAIN_FILE \
    --do_eval \
    --validation_file $VALID_FILE \
    --evaluation_strategy epoch \
    --per_device_train_batch_size=2 \
    --per_device_eval_batch_size=2 \
    --learning_rate 5e-5 \
    --num_train_epochs=5
