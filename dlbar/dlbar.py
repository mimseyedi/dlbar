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


import re
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

        for validator_function in [
            self.__check_width(width=width),
            self.__check_chars(char=empty_char),
            self.__check_chars(char=filled_char),
            self.__check_bools(boolean=status),
            self.__check_bools(boolean=percent)
        ]:
            response, exception = validator_function
            if not response:
                raise exception

        self._width = width
        self._empty_char = empty_char
        self._filled_char = filled_char
        self._status = status
        self._percent = percent


    def download(self, url: str, dest: str|Path, title: str, chunk_size: int=4096) -> None:
        """
        
        :param url: 
        :param dest: 
        :param title: 
        :param chunk_size: 
        :return: None
        """

        with open(dest, 'wb') as output_file:
            sys.stdout.write(title + "\n")

            response: requests.Response = requests.get(url, stream=True)
            total_length = response.headers.get('content-length')

            if total_length is None:
                output_file.write(response.content)
            else:
                downloaded = 0
                total_length = int(total_length)

                for data in response.iter_content(chunk_size=chunk_size):
                    output_file.write(data)
                    downloaded += len(data)

                    bar = int(self._width * downloaded / total_length)

                    sys.stdout.write(
                        "\r%s %s%s %s " % (
                            str(downloaded * 100 // total_length) + "%"
                            if self._percent else "",

                            self._filled_char * bar,
                            self._empty_char * (self._width - bar),

                            str(self.convert_size(downloaded)) + "/" + str(self.convert_size(total_length))
                            if self._status else ''
                        )
                    )

                    sys.stdout.flush()


    @property
    def width(self) -> int:
        return self._width


    @width.setter
    def width(self, width: int) -> None:
        response, exception = self.__check_width(width=width)
        if not response:
            raise exception

        self._width = width


    @property
    def empty_char(self) -> str:
        return self._empty_char


    @empty_char.setter
    def empty_char(self, empty_char: str) -> None:
        response, exception = self.__check_chars(char=empty_char)
        if not response:
            raise exception

        self._empty_char = empty_char


    @property
    def filled_char(self) -> str:
        return self._filled_char


    @filled_char.setter
    def filled_char(self, filled_char) -> None:
        response, exception = self.__check_chars(char=filled_char)
        if not response:
            raise exception

        self._filled_char = filled_char


    @property
    def status(self) -> bool:
        return self._status


    @status.setter
    def status(self, status) -> None:
        response, exception = self.__check_bools(boolean=status)
        if not response:
            raise exception

        self._status = status


    @property
    def percent(self) -> bool:
        return self._percent


    @percent.setter
    def percent(self, percent) -> None:
        response, exception = self.__check_bools(boolean=percent)
        if not response:
            raise exception

        self._percent = percent


    @staticmethod
    def convert_size(size: int) -> str:
        """

        :param size:
        :return:
        """

        for rng in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024.0:
                return "%3.0f %s" % (size, rng) if rng == 'KB' \
                    else "%3.3f %s" % (size, rng)

            size /= 1024.0


    @staticmethod
    def __check_width(width: int) -> tuple[bool, None|Exception]:
        """

        :param width:
        :return:
        """

        if isinstance(width, int):
            if width >= 10:
                return True, None

            return False, ValueError(f"The width value should not be less than 10. The current width is {width}.")

        return False, TypeError(f"The width of the download bar must be an integer. But type {type(width).__name__} received.")


    @staticmethod
    def __check_chars(char: str) -> tuple[bool, None|Exception]:
        """

        :param char:
        :return:
        """

        if isinstance(char, str):
            ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
            cleared_char = ansi_escape.sub('', char)

            if len(cleared_char) == 1:
                return True, None

            return False, ValueError(f"The length of a character should not be more or less than 1. The current length is {len(char)}.")

        return False, TypeError(f"A character must be of string type. But type {type(char).__name__} received.")


    @staticmethod
    def __check_bools(boolean: bool) -> tuple[bool, None|Exception]:
        """

        :param boolean:
        :return:
        """

        if isinstance(boolean, bool):
            return True, None

        return False, TypeError(f"The value must be of boolean type. But type {type(boolean).__name__} received.")
