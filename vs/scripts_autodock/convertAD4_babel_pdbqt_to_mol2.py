import os
import subprocess
from pathlib import Path


# Function
def get_line(fl, txt):
    with open(fl, encoding='utf8') as file:
        for line_num, value in enumerate(file, 1):
            if txt in value:
                return value

#Diretórios
prj_path = Path(__file__).parent
data_path = prj_path/ 'data'
in_path = data_path/ 'input'
out_path = data_path/ 'output'
data_path.mkdir(exist_ok=True)
in_path.mkdir(exist_ok=True)
out_path.mkdir(exist_ok=True)

#List
best_ligs = in_path.rglob('*.pdbqt')
best_ligs = list(best_ligs)
print(best_ligs)




# Loop
for result_ad4 in best_ligs:
    print(result_ad4)
    try:
        line_energy = get_line(result_ad4, 'REMARK binding_energy')
        print(line_energy)
        energy = str(' '.join(line_energy.split())).split(' ')[2]
        print(energy)
        file_out = out_path/ f'{result_ad4.stem}.mol2'
        print(file_out)

        
        if True:
            os.chdir(in_path)
            print(f'{result_ad4.stem}.pdbqt')
            subprocess.run([
                'obabel',
                '-ipdbqt',
                f'{result_ad4.stem}.pdbqt',
                '-omol2',
                '-O',
                file_out
                ])
           

        with open(file_out, 'a+') as file2:
            file2.write(f'@<TRIPOS>COMMENT\n> <AD4_BindingEnergy>\n{energy}\n')

    except Exception as e:
        print(e)

