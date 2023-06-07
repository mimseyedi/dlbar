"""
██████╗ ██╗     ██████╗  █████╗ ██████╗
██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗
██║  ██║██║     ██████╔╝███████║██████╔╝
██║  ██║██║     ██╔══██╗██╔══██║██╔══██╗
██████╔╝███████╗██████╔╝██║  ██║██║  ██║
╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝

dlbar is a simple terminal progress bar for downloading and displaying download progress.

Github repository: https://github.com/mimseyedi/dlbar
"""


import sys
import requests
from pathlib import Path


class DownloadBar:

    def __init__(self, width: int=50, empty_char: str=f"\033[31m{chr(9472)}\033[0m",
            filled_char: str=f"\033[32m{chr(9472)}\033[0m", status: bool=True,
            percent: bool=True) -> None:
        
        """
        
        :param width: 
        :param empty_char: 
        :param filled_char: 
        :param status:
        :param percent: 
        """

        pass


    def download(self, url: str, dest: Path, title: str, chunk_size: int=4096) -> None:
        """
        
        :param url: 
        :param dest: 
        :param title: 
        :param chunk_size: 
        :return: 
        """
        
        pass
    
    
    @property
    def width(self) -> int:
        pass


    @width.setter
    def width(self, width: int) -> None:
        pass


    @property
    def empty_char(self) -> str:
        pass


    @empty_char.setter
    def empty_char(self, empty_char: str) -> None:
        pass


    @property
    def filled_char(self) -> str:
        pass


    @filled_char.setter
    def filled_char(self, filled_char) -> None:
        pass


    @property
    def status(self) -> bool:
        pass


    @status.setter
    def status(self, status) -> None:
        pass


    @property
    def percent(self) -> bool:
        pass


    @percent.setter
    def percent(self, percent) -> None:
        pass


    @staticmethod
    def convert_size(size: int) -> str:
        """

        :param size:
        :return:
        """

        pass


    @staticmethod
    def __check_width(width: int) -> tuple[bool, None|Exception]:
        """

        :param width:
        :return:
        """

        if isinstance(width, int) and width >= 10:
            return True, None

        return False, ValueError("The width of the download bar must be an integer and not less than 10.")


    @staticmethod
    def __check_chars(char: str) -> tuple[bool, None|Exception]:
        """

        :param char:
        :return:
        """

        if isinstance(char, str) and len(char) == 1:
            return True, None

        return False, ValueError("A character must be of string type and its length must be equal to 1.")


    @staticmethod
    def __check_bools(boolean: bool) -> tuple[bool, None|Exception]:
        """

        :param boolean:
        :return:
        """

        if isinstance(boolean, bool):
            return True, None

        return False, TypeError(f"The value must be of boolean type. But type {type(boolean).__name__} received.")
