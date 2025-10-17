from fastmcp import FastMCP

mcp = FastMCP(name = "Calculator")

@mcp.tool()

def multiple(a: float, b: float) -> float:
    """ Multiply two numbers.

    args: a(float): the first number
          b(float): the second number
    
    returns: float
    """
    return a * b

@mcp.tool(
        name="add",
        description="Add two numbers",
        tags={"math", "arithmetic"}
)

def add(a:float, b:float) -> float:
    """ Add two numbers
    args: a(float): the first number
          b(float): the second number

    returns: float
    """
    return a + b

@mcp.tool()

def subtract(a:float, b:float) -> float:
    """ Add two numbers
    args: a(float): the first number
          b(float): the second number

    returns: float
    """
    return a - b

@mcp.tool()

def divide(a:float, b:float) -> float:
    """ Add two numbers
    args: a(float): the first number
          b(float): the second number

    returns: float
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    return a / b

if __name__ == "__main__":
    mcp.run() #STDIO by defualt. 