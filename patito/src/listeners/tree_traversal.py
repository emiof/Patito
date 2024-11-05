from ..syntax import PatitoParser
from antlr4 import TerminalNode

def extract_id(ctx: any) -> str:
    if not hasattr(ctx, "ID"):
        raise ValueError("no id token found in the context")
    return ctx.ID().getText()

def extract_type(ctx: PatitoParser.TipoContext) -> str:
    return ctx.getChild(0).getText()

def extract_expression(ctx: any) -> list[str]:
    if not hasattr(ctx, "expresion"):
        raise ValueError("no expresion found in the context")
    return extract_expression_aux(ctx.expresion())

def extract_expression_aux(ctx: any) -> list[str]:
    tokens: list[str] = []
    
    for child in ctx.getChildren():
        if isinstance(child, TerminalNode):
            tokens.append(child.getText())
        else:
            tokens += extract_expression_aux(child)

    return tokens



