import os
from modulefinder import ModuleFinder

finder = ModuleFinder()


def get_all_imported_modules(python_module: str):
    finder.run_script(python_module)
    imported_modules = []
    for name, mod in finder.modules.items():
        imported_modules.append(name)
    return imported_modules


if __name__ == '__main__':
    code_main_dir = r"C:\Users\saar.nehemia\PycharmProjects\pirate_bot_game"
    exclude_dirs = ['.git', '.idea', 'venv', '__pycache__']
    for dirpath, dirnames, filenames in os.walk(code_main_dir):

        is_continue = False
        for exclude_dir in exclude_dirs:
            if dirpath.find(exclude_dir) != -1:
                is_continue = True
        if is_continue:
            continue

        if dirpath not in exclude_dirs:
            print(dirpath)
            include_dirnames = [dirname for dirname in dirnames if dirname not in exclude_dirs]
            print(include_dirnames)
            python_modules = [f for f in filenames if f.endswith(".py")]
            print(python_modules)
            for python_module in python_modules:
                print(python_module + ":")
                full_path = os.path.join(dirpath, python_module)
                print(get_all_imported_modules(full_path))
                # a = dir(full_path)
                # for item in a:
                #     print(type(item))

                print()

            breakpoint()
