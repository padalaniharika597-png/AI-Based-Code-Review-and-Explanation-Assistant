import ast


def check_syntax(code):
    try:
        ast.parse(code)

        return {
            "valid": True,
            "error": None
        }

    except SyntaxError as e:
        return {
            "valid": False,
            "error": str(e)
        }