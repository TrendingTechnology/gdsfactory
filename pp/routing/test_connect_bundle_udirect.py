import numpy as np

import pp


@pp.cell
def test_connect_u_direct():
    w = h = 10
    c = pp.Component()
    pad_south = pp.c.pad_array(port_list=["S"], spacing=(15, 0), width=w, height=h)
    pt = c << pad_south
    pb = c << pad_south
    pb.rotate(90)
    pt.rotate(90)
    pb.move((0, -100))

    pbports = pb.get_ports_list()
    ptports = pt.get_ports_list()

    pbports.reverse()

    routes = pp.routing.connect_bundle(pbports, ptports)
    lengths = [36.436, 76.436, 116.436, 156.436, 196.436]

    for route, length in zip(routes, lengths):
        # print(route["settings"]["length"])
        c.add(route["references"])
        assert np.isclose(route["settings"]["length"], length)

    return c


if __name__ == "__main__":
    c = test_connect_u_direct()
    pp.show(c)
