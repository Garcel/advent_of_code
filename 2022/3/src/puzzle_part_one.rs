pub fn resolve(input: &&str) -> i32 {
    return rucksacks_priority(input);
}

fn rucksacks_priority(input: &&str) -> i32 {
    return input
        .lines()
        .map(|rucksack| rucksack_priority(rucksack))
        .sum::<i32>();
}

fn rucksack_priority(rucksack: &str) -> i32 {
    let (first, last) = rucksack.split_at(rucksack.len() / 2);
    let common_item = common_item(first, last);

    return priority(common_item);
}

fn common_item(first: &str, last: &str) -> char {
    for c in first.chars() {
        if last.contains(c) { return c; }
    }

    unreachable!();
}

fn priority(item: char) -> i32 {
    let ascii_value = item.to_lowercase().next().unwrap() as i32;
    let priority = ascii_value - 96; // 96 is difference between ascii and priority for this char

    return if item.is_uppercase() { priority + 26 } else { priority };
}
