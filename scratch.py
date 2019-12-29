import logging

import stm32pio.lib
import stm32pio.settings


class ProjectLogHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        print(record.args)
        print('NEW MSG', self.format(record))

# root_logger = logging.getLogger('stm32pio')
# root_logger.setLevel(logging.DEBUG)

# project = stm32pio.lib.Stm32pio('C:/Users/chufyrev/Documents/GitHub/stm32pio/stm32pio-test-project',
#                                 parameters={'board': 'nucleo_f031k6'},
#                                 save_on_destruction=False)

# string_handler = ProjectLogHandler()
# project.logger.addHandler(string_handler)
# project.logger.setLevel(logging.DEBUG)
# string_handler.setFormatter(logging.Formatter("%(levelname)-8s "
#                                               f"%(funcName)-{stm32pio.settings.log_fieldwidth_function}s "
#                                               "%(message)s"))

# project.config.save()
# print(f'the state is: {str(project.state)}')
# project.generate_code()
# print(f'the state is: {str(project.state)}')


class Base:
    def __init__(self):
        print('base:   ', id(self))

class Child(Base):
    def __init__(self):
        print('child 1:', id(self))
        super().__init__()
        print('child 2:', id(self))

inst = Child()
