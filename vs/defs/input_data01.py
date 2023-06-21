import argparse
import textwrap
import configargparse

def command_line():
    parser = configargparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
        Sintaxe: python3 autodock.py -param <nome do arquivo>
        Estudos de VS para o Autodock4 - retorna poses (.pdbqt) e scores .dlg
        *** Colocar receptor e ligantes na pasta input - ver a extensão e corrigir linhas 46, 47 e 52
        *** Não excluir o diretório autodock_out apenas o que estiver dentro 
        ''')
    )
    parser.add_argument('-param', '--param', required=True, is_config_file=True, help='config file path')
    parser.add_argument('-i', '--inp', help='File for Decoys Generate', required=True)
    parser.add_argument('-p', '--prot', help='Protein Receptor', required=True)
    parser.add_argument('-cx', '--center_x', help='X center', type=float, required=True)
    parser.add_argument('-cy', '--center_y', help='Y center', type=float, required=True)
    parser.add_argument('-cz', '--center_z', help='Z center', type=float, required=True)
    parser.add_argument('-r', '--rad', help='radius sphere and cub edge (2*r)', type=int, required=True)
    args = parser.parse_args()

    return args
