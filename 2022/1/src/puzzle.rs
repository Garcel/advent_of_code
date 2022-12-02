pub fn part_one(input: &&str) -> i32 {
    return count_elves_calories(input)
        .iter()
        .copied()
        .max() // find the calories for the elf carrying the most calories
        .unwrap();
}

pub fn part_two(input: &&str) -> i32 {
    let mut elves_calories = count_elves_calories(input);
    elves_calories.sort_by(|a, b| b.cmp(a));

    return elves_calories
        .drain(0..3) // find the calories for the TOP 3 elves carrying the most calories
        .collect::<Vec<i32>>()
        .iter()
        .sum::<i32>();
}

fn count_elves_calories(input: &&str) -> Vec<i32> {
    return input
        .lines()
        .map(|l| { // parse lines to i32. Blank lines are mapped to 0
            return match l.parse::<i32>() {
                Ok(n) => n,
                Err(_) => 0
            }
        })
        .collect::<Vec<i32>>()
        .iter()
        .fold(Vec::new(), |mut acc, x| { // split into partitions. One for each elf
            if *x == 0 || acc.is_empty() {
                acc.push(Vec::new());
            }
            acc.last_mut().unwrap().push(x);
            acc
        })
        .iter()
        .map(|v| v.iter().copied().sum()) // sum each elf calories
        .collect::<Vec<i32>>();
}
