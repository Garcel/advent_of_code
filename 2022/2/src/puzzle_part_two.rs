#[derive(Eq, Hash, PartialEq, Debug, Copy, Clone)]
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
    let expected_play_result = match_expected_play(
        play.next().unwrap().chars().next().unwrap()
    );
    let p2_play = play_for_result(&p1_play, &expected_play_result);

    return shape_score(&p2_play) + play_score(&expected_play_result);
}

fn match_play(election: char) -> Play {
    return match election {
        'A' => Play::ROCK,
        'B' => Play::PAPER,
        'C' => Play::SCISSORS,
        _ => unreachable!()
    }
}

fn match_expected_play(election: char) -> PlayResultEnum {
    return match election {
        'X' => PlayResultEnum::LOST,
        'Y' => PlayResultEnum::DRAW,
        'Z' => PlayResultEnum::WIN,
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

fn play_score(play: &PlayResultEnum) -> i32 {
    return match play {
        PlayResultEnum::LOST => 0,
        PlayResultEnum::DRAW => 3,
        PlayResultEnum::WIN => 6
    }
}

fn play_for_result(p1_play: &Play, play: &PlayResultEnum) -> Play {
    if *play == PlayResultEnum::DRAW { return *p1_play; }
    else if *play == PlayResultEnum::WIN {
        return match p1_play {
            Play::ROCK => Play::PAPER,
            Play::PAPER => Play::SCISSORS,
            Play::SCISSORS => Play::ROCK
        }
    } else {
        return match p1_play {
            Play::ROCK => Play::SCISSORS,
            Play::PAPER => Play::ROCK,
            Play::SCISSORS => Play::PAPER
        }
    }
}
