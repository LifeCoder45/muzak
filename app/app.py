import random
import textwrap

from app.data import Data
from utils.utils import Utils


class App:
    def __init__(self, chords, scales, hints, duration):
        self.chords = chords
        self.scales = scales
        self.hints = hints
        self.duration = duration

        self.data = Data()

    def run(self):
        print('\nStarting, use CTRL+C to stop!')

        Utils.sleep(3)

        while True:
            Utils.clear()

            form = self.data.get_form()
            position = self.data.get_position()
            form_type, hint = self.get_form_hint(form)

            form_hint = textwrap.dedent(hint)

            print(f'{form_type}: {form.name} form, {position} position')

            if self.hints:
                print(f'\n{form_hint}')

            Utils.sleep(self.duration)

    def get_form_hint(self, form):
        if self.chords and not self.scales:
            return 'Chord', form.chord

        if self.scales and not self.chords:
            return 'Scale', form.scale

        if random.randint(1, 10) % 2 == 0:
            return 'Chord', form.chord
        else:
            return 'Scale', form.scale
