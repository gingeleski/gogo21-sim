class Card:
    def __init__(self, value, alt_value=None):
        self.value = value
        self.alt_value = alt_value

    def get_value(self):
        """

        :rtype: int
        """
        return self.value

    def has_alt_value(self):
        if self.alt_value is not None:
            return True
        return False

    def set_alt_value(self, alt_value):
        self.alt_value = alt_value

    def get_alt_value(self):
        return self.alt_value
