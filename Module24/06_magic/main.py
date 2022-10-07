def get_num(search_elem):
    for key, elem in dict_elem.items():
        if isinstance(search_elem, type(elem)):
            return key
    return 0


def add(fst_elem, sec_elem):
    try:
        return dict_elem[get_num(fst_elem) * get_num(sec_elem)]
    except (TypeError, IndexError, Exception):
        return Nothing()


def subtract(fst_elem, sec_elem):
    try:
        return dict_elem[get_num(fst_elem) / get_num(sec_elem)]
    except (ZeroDivisionError, TypeError, IndexError, Exception):
        return Nothing()


class Nothing:
    def __str__(self):
        return 'Nothing'

    def __add__(self, other):
        return other

    def __sub__(self, other):
        return self


class Water:
    def __str__(self):
        return 'Water'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Air:
    def __str__(self):
        return 'Air'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Fire:
    def __str__(self):
        return 'Fire'

    def __abs__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Earth:
    def __str__(self):
        return 'Earth'

    def __abs__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Storm:
    def __str__(self):
        return 'Storm'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Steam:
    def __str__(self):
        return 'Steam'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Mud:
    def __str__(self):
        return 'Mud'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Lightning:
    def __str__(self):
        return 'Lightning'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Dust:
    def __str__(self):
        return 'Dust'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Lava:
    def __str__(self):
        return 'Lava'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class WaterReservoir:
    def __str__(self):
        return 'WaterReservoir'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Tsunami:
    def __str__(self):
        return 'Tsunami'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class HotSpring:
    def __str__(self):
        return 'HotSpring'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


class Swamp:
    def __str__(self):
        return 'Swamp'

    def __add__(self, other):
        return add(self, other)

    def __sub__(self, other):
        return subtract(self, other)


dict_elem = {0: Nothing(), 2: Water(), 3: Air(), 5: Fire(), 7: Earth(), 2*2: WaterReservoir(),
             2*3: Storm(), 2*5: Steam(), 2*7: Mud(), 3*5: Lightning(), 3*7: Dust(), 5*7: Lava(),
             2*2*3: Tsunami(), 2*2*5: HotSpring(), 2*2*7: Swamp()}

# for elem in [Nothing(), Water(), Air(), Fire(), Earth(), WaterReservoir(), Storm(), Steam(), Mud()]:
for elem in dict_elem.values():
    print()
    print('{} + {} = {}'.format(Water(), elem, Water() + elem))
    print('{} - {} = {}'.format(elem, Water(), elem - Water()))
