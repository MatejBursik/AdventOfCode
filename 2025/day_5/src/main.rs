mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i64 {
    let mut fresh_ranges: Vec<(i64, i64)> = Vec::new();
    let mut ingredients: Vec<i64> = Vec::new();
    let mut switch = true;

    for line in input {
        if line == "" {
            switch = !switch;
            continue;
        }

        if switch {
            let (a, b) = line.split_once('-').unwrap();
            fresh_ranges.push((a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()));
        } else {
            ingredients.push(line.parse::<i64>().unwrap());
        }
    }

    let mut count = 0;

    for i in ingredients {
        for &(a, b) in &fresh_ranges {
            if i >= a && i <= b {
                count += 1;
                break;
            }
        }
    }

    count
}

fn merge_ranges(mut ranges: Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    ranges.sort_by_key(|r| r.0);

    let mut merged: Vec<(i64, i64)> = Vec::new();

    for (start, end) in ranges {
        if let Some(last) = merged.last_mut() {
            // if overlapping or touching, merge
            if start <= last.1 {
                last.1 = last.1.max(end);
                continue;
            }
        }
        
        merged.push((start, end));
    }

    merged
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut fresh_ranges: Vec<(i64, i64)> = Vec::new();

    for line in input {
        if line == "" { break }

        let (a, b) = line.split_once('-').unwrap();
        fresh_ranges.push((a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()));
    }

    let merged = merge_ranges(fresh_ranges);
    let mut count = 0;

    for (a, b) in merged {
        count += b - a + 1;
    }

    count
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: count fresh available ingredient IDs
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: count all ingredient IDs in the fresh ranges
    println!("Part 2 answer: {}", part_2(&lines));
}
