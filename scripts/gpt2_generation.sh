#!/bin/sh

$RAND_LEN = $1
$PROMPT = $2
$RAND_K = $3
$RAND_GEN = $4

python run_generation.py \
    --model_type gpt2 \
    --model_name_or_path ../model \
    --length $RAND_LEN \
    --prompt $PROMPT \
    --prefix "<BOS>" \
    --stop_token "<EOS>" \
    --k $RAND_K \
    --num_return_sequences $RAND_GEN
