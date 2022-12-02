use std::env;

mod puzzle;

pub fn main() {
    let args: Vec<String> = env::args().collect();

    let input: &str = &args[1];

    println!(
        "{}",
        puzzle::part_one(&input)
    );

    println!(
        "{}",
        puzzle::part_two(&input)
    );
}

#[cfg(test)]
mod tests;
