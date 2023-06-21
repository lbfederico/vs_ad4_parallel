from vs.defs.input_data01 import command_line
from vs.defs.paths import (
    prj_path,
    out_path,
    pdbqt_path,
    scripts_path,
    best_path,
    poses_path,
    alldata_path
)
import os
import shutil
import subprocess


args = command_line()

def pipeline(lig):
    """
    Função para rodar os scripts em sequencia do AD4
    :param lig:
    :return:
    """

    path_lig = alldata_path/ f'out_{lig.stem}'
    path_lig.mkdir(exist_ok=True, parents=True)
    shutil.copy(f'{out_path}/{args.prot.split(".")[0]}.pdbqt', path_lig)

    print(f'Start {lig.name}')
    shutil.move(pdbqt_path/lig.name , path_lig)

    os.chdir(path_lig)

    subprocess.run([
        prj_path/ './pythonsh',
        scripts_path/ 'prepare_dpf42.py',
        '-l', lig.name,
        '-r', f'{args.prot.split(".")[0]}.pdbqt'
    ])
    print(f'Create {args.prot.split(".")[0]}.dpf')


    subprocess.run([
        prj_path/ './pythonsh',
        scripts_path/ 'prepare_gpf4.py',
        '-l', lig.name,
        '-r', args.prot.split('.')[0] + '.pdbqt',
        '-i', out_path/ 'ref.gpf',
        '-p', f'npts={(args.rad)},{(args.rad)},{(args.rad)}',
        '-o', f'{lig.stem}_{args.prot.split(".")[0]}.gpf',
    ])

    print(f'.gpf {lig.stem}_{args.prot.split(".")[0]} create')

    print('Autogrid running')

    subprocess.run([
        'autogrid4',
        '-l', f'{lig.stem}.glg',
        '-p', f'{lig.stem}_{args.prot.split(".")[0]}.gpf'
    ])
    print(f'autogrid {lig.stem}_{args.prot.split(".")[0]} finished')

    print('AD4 running')
    subprocess.run([
        'autodock4',
        '-p', f'{lig.stem}_{args.prot.split(".")[0]}.dpf',
        '-l', f'{lig.stem}.dlg'
    ])


    subprocess.run([
        prj_path/ './pythonsh',
        scripts_path/ 'summarize_results4.py',
        '-d', path_lig
    ])

    print(f'sumamary moved to {out_path}')

    subprocess.run([
        prj_path/ './pythonsh',
        scripts_path/ 'write_lowest_energy_ligand.py',
        '-f',f'{lig.stem}.dlg',
        '-N',
        '-o', f'best_{lig.name}'
    ])
    print(f' best_{lig.name} create')

    subprocess.run([
        prj_path/ './pythonsh',
        scripts_path/ 'write_conformations_from_dlg.py',
        '-d', f'{lig.stem}.dlg',
        '-o', f'pose_{lig.stem}'
    ])

    print(f'Create pose_{lig.stem}')
    print(f'Finished run {lig.stem}')

    best_poses = list(path_lig.glob('*best*'))
    [shutil.move(best, best_path) for best in best_poses]

    pose_files = list(path_lig.glob('*pose*'))
    [shutil.move(pose, poses_path ) for pose in pose_files]


