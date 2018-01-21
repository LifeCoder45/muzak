# noinspection PyMethodMayBeStatic
class Menu:

    def show_welcome(self):
        print('Welcome to MUZAK!')

    def get_mode_selection(self):
        print('\nWhat would you like to practice?')
        print('1) Scales')
        print('2) Chords')
        print('3) Both\n')

        while True:
            val = input('Choice: ')
            if val in ['1', '2', '3']:
                return int(val)

    def get_hints_enabled(self):
        print('\nWould you like hints?')
        print('1) Yes')
        print('2) No\n')

        while True:
            val = input('Choice: ')
            if val in ['1', '2']:
                return val == '1'

    def get_duration(self):
        print('\nHow long would you like between questions, in seconds?\n')

        while True:
            val = input('Choice: ')

            try:
                duration = int(val)

                if duration > 0:
                    return duration
            except ValueError:
                pass
