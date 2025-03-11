class StringUtils:
   

    def capitalize(self, string: str) -> str:
       capitilize("skypro") -> "Skypro"
        return string.capitalize()

    def trim(self, string: str) -> str:
        trim("   skypro") -> "skypro"
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        string - строка для обработки
        symbol - искомый символ
        contains("SkyPro", "S") -> True
        contains("SkyPro", "U") -> False
        res = False
        try:
            res = string.index(symbol) > -1
        except ValueError:
            pass
        return res

    def delete_symbol(self, string: str, symbol: str) -> str:
        delete_symbol("SkyPro", "k") -> "SyPro"
        delete_symbol("SkyPro", "Pro") -> "Sky"
        if self.contains(string, symbol):
            string = string.replace(symbol, "")
        return string
