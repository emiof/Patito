from typing import Any
from antlr4 import TerminalNode
from ..classifications import Signature, VariableType
from ..syntax import PatitoParser

def extract_id(ctx: any) -> str:
    if not hasattr(ctx, "ID"):
        raise ValueError("no id token found in the context")
    return ctx.ID().getText()

def extract_type(ctx: PatitoParser.TipoContext) -> str:
    return ctx.getChild(0).getText()

def extract_expression(ctx: any) -> list[str]:
    if not hasattr(ctx, "expresion"):
        raise ValueError("no expresion found in the context")
    return flatten_tree(ctx.expresion())

def extract_signature(ctx: PatitoParser.Opc_lista_id_tipoContext) -> Signature:
    tokens: list[str] = flatten_tree(ctx)
    return [VariableType.to_type(token) for i, token in enumerate(tokens) if tokens[i-1] == ":"]

def flatten_tree(ctx: any) -> list[str]:
    tokens: list[str] = []
    
    for child in ctx.getChildren():
        if isinstance(child, TerminalNode):
            tokens.append(child.getText())
        else:
            tokens += flatten_tree(child)

    return tokens    



