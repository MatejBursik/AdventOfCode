mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i64 {
    let mut total: i64 = 0;

    for bank in input {
        let mut max_joltage: i64 = 0;
        let chars: Vec<char> = bank.chars().collect();

        for i in 0..chars.len() {
            for j in i + 1..chars.len() {
                let combined: i64 = format!("{}{}", chars[i], chars[j]).parse().unwrap();

                if combined > max_joltage {
                    max_joltage = combined;
                }
            }
        }

        total += max_joltage;
    }

    total
}

fn part_2(input: &Vec<String>) -> i128 {
    let mut total: i128 = 0;
    let k = 12;
    let mut chars: Vec<char>;
    let mut max_joltage;
    let mut start;
    let mut end;
    let mut max_digit;
    let mut max_index;

    for bank in input {
        max_joltage = String::with_capacity(k);
        chars = bank.chars().collect();
        
        start = 0;

        for remaining in (0..k).rev() {
            end = chars.len() - remaining;
            max_digit = '0';
            max_index = start;

            // Find the maximum digit in this range
            for idx in start..end {
                if chars[idx] > max_digit {
                    max_digit = chars[idx];
                    max_index = idx;
                }
            }

            max_joltage.push(max_digit);
            start = max_index + 1;
        }

        total += max_joltage.parse::<i128>().unwrap();
    }

    total
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: sum of the maximum joltage of 2 batteries from each bank
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: sum of the maximum joltage of 12 batteries from each bank
    println!("Part 2 answer: {}", part_2(&lines));
}
