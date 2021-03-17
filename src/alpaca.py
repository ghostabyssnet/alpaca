# alpaca dev
# joao.cardoso
# 16/03/21
# changelog
# 0.1 - init
# 0.1.2 - funciona de verdade

# TODO: quando o arquivo v2 e maior que o v1, o alpaca nao pega os arquivos que nao tao presentes no v1.
# seria uma boa colocar os arquivos do v2 la tambem, deixar uma solucao completa ou sei la.

import os
import sys
import filecmp
from xml.dom import minidom

# const

A_DEBUG = True
RESULT_DIRECTORY_NAME = 'result'
RESULT_DIRECTORY = os.getcwd() + '\\' + RESULT_DIRECTORY_NAME # nao altere

# endconst

def print_debug(msg):
    if A_DEBUG == True:
        print(msg)

def check_dir(dir1, dir2):
    if (dir1 == None or dir2 == None):
        print('Erro nas pastas.')
        return False
    return True

def init_dir():
    result_dir = os.getcwd() + '\\' + RESULT_DIRECTORY_NAME 
    if (not os.path.isdir(result_dir)):
        os.mkdir(result_dir) # cria o diretorio se ele nao existir ainda
    print_debug('Diretorio de resultado ' + result_dir + ' pronto para uso.')
    RESULT_DIRECTORY = result_dir
    print(RESULT_DIRECTORY)

# getmaxsize pega o tamanho do maior diretorio entre os dois
def dir_getmaxsize(dir1, dir2):
    files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
    files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]
    if (len(files1) == 0 or len(files2) == 0):
        print('Um dos diretorios esta vazio.')
        exit(-1)
    if (len(files1) == len(files2)):
        return len(files1)
    elif (len(files1) > len(files2)):
        return len(files1)
    else:
        return len(files2)
    
def dir_search(dir):
    pass # TODO: isso aqui

def dir_file_check(addr1, addr2):
    if (os.path.exists(addr1) and os.path.exists(addr2)):
        print_debug('Caminho confirmado para ' + addr1)
        return True
    else:
        print_debug('Um arquivo nao existe em um dos dois diretorios. TODO: melhorar isso')
        return False

def dir_file_is_valid(d_file):
    filename, file_extension = os.path.splitext(d_file)
    if (file_extension != '.xml' and file_extension != '.json'):
        # TODO: se o bagulho ficar brabo, fazer com que aceite uma lista de extensions
        # por enquanto estamos evitando de dar merda (.bin, .exe e similares)
        print_debug('Arquivo ' + d_file + ' nao tem extensao valida')
        return False
    return True

def alpaca_compare_files(path1, fname1, path2, fname2):
    f_result = RESULT_DIRECTORY + '\\' + fname1 + '_result'
    print(f_result)
    with open(path1) as f1, open(path2) as f2, open(f_result, 'w') as outfile:
        for line1, line2 in zip(f1, f2):
            if line1 == line2:
                print('Igual: ' + line1, end='', file=outfile)
                print_debug('Igual: ' + line1)
            else:
                print('DIFF: ' + line1 + ' --> ' + line2, end='', file=outfile)
                print_debug('DIFF: ' + line1 + ' --> ' + line2)
    
    # TODO...
    # NEEDS_TESTING: cria file f_result em RESULT_DIRECTORY

def run_alpaca(dir1, dir2):
    size_t = dir_getmaxsize(dir1, dir2)
    files1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
    files2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]
    #print(files1)
    #print(files2)
    #print(size_t)
    # wtf
    #for x in range(0, len(files1)):
    #    print(x)
    for x in range(0, size_t):
        if (x < len(files1)):
            path1 = dir1 + '\\' + files1[x]
            fname1 = files1[x]
        if (x < len(files2)):
            fname2 = files2[x]    
            path2 = dir2 + '\\' + files2[x]
        if dir_file_check(path1, path2):
            print_debug('dir_file_check para ' + '{x}' + ' passou')
            if (dir_file_is_valid(path1) and dir_file_is_valid(path2)):
                print_debug('dir_file_is_valid passou tambem')
                alpaca_compare_files(path1, fname1, path2, fname2)


def main(argv):
    dir1 = ''
    dir2 = ''
    if (sys.argv[1] == None or sys.argv[2] == None): # argv[0] e o nome do script
        print('Erro. Utilize py[thon] alpaca.py pasta_1 pasta_2\nCertifique-se que as pastas estao como subdiretorios desta')
        exit(-1)
    dir1 = os.getcwd() + '\\' + sys.argv[1] # pasta atual + \ + arg
    dir2 = os.getcwd() + '\\' + sys.argv[2]
    if (check_dir(dir1, dir2)):
        print('check_dir passou')
        init_dir()
        run_alpaca(dir1, dir2)

if __name__ == "__main__":
   main(sys.argv[1:])