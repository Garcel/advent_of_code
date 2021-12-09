import os
import sys


def main():
    total_output_value = 0

    for row in open(os.path.join(sys.path[0], 'input'), 'r'):
        parts = row.split('|')
        unique_signal_patterns = parts[0].strip().split()
        signal_patterns_mapping = decode_signals(unique_signal_patterns)

        output_values = parts[1].split()

        current_output_value = []

        for output_value in output_values:
            sorted_output_value = ''.join(sorted(output_value))

            current_output_value.append(signal_patterns_mapping.get(sorted_output_value))

        strings = [str(integer) for integer in current_output_value]
        string_number = ''.join(strings)
        total_output_value += int(string_number)

    print(total_output_value)


def decode_signals(signals: [str]) -> dict:
    signal_patterns_mapping = {}
    easy_signal_digits_mapping = {}
    pending_signals = []

    for signal in signals:
        sorted_signal = ''.join(sorted(signal))
        signal_len = len(signal)

        if signal_len == 2:
            signal_patterns_mapping[sorted_signal] = 1
            easy_signal_digits_mapping[1] = sorted_signal
        elif signal_len == 3:
            signal_patterns_mapping[sorted_signal] = 7
            easy_signal_digits_mapping[7] = sorted_signal
        elif signal_len == 4:
            signal_patterns_mapping[sorted_signal] = 4
            easy_signal_digits_mapping[4] = sorted_signal
        elif signal_len == 7:
            signal_patterns_mapping[sorted_signal] = 8
            easy_signal_digits_mapping[8] = sorted_signal
        else:
            pending_signals.append(sorted_signal)

    if 1 not in easy_signal_digits_mapping and 4 in easy_signal_digits_mapping and 7 in easy_signal_digits_mapping:
        easy_signal_digits_mapping[1] = ''.join(
            sorted(set(easy_signal_digits_mapping.get(4)).intersection(easy_signal_digits_mapping.get(7)))
        )
        signal_patterns_mapping[easy_signal_digits_mapping.get(1)] = 1

    for pending_signal in pending_signals:
        signal_len = len(pending_signal)

        if signal_len == 6:
            # 0, 6, 9
            # 6 contains one of the 1 segments
            if [segment in pending_signal for segment in easy_signal_digits_mapping.get(1)].count(True) == 1:
                signal_patterns_mapping[pending_signal] = 6
                easy_signal_digits_mapping[6] = pending_signal

            # 9 contains all 4 segments
            elif all(segment in pending_signal for segment in easy_signal_digits_mapping.get(4)):
                signal_patterns_mapping[pending_signal] = 9
                easy_signal_digits_mapping[9] = pending_signal
            else:
                signal_patterns_mapping[pending_signal] = 0

        elif signal_len == 5:
            # 2, 3, 5
            # 3 contains all 1 segments
            if all(segment in pending_signal for segment in easy_signal_digits_mapping.get(1)):
                signal_patterns_mapping[pending_signal] = 3

            # 2 contains one of the 1 segments and does not contain the 1 segments contained by 6
            elif is_number_five(pending_signal, easy_signal_digits_mapping):
                signal_patterns_mapping[pending_signal] = 5
            else:
                signal_patterns_mapping[pending_signal] = 2

    return signal_patterns_mapping


def is_number_five(signal: str, mapping: dict) -> bool:
    # check against 9
    if 9 in mapping and len(''.join(sorted(set(mapping.get(9)).intersection(signal)))) == 5:
        return True
    elif 6 in mapping and len(''.join(sorted(set(mapping.get(6)).intersection(signal)))) == 5:
        return True
    elif 4 in mapping and len(''.join(sorted(set(mapping.get(4)).intersection(signal)))) == 3:
        return True

    return False


if __name__ == "__main__":
    main()
