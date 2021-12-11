import os
import re
import sys
import typing
from collections import OrderedDict
from enum import Enum
from typing import Union

UNARY_OPERATOR_REGEX = re.compile('NOT ([a-z]+) -> ([a-z]+)')
BINARY_OPERATOR_REGEX = re.compile('([a-z]+|[0-9]+) (AND|OR|LSHIFT|RSHIFT) ([a-z]+|[0-9]+) -> ([a-z]+)')
ASSIGNMENT_REGEX = re.compile('([a-z]+|[0-9]+) -> ([a-z]+|[0-9]+)')


def main():
    with open(os.path.join(sys.path[0], 'input'), 'r') as input_file:
        print(puzzle1(input_file))


def puzzle1(input_file: typing.TextIO):
    circuit = Circuit()

    for row in input_file:
        operation, *args = parse_instruction(row.strip())

        circuit.execute(operation, *args)

    return circuit.get_wire_signals()


class OperationKind(Enum):
    ASSIGN = 0
    AND = 1
    OR = 2
    LSHIFT = 3
    RSHIFT = 4
    NOT = 5


def parse_binary_operation(command: str) -> OperationKind:
    if command == 'AND':
        return OperationKind.AND
    elif command == 'OR':
        return OperationKind.OR
    elif command == 'LSHIFT':
        return OperationKind.LSHIFT
    else:
        return OperationKind.RSHIFT


def parse_instruction(instruction: str) -> (OperationKind, Union[int, str]):
    m_unary = UNARY_OPERATOR_REGEX.fullmatch(instruction)
    m_binary = BINARY_OPERATOR_REGEX.fullmatch(instruction)
    m_assign = ASSIGNMENT_REGEX.fullmatch(instruction)

    if m_unary:
        operation = OperationKind.NOT
        return operation, m_unary.group(2), m_unary.group(1)

    elif m_binary:
        operation = parse_binary_operation(m_binary.group(2))
        operand1 = m_binary.group(1)
        operand2 = m_binary.group(3)
        target = m_binary.group(4)

        return operation, target, operand1, operand2
    else:
        operation = OperationKind.ASSIGN
        return operation, m_assign.group(2), m_assign.group(1)


class Operation:
    kind: OperationKind
    target: str
    operands: OrderedDict[str: Union[int, None]]

    def __init__(self, kind: OperationKind, target: str, **kargs: (str, Union[int, None])):
        self.kind = kind
        self.target = target
        self.operands = OrderedDict()

        for name, value in kargs.items():
            self.operands[name] = value

    def is_ready(self) -> bool:
        return not self.get_pending_operands()

    def get_pending_operands(self) -> [str]:
        return [key for key, value in self.operands.items() if value is None]

    def execute(self) -> (str, int):
        if self.kind == OperationKind.ASSIGN:
            result = self.operands.popitem(last=False)[1]
        elif self.kind == OperationKind.NOT:
            result = ~self.operands.popitem(last=False)[1] & 0xFFFF
        elif self.kind == OperationKind.AND:
            result = self.operands.popitem(last=False)[1] & self.operands.popitem(last=False)[1]
        elif self.kind == OperationKind.OR:
            result = self.operands.popitem(last=False)[1] | self.operands.popitem(last=False)[1]
        elif self.kind == OperationKind.LSHIFT:
            result = self.operands.popitem(last=False)[1] << self.operands.popitem(last=False)[1]
        else:
            result = self.operands.popitem(last=False)[1] >> self.operands.popitem(last=False)[1]

        return self.target, result

    def set_operand(self, name: str, value: int):
        self.operands[name] = value


class Circuit:
    wires_signals: [[int]]
    pending: {str: [Operation]}

    def __init__(self):
        self.wires_signals = {}
        self.pending = {}

    def execute(self, operation_kind: OperationKind, *args):
        operands = {}
        for i in range(1, len(args)):
            arg = args[i]

            if arg.isdigit():
                operands[f"literal{i}"] = int(arg)
            else:
                operands[arg] = self.wires_signals.get(arg)

        operation = Operation(operation_kind, args[0], **operands)

        if operation.is_ready():
            target_name, target_value = operation.execute()
            self.wires_signals[target_name] = target_value
            self._dispatch_result(target_name)
        else:
            self._delay_operation(operation)

    def _delay_operation(self, operation: Operation):
        for operand in operation.get_pending_operands():
            if operand in self.pending:
                self.pending[operand].append(operation)
            else:
                self.pending[operand] = [operation]

    def _dispatch_result(self, wire: str):
        if wire not in self.pending:
            return

        while self.pending[wire]:
            operation = self.pending[wire].pop()
            operation.set_operand(wire, self.wires_signals[wire])

            if operation.is_ready():
                target_name, target_value = operation.execute()
                self.wires_signals[target_name] = target_value
                self._dispatch_result(target_name)

    def get_wire_signals(self) -> dict:
        return self.wires_signals


if __name__ == "__main__":
    main()
