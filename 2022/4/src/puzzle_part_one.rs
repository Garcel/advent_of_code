use std::ops::RangeInclusive;

pub fn resolve(input: &&str) -> i32 {
    return assignment_pairs_fully_overlapped(input);
}

fn assignment_pairs_fully_overlapped(input: &&str) -> i32 {
    return input
        .lines()
        .filter(|pair| assignment_pair_fully_overlapped(pair))
        .count() as i32;
}

fn assignment_pair_fully_overlapped(pair: &str) -> bool {
    let mut elves = pair.split(',');
    let first_range = parse_range(elves.next().unwrap());
    let second_range = parse_range(elves.next().unwrap());

    return fully_overlapped(first_range, second_range);
}

fn parse_range(range_str: &str) -> RangeInclusive<i32> {
    let mut range_it = range_str.split('-');
    let start = range_it.next().unwrap().parse::<i32>().unwrap();
    let end = range_it.next().unwrap().parse::<i32>().unwrap();

    return RangeInclusive::new(start, end);
}

fn fully_overlapped(first: RangeInclusive<i32>, second: RangeInclusive<i32>) -> bool {
    return (second.contains(&first.start()) && second.contains(&first.end())) ||
        (first.contains(&second.start()) && first.contains(&second.end()));
}
