def clamp(val: int, max_val: int | float = None, min_val: int | float = None) -> int | float:
    """
    This function limits a value to a maximum and minimum

    `val`: Value to be clamped
    `max_val`: Maximum constraint
    `min_val`: Minimum constraint
    """
    if min_val != None and max_val != None:
        return max(min(val, max_val), min_val)
    elif min_val != None and max_val == None:
        return max(val, min_val)
    elif min_val == None and max_val != None:
        return min(val, max_val)


def move_toward(val: int | float = 0, dest: int | float = 100, step: int | float = 1):
    """
    This function moves a value towards another value

    `val`: Value to move
    `dest`: Final value
    `step`: Step between values
    """
    if val < dest:
        val = clamp(val + abs(step), dest)
    if val > dest:
        val = clamp(val - abs(step), dest)
    return val


class Tween():
    """A class of easing functions to improve moving between values
    
    See Wiki for more details."""

    def lerp(start_val: int | float = 0, dest_val: int | float = 0, pct: int | float = 100):
        """For use in `Tween()`: Allows smooth interpolation between values using various functions
        `start_val`: Original value
        `dest_val`: Final value
        `pct`: Current Percentage"""
        return (start_val + (dest_val - start_val) * pct)

    def flip(x: int | float):
        """For use in `lerp()`: Acts as a flip for a graph function"""
        return 1 - x

    def spike(t: int | float):
        """For use in `lerp()`: Acts as a bounce (Mirror) function"""
        if t <= 0.5:
            return Tween.in_quad(t / 0.5)
        return Tween.in_quad(Tween.flip(t) / 0.5)

    def in_quad(t: int | float):
        """For use in `lerp()`: Acts as a quadratic for smoothing in"""
        return t * t

    def out_quad(t: int | float):
        """For use in `lerp()`: Acts as a quadratic for smoothing out"""
        return Tween.flip(Tween.flip(t) ** 2)

    def in_out_quad(t: int | float):
        """For use in `lerp()`: Combines `in_quad()` and `out_quad()`"""
        return Tween.lerp(Tween.in_quad(t), Tween.out_quad(t), t)
