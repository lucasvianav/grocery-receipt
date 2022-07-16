import re

from utils import parse_float


class Product:
    """Represent a grocery product."""

    __name: str
    __quantity: float
    __measurement_unity: str
    __unit_price: float
    __price: float
    __pricing_inconsistent: bool

    def __init__(self, raw: str):
        matches: list[tuple[str, ...]] = re.findall(
            r"^[\w\d]*\s*[a-z\s]*([\w\d\s]+?)\s*(\d*,?\d*(UN|KG)) x (\d*,?\d*).+?(\d*,?\d*)$",
            self.__substitute_common_mistakes(raw.strip()),
        )

        if not matches:
            raise RuntimeError("Product data couldn't be parsed.")

        name, quantity, unity, unit_price, price = matches[0]

        self.__name = name.title()
        self.__quantity = parse_float(quantity.replace(unity, ""))
        self.__measurement_unity = unity.lower()
        self.__unit_price = parse_float(unit_price)
        self.__price = parse_float(price)
        self.__pricing_inconsistent = (
            abs(self.__unit_price * self.__quantity - self.__price) > 1
        )

    def __str__(self) -> str:
        representation = [
            f"Product name: {self.get_name()}\n",
            f"Quantity bought: {self.get_quantity()}",
            " (maybe)\n" if self.__pricing_inconsistent else "\n",
            f"Price per {self.__measurement_unity}: R${self.get_unit_price()}",
            " (maybe)\n" if self.__pricing_inconsistent else "\n",
            f"Total price: R${self.get_price()}",
            " (maybe)" if self.__pricing_inconsistent else "",
        ]
        return "".join(representation)

    def get_quantity(self) -> str:
        return f"{self.__quantity} {self.__measurement_unity}."

    def get_name(self) -> str:
        return self.__name

    def get_unit_price(self) -> float:
        return self.__unit_price

    def get_price(self) -> float:
        return self.__price

    def __substitute_common_mistakes(self, raw: str) -> str:
        """Correct common OCR mistakes from when parsing a grocery product from a receipt photo."""
        return (
            raw.replace("JUN", "1UN")
            .replace("]", "I")
            .replace("[", "L")
            .replace("\n", " ")
            .replace("k9", "kg")
        )
