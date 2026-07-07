# Autoresearch adapted

The original autoresearch can be found in the `classic` subfolder. The new "AlphaEvolve" style approach is found in `evolution` (based on OpenEvolve).

## To run mini-code-cli (for the classic research):
```bash
# build python only image
# apptainer build mini_code.sif apptainer_python.def


# Python only (no gpu, no torch)
# apptainer shell --containall --bind /hx2-weka/home/nr1713/autoresearch/classic:/workspace mini_code.sif

# Build the torch image
# apptainer build mini_code_torch.sif apptainer_torch.def

# GPU container
# APPTAINERENV_CUDA_VISIBLE_DEVICES=2 apptainer shell --containall --bind /hx2-weka/home/nr1713/autoresearch/classic:/workspace --nv mini_code_torch.sif

# Build the final image from a local torch image
apptainer build mini_code_torch_full.sif apptainer_torch_full.def

# GPU container
APPTAINERENV_CUDA_VISIBLE_DEVICES=2 apptainer shell --containall --bind /hx2-weka/home/nr1713/autoresearch/classic:/workspace --nv mini_code_torch_full.sif

# Inside apptainer:
cd /workspace
mini-code --auto-mode --agent-md program.md --enable-shell
# Prompt: Let's start the experiments with train.py
```

(C) Nikolai Rozanov - 2026 - Present