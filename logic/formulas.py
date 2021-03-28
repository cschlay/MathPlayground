from __future__ import annotations


class Formula:
    def __init__(self, name: str, value: bool, atomic: bool = True):
        self.name: str = name
        self.value: bool = value
        self.atomic: bool = atomic

    def apply_and(self, formula: Formula) -> Formula:
        name: str = self._build_binary_name(formula, symbol=u'\u2227')
        return Formula(name, self.value and formula.value, atomic=False)

    def apply_equivalence(self, formula: Formula):
        name: str = self._build_binary_name(formula, symbol=u'\u2194')
        return Formula(name, self.value == formula.value, atomic=False)

    def apply_implies(self, formula: Formula):
        name: str = self._build_binary_name(formula, symbol=u'\u2192')
        value: bool = False if self.value and not formula.value else True
        return Formula(name, value, atomic=False)

    def apply_not(self) -> Formula:
        symbol = u'\u00AC'
        if self.atomic:
            name: str = f"{symbol}{self.name}"
        else:
            name: str = f"{symbol}({self.name})"
        return Formula(name, not self.value, atomic=False)

    def apply_or(self, formula: Formula) -> Formula:
        name: str = self._build_binary_name(formula, symbol=u'\u2228')
        return Formula(name, self.value or formula.value, atomic=False)

    def _build_binary_name(self, formula: Formula, symbol: str) -> str:
        name: str = ""
        if self.atomic:
            name += self.name
        else:
            name += f"({self.name})"
        name += f" {symbol} "
        if formula.atomic:
            name += formula.name
        else:
            name += f"({formula.name})"
        return name

    def __str__(self):
        return f"{self.name} = {self.value}"


class Truth(Formula):
    def __init__(self):
        super().__init__("T", True)


class Falsity(Formula):
    def __init__(self):
        super().__init__("F", False)
