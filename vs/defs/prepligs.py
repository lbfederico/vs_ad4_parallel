import shutil
import subprocess
from openbabel import pybel
from vs.defs.paths import (
    input_path,
    pdbqt_path,
    scripts_path,
    prj_path,
    out_path
)
from vs.defs.pipeline import args



def convert_pdb_pybel(file_path, output_path):


    molfile = (pybel.readfile(file_path.suffix[1:], str(file_path)))


    for i, mol in enumerate(molfile):
        output_file = f'{output_path}/mol_{i + 1}.pdb'
        mol.write('pdb', output_file)

def prepligs_ad4():

    print('Ligand Split')
    input_filepath = input_path / f'{args.inp}'
    convert_pdb_pybel(input_filepath, pdbqt_path)

    print('Create .pdbqt')
    lig_list = list(pdbqt_path.glob('*.*'))

    for i, lig in enumerate(lig_list):
        subprocess.run([
            './pythonsh',
            scripts_path / 'prepare_ligand4.py',
            '-l', lig])
        print(f'{i + 1} ligands .pdbqt were created')
        lig.unlink()
        pdbqt = list(prj_path.glob('*.pdbqt'))
        shutil.move(pdbqt[0], pdbqt_path)

def prepprot_ad4():

    print('Start protein prepare')
    subprocess.run([
        './pythonsh',
        f'{scripts_path}/prepare_receptor4.py',
        '-r', f'{input_path}/{args.prot}',
        '-o', f'{args.prot.split(".")[0]}.pdbqt'
    ])
    shutil.move(args.prot.split('.')[0] + '.pdbqt', out_path)

    with open((f'{out_path}/ref.gpf'), 'w') as file:
        file.writelines(f'gridcenter {args.center_x}'
                        f' {args.center_y} '
                        f'{args.center_z}'
                        )
    print('Create ref.gpf')
