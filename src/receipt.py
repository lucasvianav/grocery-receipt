import re

from product import Product
from utils import get_n_leading_zeros, parse_float


class Receipt:
    """Represent a grocery receipt."""

    __products: list[Product] = []
    """All grocery products in a receipt."""
    __value: float
    """The receipt's total value/price."""
    __pricing_inconsistent: bool
    """
    If the total price read from the raw text is too different from the on
    calculated through the sum of all products.
    """

    def __init__(self, raw: str):
        items_indexes = re.findall(r"^\d+\s+", raw, re.IGNORECASE + re.MULTILINE)
        price_regex = r"^Total\s*R\$\s*(\d{1,},\d{2}).*$"
        price_line = re.search(price_regex, raw, re.IGNORECASE + re.MULTILINE)

        # search for the total price line in the raw text
        if price_line:
            price_line_start, _ = price_line.span()
            price = re.findall(price_regex, raw, re.IGNORECASE + re.MULTILINE)[0]
            products_raw = raw[:price_line_start]
        else:
            price = None
            products_raw = raw

        # split products raw text into a list
        split_pivot = "||<<>>####+####<<>>||"
        for i in items_indexes:
            products_raw = products_raw.replace(i, split_pivot)
        products_raw_arr = products_raw.split(split_pivot)[1:]

        # parse products and save the successful ones
        for p_raw in products_raw_arr:
            try:
                product = Product(p_raw)
            except RuntimeError:
                pass
            else:
                self.__products.append(product)

        if not self.__products:
            raise RuntimeError("The receipt's products' data could not be parsed")

        # save the total price
        try:
            sum_products = sum([p.get_price() for p in self.__products])
            inconsistent = not price and any(
                [p.get_price_inconsistency() for p in self.__products]
            )
            self.__value = parse_float(price) if price else sum_products
            self.__pricing_inconsistent = (
                inconsistent or abs(sum_products - self.__value) > 3
            )
        except Exception:
            raise RuntimeError("The receipt's products' data could not be parsed")

    def __str__(self):
        n_leading_zeros = get_n_leading_zeros(len(self.__products))
        string = "\n\n".join(
            [
                f"Product #{str(i + 1).zfill(n_leading_zeros)}\n{p}"
                for i, p in enumerate(self.__products)
            ]
        )
        string += f"\n\nTOTAL RECEIPT VALUE: R${self.get_value()}"
        string += " (maybe)" if self.__pricing_inconsistent else ""
        return string

    def get_products(self):
        return self.__products

    def get_value(self):
        return self.__value
