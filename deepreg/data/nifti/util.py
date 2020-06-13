import glob
import os


def get_sorted_filenames_in_dir(dir_path: str, suffix: str = ""):
    """
    Return the path of all files under the given directory.

    :param dir_path: path of the directory
    :param suffix: suffix of filenames like h5, nii.gz, should not start with .
    :return: list of file paths
    """
    return sorted(glob.glob(os.path.join(dir_path, "**", "*." + suffix), recursive=True))


def check_difference_between_two_lists(list1: list, list2: list):
    """
    Raise error if two lists are not identical
    :param list1: 
    :param list2: 
    :param err_msg: 
    :return: 
    """

    list1_unique = sorted(set(list1) - set(list2))
    list2_unique = sorted(set(list2) - set(list1))
    if len(list2_unique) != 0 or len(list1_unique) != 0:
        raise ValueError("two lists are not identical\n"
                         "list1 has unique elements {}\n"
                         "list2 has unique elements {}\n".format(list1_unique, list2_unique))
