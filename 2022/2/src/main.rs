use std::env;

mod puzzle_part_one;
mod puzzle_part_two;

pub fn main() {
    let args: Vec<String> = env::args().collect();

    let input: &str = &args[1];

    println!(
        "{}",
        puzzle_part_one::resolve(&input)
    );

    println!(
        "{}",
        puzzle_part_two::resolve(&input)
    );
}

#[cfg(test)]
mod tests;
