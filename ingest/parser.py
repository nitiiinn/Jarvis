from tree_sitter_language_pack import get_parser


class CodeParser:

    def __init__(self):

        self.parsers = {}

    def get_language_parser(self, language):

        if language not in self.parsers:
            self.parsers[language] = get_parser(language)

        return self.parsers[language]

    def parse_code(self, code, language):

        parser = self.get_language_parser(language)

        tree = parser.parse(bytes(code, "utf-8"))

        return tree