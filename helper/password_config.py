import re


class PasswordConfig:

    __regex = {
        'Lowercase': 'a-z',
        'Uppercase': 'A-Z',
        'Numbers': '\d',
        'Symbols': '_\W\D'
    }
    options = {
        'Lowercase': True,
        'Uppercase': True,
        'Numbers': False,
        'Symbols': False
    }
    length = '0'
    password = ''


    def __init__(self):
        pass

    def _get_regex(self) -> str:
        pref = ['^']
        post = []

        for key in self.__regex.keys():
            if self.options[key]:
                pref.append(f'(?=.*[{self.__regex[key]}])')
                post.append(self.__regex[key])

        pref.extend(['[', *post, ']{6,32}$'])

        return ''.join(pref)

    def is_match_options(self) -> bool:
        regex = re.compile(self._get_regex())

        return bool(re.search(regex, self.password))

    def is_match_length(self) -> bool:

        return int(self.length) == len(self.password)
