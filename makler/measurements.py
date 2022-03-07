from decimal import Decimal


class LengthInMeters(Decimal):
    pass


class AreaInSquareMeters(Decimal):

    def __str__(self) -> str:
        return f'{super()}m²'
