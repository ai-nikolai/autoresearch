# How to get started with openEvolve and autoresearch

## Getting started:

1. installation
```bash
pip3 install openevolve
```

2. Running it.
```bash
export OPENAI_API_KEY="sk-dummy"
python openevolve-run.py model.py \
  evaluate.py \
  --config config.yaml \
  --iterations 10
```