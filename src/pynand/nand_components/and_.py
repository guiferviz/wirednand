from pynand.core import Bus, Component, Status, component, simulation
from pynand.nand_components.nand import nand
from pynand.nand_components.not_ import not_


@component
def and_(a: Bus, b: Bus) -> dict[str, Bus]:
    nand1 = nand(a, b)
    not1 = not_(nand1.outputs["q"])
    return {"q": not1.outputs["q"]}


@simulation(and_)
def and_simulation(component: Component, status: Status) -> None:
    a, b = component.inputs["a"], component.inputs["b"]
    q = component.outputs["q"]
    status[q] = status[a] & status[b]
