use std::collections::HashSet;
use std::collections::HashMap;

mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i32 {
    let mut total = 0;
    let mut old_beams: HashSet<usize> = HashSet::new();
    let mut new_beams: HashSet<usize> = HashSet::new();

    for line in input {
        if line == &".".repeat(input[0].len()) {
            continue;
        }

        for (i, b) in line.chars().enumerate() {
            if b == 'S' {
                new_beams.insert(i);
            } else if b == '^' && old_beams.contains(&i) {
                new_beams.insert(i - 1);
                new_beams.insert(i + 1);
                total += 1;
            } else if b == '.' && old_beams.contains(&i) {
                new_beams.insert(i);
            }
        }

        old_beams = new_beams.clone();
        new_beams.clear();
    }

    total
}

fn count_timelines(input: &Vec<String>, row: usize, col: usize, cache: &mut HashMap<(usize, usize), i64>) -> i64 {
        // reached bottom
        if row >= input.len() {
            return 1;
        }
        
        // check cache
        if let Some(&count) = cache.get(&(row, col)) {
            return count;
        }
        
        let b = input[row].chars().nth(col).unwrap();
        
        let result = match b {
            '.' | '|' | 'S' => {
                // down
                if row + 1 < input.len() {
                    count_timelines(input, row + 1, col, cache)
                } else {
                    1
                }
            },

            '^' => {
                let mut total: i64 = 0;
                
                // left
                if col > 0 && row + 1 < input.len() {
                    total += count_timelines(input, row + 1, col - 1, cache);
                } else if col > 0 {
                    total += 1;
                }
                
                // right
                if col + 1 < input[row].len() && row + 1 < input.len() {
                    total += count_timelines(input, row + 1, col + 1, cache);
                } else if col + 1 < input[row].len() {
                    total += 1;
                }
                
                total
            },

            _ => 0
        };
        
        cache.insert((row, col), result);
        
        result
    }

fn part_2(input: &Vec<String>) -> i64 {
    let mut cache = HashMap::new();
    let mut start = 0;

    for (i, ch) in input[0].chars().enumerate() {
        if ch == 'S' {
            start = i;
            break;
        }
    }
    
    // DFS recursion
    count_timelines(input, 0, start, &mut cache)
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: count number of splits
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: count numebr of timelines
    println!("Part 2 answer: {}", part_2(&lines));
}
