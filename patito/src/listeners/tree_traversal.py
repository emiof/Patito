from typing import Any
from antlr4 import TerminalNode
from ..classifications import Signature, VariableType
from ..syntax import PatitoParser

def extract_id(ctx: Any) -> str:
    if not hasattr(ctx, "ID"):
        raise ValueError("no id token found in the context")
    return ctx.ID().getText()

def extract_type(ctx: PatitoParser.TipoContext) -> str:
    return ctx.getChild(0).getText()

def extract_expression(ctx: PatitoParser.ExpresionContext) -> list[str]:
    if not isinstance(ctx, PatitoParser.ExpresionContext):
        raise ValueError("no expresion found in the context")
    return flatten_tree(ctx)

def extract_signature(ctx: PatitoParser.Opc_lista_id_tipoContext) -> Signature:
    tokens: list[str] = flatten_tree(ctx)
    return [VariableType.to_type(token) for i, token in enumerate(tokens) if tokens[i-1] == ":"]

def flatten_tree(ctx: Any) -> list[str]:
    tokens: list[str] = []
    
    for child in ctx.getChildren():
        if isinstance(child, TerminalNode):
            tokens.append(child.getText())
        else:
            tokens += flatten_tree(child)

    return tokens    

def extract_expression_list(ctx: Any) -> list[PatitoParser.ExpresionContext]:
    if isinstance(ctx, PatitoParser.ExpresionContext):
        return [ctx]
    elif isinstance(ctx, TerminalNode):
        return []
    
    return [expression for child in ctx.getChildren() for expression in extract_expression_list(child)]