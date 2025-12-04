mod txt_reader;
use txt_reader::txt_reader;

fn check_8_direct_pos(diagram: &Vec<Vec<char>>, x: i32, y: i32, height: i32, width: i32) -> bool{
    let directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)];
    let mut count = 0;
    let mut nx: i32;
    let mut ny: i32;

    for (d_x, d_y) in directions {
        nx = x + d_x;
        ny = y + d_y;

        if nx >= 0 && ny >= 0 && nx < height && ny < width {
            if diagram[ny as usize][nx as usize] == '@' {
                count += 1;
            }
        }
    }

    count < 4
}

fn part_1(input: &Vec<String>) -> i32 {
    let mut count = 0;
    let mut diagram: Vec<Vec<char>> = Vec::new();

    for line in input {
        diagram.push(line.chars().collect());
    }

    let h = diagram.len() as i32;
    let w = diagram[0].len() as i32;

    for y in 0..h {
        for x in 0..w {
            if diagram[y as usize][x as usize] == '@' {
                if check_8_direct_pos(&diagram, x, y, h, w) {
                    count += 1;
                }
            }
        }
    }
    
    count
}

fn count_removed(diagram: &Vec<Vec<char>>) -> i32 {
    diagram.iter()
        .flat_map(|line| line.iter())
        .filter(|&&c| c == 'X')
        .count() as i32
}

fn part_2(input: &Vec<String>) -> i32 {
    let mut diagram: Vec<Vec<char>> = Vec::new();

    for line in input {
        diagram.push(line.chars().collect());
    }

    let h = diagram.len() as i32;
    let w = diagram[0].len() as i32;
    let mut run = true;

    while run {
        run = false;

        for y in 0..h {
            for x in 0..w {
                if diagram[y as usize][x as usize] == '@' {
                    if check_8_direct_pos(&diagram, x, y, h, w) {
                        // marked as removed
                        diagram[y as usize][x as usize] = 'X';
                        run = true;
                    }
                }
            }
        }
    }

    count_removed(&diagram)
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: count paper rolls that can be accessed by forklift
    //  (can be accessed if there are fewer than four paper rolls in the eight adjacent positions)
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: count paper rolls that can be removed
    //  (if accessible remove it, and repeat until non removed)
    println!("Part 2 answer: {}", part_2(&lines));
}
