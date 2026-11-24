"""Run the standalone certificate checker; no discovery engine is included."""
from pathlib import Path
import runpy,sys
v=Path(__file__).resolve().parent/"verify"
sys.path.insert(0,str(v))
runpy.run_path(str(v/"verify_standalone.py"),run_name="__main__")
