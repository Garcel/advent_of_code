use crate::puzzle_part_one;
use crate::puzzle_part_two;

#[test]
fn test_part_one_demo() {
    let input = include_str!("../input/demo.txt");
    assert_eq!(puzzle_part_one::resolve(&input), 15);
}

#[test]
fn test_part_one() {
    let input = include_str!("../input/puzzle.txt");
    assert_eq!(puzzle_part_one::resolve(&input), 14531);
}

#[test]
fn test_part_two_demo() {
    let input = include_str!("../input/demo.txt");
    assert_eq!(puzzle_part_two::resolve(&input), 12);
}

#[test]
fn test_part_two() {
    let input = include_str!("../input/puzzle.txt");
    assert_eq!(puzzle_part_two::resolve(&input), 11258);
}
