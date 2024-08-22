import pytest

from wirednand.core import Bus
from wirednand.nand_components.not_ import not_
from wirednand.simulator import Simulator


@pytest.mark.parametrize(
    "inputs, outputs",
    [
        [dict(a=0), dict(q=1)],
        [dict(a=1), dict(q=0)],
    ],
)
def test_nand(inputs, outputs):
    input_buses = {i: Bus() for i in inputs}
    component = not_(*input_buses.values())
    simulator = Simulator(component)
    for k, v in inputs.items():
        input_bus = input_buses[k]
        simulator.status[input_bus] = v
    simulator.status.commit()
    simulator.step()
    for k, v in outputs.items():
        output_bus = component.outputs[k]
        assert simulator.status[output_bus] == v