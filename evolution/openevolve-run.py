"""
Entry point script for OpenEvolve
"""
import sys
import asyncio
import multiprocessing as mp
from openevolve.cli import main_async

def new_main():
    mp.set_start_method("spawn", force=True)
    return asyncio.run(main_async())

if __name__ == "__main__":
    sys.exit(new_main())
