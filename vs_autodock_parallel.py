from vs.defs.paths import (prj_path,
                           alldata_path,
                           out_path,
                           dlg_path,
                           scripts_path,
                           input_path,
                           pdbqt_path,
                           )
from vs.defs.prepligs import prepligs_ad4, prepprot_ad4
from vs.defs.pipeline import pipeline, args
import shutil
import multiprocessing as mp


prepligs_ad4()
prepprot_ad4()

ligs_autodock = list(pdbqt_path.glob('*.pdbqt'))
prot_pdbqt = out_path/ f'{args.prot.split(".")[0]}.pdbqt'

pool = mp.Pool(mp.cpu_count())
results = pool.map((pipeline),[lig for lig in ligs_autodock])
pool.close()

dlg_list = alldata_path.rglob('*.dlg')
[shutil.move(dlg, dlg_path) for dlg in dlg_list]