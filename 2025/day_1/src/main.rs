mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i32 {
    let mut pos = 50;
    let mut count = 0;
    
    for line in input {
        let direction = line.chars().next().unwrap();
        let distance: i32 = line[1..].parse().unwrap();
        
        // Calculate new position
        pos = match direction {
            'L' => {
                (((pos - distance) % 100) + 100) % 100
            },

            'R' => {
                (pos + distance) % 100
            },

            _ => panic!("Invalid direction")
        };
        
        if pos == 0 {
            count += 1;
        }
    }
    
    count
}

fn part_2(input: &Vec<String>) -> i32 {
    let mut pos = 50;
    let mut count = 0;
    
    for line in input {
        let direction = line.chars().next().unwrap();
        let distance: i32 = line[1..].parse().unwrap();
        
        // Count each click separately
        for _ in 0..distance {
            pos = match direction {
                'L' => {
                    if pos == 0 {
                        99
                    } else {
                        pos - 1
                    }
                }

                'R' => {
                    if pos == 99 {
                        0
                    } else {
                        pos + 1
                    }
                }

                _ => panic!("Invalid direction")
            };
            
            if pos == 0 {
                count += 1;
            }
        }
    }
    
    count
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1 count how many times dail lands on 0    
    println!("Part 1 answer: {}", part_1(&lines));

    // P2 count how many times dail lands or passes 0
    println!("Part 2 answer: {}", part_2(&lines));
}
