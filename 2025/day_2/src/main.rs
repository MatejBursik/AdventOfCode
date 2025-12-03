mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i64 {
    let mut result: i64 = 0;
    let line = &input[0];
    
    for pair in line.split(',') {
        let parts: Vec<&str> = pair.split('-').collect();

        let start: i64 = parts[0].parse().unwrap();
        let end: i64 = parts[1].parse().unwrap();

        for num in start..end + 1 {
            let num_str = num.to_string();

            // if even
            if num_str.len() % 2 == 0 {
                // if halves equal
                if num_str[0..num_str.len()/2] == num_str[num_str.len()/2..] {
                    result += num;
                }
            }
        }
    }

    result
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut result: i64 = 0;
    let line = &input[0];
    
    for pair in line.split(',') {
        let parts: Vec<&str> = pair.split('-').collect();

        let start: i64 = parts[0].parse().unwrap();
        let end: i64 = parts[1].parse().unwrap();

        for num in start..end + 1 {
            let num_str = num.to_string();
            let mut pattern: String = "".to_string();

            for i in 1..(num_str.len() / 2) + 1 {
                pattern.push_str(&num_str[i - 1..i]);

                // if not divisible by pattern, skip
                if num_str.len() % i == 0 {
                    // if pattern repeats
                    if num_str == pattern.repeat(num_str.len() / i) {
                        result += num;
                        break;
                    }
                }
            }
        }
    }

    result
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: add up all of the invalid IDs
    // ID is invalid if its halves (by characters) are the same
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: add up all of the invalid IDs
    // ID is invalid if it has a repeating pattern
    println!("Part 2 answer: {}", part_2(&lines));
}
