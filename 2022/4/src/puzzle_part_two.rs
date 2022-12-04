use core::cmp::max;
use core::cmp::min;
use range_set::range_compare::RangeDisjoint;
use std::ops::RangeInclusive;
use std::slice::Iter;

pub fn resolve(input: &&str) -> i32 {
    return assignment_sections_fully_overlapped(input);
}

fn assignment_sections_fully_overlapped(input: &&str) -> i32 {
    let ranges: Vec<RangeInclusive<i32>> = input
        .lines()
        .map(|pair| to_range(pair))
        .filter(|(first, second)| assignment_pair_overlaps(first, second))
        .map(|(first, second)| assignment_pair_range(first, second))
        .collect();

    return ranges
        .iter()
        .filter(|range| fully_overlaps_ranges(range, ranges.iter()))
        .count() as i32;
}

fn to_range(pair: &str) -> (RangeInclusive<i32>, RangeInclusive<i32>) {
    let mut elves = pair.split(',');
    let first_range = parse_range(elves.next().unwrap());
    let second_range = parse_range(elves.next().unwrap());

    return (first_range, second_range);
}

fn assignment_pair_range(first_range: RangeInclusive<i32>, second_range: RangeInclusive<i32>)
    -> RangeInclusive<i32> {
    return RangeInclusive::new(
        min(*first_range.start(), *second_range.start()),
        max(*first_range.end(), *second_range.end()),
    );
}

fn parse_range(range_str: &str) -> RangeInclusive<i32> {
    let mut range_it = range_str.split('-');
    let start = range_it.next().unwrap().parse::<i32>().unwrap();
    let end = range_it.next().unwrap().parse::<i32>().unwrap();

    return RangeInclusive::new(start, end);
}

fn assignment_pair_overlaps(
    first: &RangeInclusive<i32>, second: &RangeInclusive<i32>
) -> bool {
    return RangeDisjoint::compare(&first, &second) == None;
}

fn fully_overlaps_ranges(first: &RangeInclusive<i32>, ranges_iter: Iter<RangeInclusive<i32>>)
    -> bool {
    for range in ranges_iter {
        if RangeDisjoint::compare(&first, &range) == None { return true; }
    }

    return false;
}
