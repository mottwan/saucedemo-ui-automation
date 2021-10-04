import os
import platform


def get_executable_file_path_for(filename):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '../resources/{}/{}'.format(platform.system(), __executable_file_name(filename)))


def __executable_file_name(binary_file):
    return '{}.exe'.format(binary_file) if platform.system() == 'Windows' else binary_file
