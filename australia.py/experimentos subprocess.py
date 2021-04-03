import subprocess

saida = subprocess.run(['echo', 'teste testado do teste'], shell=True, capture_output=True, text=True)
print(saida.stdout)
