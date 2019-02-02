__author__ = 'RobertaBtt'

from configparser import SafeConfigParser, ConfigParser
import logging

_logger = logging.getLogger(__name__)
import os

class MusicbrainzPortingConfig:

    @staticmethod
    def get_confi_by_key(key):
        try:
            value = MusicbrainzPortingConfig._get_value(key)
            return value

        except Exception as e:
            _logger.info(str(e))
            return 0


    @staticmethod
    def _get_value(key):
        try:
            module_dir = os.path.dirname(__file__)
            filename = module_dir + '/config.ini'

            if os.path.isfile(filename):
                parser = ConfigParser()
                parser.read(filename)
            else:
                print ("FILE NOT FOUND")

            section = 'DEFAULT'
            parser.read('config.ini')

            value = parser.get(section,  key)
            return value

        except Exception as e:

            raise Exception



MusicbrainzPortingConfig().get_confi_by_key('hostname')


#
# def main():
#     filename = "options.cfg"
#     if os.path.isfile(filename):
#         parser = SafeConfigParser()
#         parser.read(filename)
#         print(parser.sections())
#         screen_width = parser.getint('graphics','width')
#         screen_height = parser.getint('graphics','height')
#     else:
#         print("Config file not found")
#
# if __name__=="__main__":
#     main()