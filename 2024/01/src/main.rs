use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn read_file(path: &str) -> Vec<String> {
    let mut data: Vec<String> = vec![];
    match File::open(path) {
        Ok(file) => {
            let reader = io::BufReader::new(file);
            for line in reader.lines() {
                match line {
                    Ok(content) => {
                        data.push(content);
                    },
                    Err(e) => eprintln!("Error reading line: {}", e)
                }
            }
        }
        Err(e) => eprintln!("Error opening file: {}", e)
    }

    return data;
}

fn total_distance(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    // Sort both lists
    let mut left_sorted = left.clone();
    let mut right_sorted = right.clone();
    left_sorted.sort();
    right_sorted.sort();

    // Calculate the total distance
    return left_sorted.iter()
        .zip(right_sorted.iter())
        .map(|(l, r)| (l - r).abs())
        .sum();
}

fn similarity_score(left: &Vec<i32>, right: &Vec<i32>) -> i32 {
    // Count occurrences of each number in the right list
    let mut right_count = HashMap::new();
    for num in right {
        *right_count.entry(num).or_insert(0) += 1;
    }

    // Calculate the similarity score
    let mut similarity_score = 0;
    for num in left {
        if let Some(&count) = right_count.get(&num) {
            similarity_score += num * count;
        }
    }

    return similarity_score;
}

fn main() {
    let data = read_file("input.txt");
    let mut left: Vec<i32> = vec![];
    let mut right: Vec<i32> = vec![];

    for line in data {
        let lr: Vec<&str> = line.split_whitespace().collect();
        left.push(lr[0].parse::<i32>().unwrap());
        right.push(lr[1].parse::<i32>().unwrap());
    }

    let total_distance = total_distance(&left, &right);
    let similarity_score = similarity_score(&left, &right);

    println!("Total distance: {}", total_distance);
    println!("Similarity score: {}", similarity_score);
}
