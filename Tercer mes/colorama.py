class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(bcolors.WARNING + "Peligro, ten cuidado" + bcolors.ENDC)
print(bcolors.BOLD + "Este texto tiene negritas" + bcolors.ENDC)
print(bcolors.UNDERLINE + "Este texto tiene subrayados" + bcolors.ENDC)
print(bcolors.HEADER + "Alarma!" + bcolors.ENDC)
