use itertools::Itertools;

pub fn resolve(input: &&str) -> i32 {
    return rucksacks_priorities(input);
}

fn rucksacks_priorities(input: &&str) -> i32 {
    return input
        .lines()
        .collect::<Vec<&str>>()
        .chunks(6)
        .map(|rucksacks_chunk| elves_group_rucksacks_priority(rucksacks_chunk)) // 6 lines
        .sum::<i32>();
}

fn elves_group_rucksacks_priority(rucksacks_chunk: &[&str]) -> i32 {
    return rucksacks_chunk
        .iter()
        .collect::<Vec<&&str>>()
        .chunks(3)
        .map(|rucksack_chunk| rucksack_badge_priority(rucksack_chunk)) // 3 lines
        .sum::<i32>();
}

fn rucksack_badge_priority(rucksack_chunk:&[&&str]) -> i32 {
    let (first, second, third) = rucksack_chunk.iter().collect_tuple().unwrap();
    let badge = common_item(first, second, third);

    return priority(badge);
}

fn common_item(first: &str, second: &str, third: &str) -> char {
    for c in first.chars() {
        if second.contains(c) && third.contains(c) { return c; }
    }

    unreachable!();
}

fn priority(item: char) -> i32 {
    let ascii_value = item.to_lowercase().next().unwrap() as i32;
    let priority = ascii_value - 96;

    return if item.is_uppercase() { priority + 26 } else { priority };
}
