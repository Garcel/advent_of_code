#[derive(Eq, Hash, PartialEq, Debug)]
enum Play {
    ROCK,
    SCISSORS,
    PAPER
}

#[derive(Eq, Hash, PartialEq, Debug)]
enum PlayResultEnum {
    LOST,
    DRAW,
    WIN
}

pub fn resolve(input: &&str) -> i32 {
    return rounds_scores(input);
}

fn rounds_scores(input: &&str) -> i32 {
    return input
        .lines()
        .map(|round| round_score(&round))
        .collect::<Vec<i32>>()
        .iter()
        .sum::<i32>();
}

fn round_score(round: &&str) -> i32 {
    let mut play = round.split_whitespace();
    let p1_play = match_play(play.next().unwrap().chars().next().unwrap()); // oh well
    let p2_play = match_play(play.next().unwrap().chars().next().unwrap());

    return shape_score(&p2_play) + play_score(&p1_play, &p2_play);
}

fn match_play(election: char) -> Play {
    return match election {
        'A' => Play::ROCK,
        'B' => Play::PAPER,
        'C' => Play::SCISSORS,
        'X' => Play::ROCK,
        'Y' => Play::PAPER,
        'Z' => Play::SCISSORS,
        _ => unreachable!()
    }
}

fn shape_score(play: &Play) -> i32 {
    return match play {
        Play::ROCK => 1,
        Play::PAPER => 2,
        Play::SCISSORS => 3
    }
}

fn play_score(p1_play: &Play, p2_play: &Play) -> i32 {
    let play_result = play_result(p1_play, p2_play);
    return match play_result {
        PlayResultEnum::LOST => 0,
        PlayResultEnum::DRAW => 3,
        PlayResultEnum::WIN => 6
    }
}

fn play_result(p1_play: &Play, p2_play: &Play) -> PlayResultEnum {
    if p1_play == p2_play { return PlayResultEnum::DRAW; }
    else if p2_play == &Play::ROCK && p1_play != &Play::PAPER { return PlayResultEnum::WIN; }
    else if p2_play == &Play::PAPER && p1_play != &Play::SCISSORS { return PlayResultEnum::WIN; }
    else if p2_play == &Play::SCISSORS && p1_play != &Play::ROCK { return PlayResultEnum::WIN; }
    else { return PlayResultEnum::LOST; }
}
