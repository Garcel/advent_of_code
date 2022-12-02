mod puzzle;

const ITERATIONS: u64 = 100;

pub fn main() {
    let input = include_str!("../input/puzzle.txt");

    bench_part_one(&input);
    bench_part_two(&input);
}

fn bench_part_one(input: &&str) {
    let time = bench(&puzzle::part_one, &input);
    println!("Part One took {:.3} milliseconds.", time);
}

fn bench_part_two(input: &&str) {
    let time = bench(&puzzle::part_two, &input);
    println!("Part Two took {:.3} milliseconds.", time);
}

fn bench(f: &dyn Fn(&&str) -> i32, input: &&str) -> f64 {
    let now = std::time::Instant::now();

    for _ in 0..ITERATIONS {
        f(input);
    }

    return now.elapsed().as_millis() as f64 / ITERATIONS as f64;
}
