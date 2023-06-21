from pathlib import Path
import shutil
from traquitanas.files import utils



prj_path = Path(__file__).parents[2]

vs_path = prj_path/ 'vs'

# Data
out_path = vs_path / 'autodock_out'
out_path.mkdir(exist_ok=True, parents=True)

defs_path = vs_path / 'defs'
scripts_path = vs_path / 'scripts_autodock'
input_path = vs_path / 'input'


shutil.rmtree(
    out_path,
    ignore_errors=False,
    onerror=utils.handle_remove_readonly
)

out_path.mkdir(exist_ok=True, parents=True)

ad4_path = out_path / 'ad4_out'
ad4_path.mkdir(exist_ok=True, parents=True)

poses_path = out_path / 'pose_results'
poses_path.mkdir(exist_ok=True, parents=True)

best_path = out_path/ 'best_results'
best_path.mkdir(exist_ok=True, parents=True)

pdbqt_path = out_path/ 'pdbqt'
pdbqt_path.mkdir(exist_ok=True, parents=True)

alldata_path = out_path/ 'all_data'
alldata_path.mkdir(exist_ok=True, parents=True)

dlg_path = out_path/ 'dlg'
dlg_path.mkdir(exist_ok=True, parents=True)


