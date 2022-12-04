use crate::puzzle::*;

#[test]
fn test_part_one_demo() {
    let input = include_str!("../input/demo.txt");
    assert_eq!(part_one(&input), 24000);
}

#[test]
fn test_part_one() {
    let input = include_str!("../input/puzzle.txt");
    assert_eq!(part_one(&input), 68923);
}

#[test]
fn test_part_two_demo() {
    let input = include_str!("../input/demo.txt");
    assert_eq!(part_two(&input), 45000);
}

#[test]
fn test_part_two() {
    let input = include_str!("../input/puzzle.txt");
    assert_eq!(part_two(&input), 200044);
}
