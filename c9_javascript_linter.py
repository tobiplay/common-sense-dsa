from c9_stack_implementation import Stack


class Linter:
    def __init__(self) -> None:
        self.stack = Stack()

    def is_opening_brace(self, char: str) -> bool:
        return char in ["(", "{", "["]

    def is_closing_brace(self, char: str) -> bool:
        return char in [")", "}", "]"]

    def is_not_match(self, opening_brace: str, closing_brace: str) -> bool:
        return {"(": ")", "{": "}", "[": "]"}[opening_brace] != closing_brace

    def lint(self, text: str):
        for char in text:
            if self.is_opening_brace(char):
                self.stack.push(char)

            elif self.is_closing_brace(char):
                popped_opening_brace = ""
                popped_opening_brace = self.stack.pop()

                if not popped_opening_brace:
                    return f"{char} does not have an opening brace"

                if self.is_not_match(popped_opening_brace, char):
                    return f"{char} has a mismatched opening brace"

        if self.stack.read():
            return f"{self.stack.read()} does not have a closing brace"

        return True


Linter_1 = Linter()
print(Linter_1.lint("(var x = {y: [1, 2, 3]})"))
