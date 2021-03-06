"""
Generate a coupler DOE
"""
import pp
from pp.components.coupler import coupler
from pp.routing.add_fiber_array import add_fiber_array


@pp.cell
def CP2x2(gap=0.3, length=10.0):
    c = coupler(gap=gap, length=length)
    return add_fiber_array(c)


if __name__ == "__main__":
    c = CP2x2()
    pp.show(c)
