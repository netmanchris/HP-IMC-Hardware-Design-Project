from cx_Freeze import setup, Executable
setup( name = "HP_IMC_Sizing_Calculator",
       version = "1.0",
       description = "HP IMC Sizing Calculator version 1.\n Platform Only",
       executables = [Executable("Plat_Sizing_Project.py")]
         )
