#!/usr/bin/env bash
export SQUAD_DIR=~/data/squad
python ./evaluate-v1.1.py $SQUAD_DIR/dev-v1.1.json ./bert_base_srl/predictions.json