# How to get started with openEvolve and autoresearch

## Getting started:

1. installation
```bash
pip3 install openevolve
```

2. Running it.
```bash
export OPENAI_API_KEY="sk-dummy"
CUDA_VISIBLE_DEVICES=2 python openevolve-run.py model.py \
  evaluate.py \
  --config config.yaml \
  --iterations 10 \
  --output experiment_1 | tee > out.txt
```

3. Visualising results:
```bash
# python3 scripts/visualizer.py --path ../autoresearch/evolution/experiment_100836
python3 ./openevolve/scripts/visualizer.py --path ./autoresearch/evolution/experiment_100855/checkpoints --static-output ./analysis_web
```

4. testing:
```bash
python3 prepare.py
CUDA_VISIBLE_DEVICES=2 python3 evaluate.py 
```

## Other useful commands:
```bash
source ~/miniconda3/etc/profile.d/conda.sh
conda activate env_kb
# or
conda activate env_robust_kernelbench
```

### Slurm:
1. Running the job:
```bash
 sbatch ./evolution/run_slurm.sh
```

2. Interactive session
```bash
salloc --partition=interactive-gpu --gres=gpu:h200:3 --time=08:00:00 --ntasks=3
srun --pty --overlap --jobid=100831 bash
tmux attach -t 0
```

### LLM Serving

1. Serving LLM
```bash
python3 -m sglang.launch_server \
--model-path Qwen/Qwen3-Coder-Next \
--tensor-parallel-size 2 \
--tool-call-parser qwen3_coder \
--host 0.0.0.0 \
--port 30000
```

2. Testing it's running:
```bash
curl -v http://0.0.0.0:30000/health
# OR
python -c "import urllib.request; req = urllib.request.Request('http://0.0.0.0:30000/health'); resp = urllib.request.urlopen(req); print(f'HTTP/1.1 {resp.status} {resp.reason}'); [print(f'{k}: {v}') for k, v in resp.headers.items()]; print(); print(resp.read().decode())"
```

3. Capturing tmux output:
```bash
tmux capture-pane -t 0:0.0 -S - && tmux save-buffer ~/output.txt
```

## OpenEvolve config
NOTE: OpenEvolve maximises the evaluation...
```bash
# Optimal configuration discovered
max_iterations: 200  # More is better
diff_based_evolution: true  # For capable models
temperature: 0.4  # For Gemini, 0.6 for others
max_tokens: 16000  # Sweet spot
num_top_programs: 3
num_islands: 4
migration_interval: 20
migration_rate: 0.1
include_artifacts: true  # Critical for performance
```


<!-- 
```bash

# 1. Install uv project manager (if you don't already have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Download data and train tokenizer (one-time, ~2 min)
uv run prepare.py

# 4. Manually run a single training experiment (~5 min)
uv run train.py
``` 
-->