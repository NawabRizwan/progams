from cx_Freeze import setup, Executable

base = None


executables = [Executable("OpenFolder.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Open folder",
    options = options,
    version = "1.0",
    description = 'opens any folder',
    executables = executables
)