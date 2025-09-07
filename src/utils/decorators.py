from typing import Any, Callable, Iterable, Tuple, Type

def safe(
    default: Any = None,
    on: Tuple[Type[BaseException], ...] = (Exception,),
    reraise: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Decorator for safe function execution.
    - Returns `default` on errors (of types `on`), if reraise=False.
    - If reraise=True — re-raises the exception.
    """
    def deco(fn: Callable[..., Any]) -> Callable[..., Any]:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return fn(*args, **kwargs)
            except on:
                if reraise:
                    raise
                return default
        return wrapper
    return deco
