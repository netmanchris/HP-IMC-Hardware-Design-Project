from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [], include_files =['HPIMC_Plat_HardwareSchemes.csv'])

base = 'Console'

executables = [
    Executable('Plat_Sizing_Project.py', base=base)
]

setup(name='HP_IMC_Sizing_Calculator',
      version = '1.7',
      author = '@netmanchris',
      description = 'HP IMC Sizing Calculator version 1.7\n Platform Only',
      options = dict(build_exe = buildOptions),
      executables = executables)








