#!/bin/sh

N=1
OUTPUT_DIR="../model/"
TEST_FILE="../data/test.txt"

CUDA_VISIBLE_DEVICES=$N

python ../src/run_clm.py \
    --output_dir=$OUTPUT_DIR \
    --model_type=gpt2 \
    --model_name_or_path=$OUTPUT_DIR \
    --do_eval \
    --validation_file $TEST_FILE \
    --per_device_eval_batch_size=2 \
