use std::collections::HashMap;

#[derive(Debug)]
pub struct Region {
    pub width: usize,
    pub height: usize,
    pub presents_required: Vec<usize> // idx = Present id, num = count
}

pub fn parse_input(input: &Vec<String>) -> (HashMap<i32, Vec<Vec<char>>>, Vec<Region>) {
    let mut presents: HashMap<i32, Vec<Vec<char>>> = HashMap::new();
    let mut regions: Vec<Region> = Vec::new();
    let mut i: usize = 0;

    while i < input.len() {
        if input[i].contains(':') && input[i].contains('x') {
            // Add a Region
            let (left, right) = input[i].split_once(':').unwrap();
            let (w, h) = left.split_once('x').unwrap();

            regions.push(
                Region {
                    width: w.parse().unwrap(),
                    height: h.parse().unwrap(),
                    presents_required: right.split(' ').skip(1).map(|x| x.parse().unwrap()).collect()
                }
            );

            i += 1;

        } else if input[i].contains(':') && !input[i].contains('x') {
            // Add a Present
            presents.insert(
                input[i][..input[i].len() - 1].parse::<i32>().unwrap(),
                vec![
                    input[i + 1].chars().collect(),
                    input[i + 2].chars().collect(),
                    input[i + 3].chars().collect()
                ]
            );
            
            i += 4;

        } else {
            // Empty
            i += 1;
        }
    }

    (presents, regions)
}

pub fn rotate(shape: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    // Rotate the shape
    let h = shape.len();
    let w = shape[0].len();
    let mut r = vec![vec!['.'; h]; w];

    for y in 0..h {
        for x in 0..w {
            r[x][h - 1 - y] = shape[y][x];
        }
    }
    
    r
}

pub fn rotations(shape: &Vec<Vec<char>>) -> Vec<Vec<Vec<char>>> {
    // Generate unique rotations
    let mut result = Vec::new();
    let mut current = shape.clone();

    for _ in 0..4 {
        if !result.contains(&current) {
            result.push(current.clone());
        }
        current = rotate(&current);
    }

    result
}

pub fn can_place(grid: &Vec<Vec<bool>>, shape: &Vec<Vec<char>>, x: usize, y: usize) -> bool {
    // Check placement validity
    for dy in 0..shape.len() {
        for dx in 0..shape[0].len() {
            if shape[dy][dx] == '#' && grid[y + dy][x + dx] {
                return false;
            }
        }
    }

    true
}

pub fn set_shape(
    // Place or Remove shape
    grid: &mut Vec<Vec<bool>>, shape: &Vec<Vec<char>>, x: usize, y: usize, value: bool) {
    
    for dy in 0..shape.len() {
        for dx in 0..shape[0].len() {
            if shape[dy][dx] == '#' {
                grid[y + dy][x + dx] = value;
            }
        }
    }
}

pub fn remaining_area(shapes: &Vec<Vec<Vec<Vec<char>>>>, idx: usize) -> i32 {
    // Sum all needed area for remaining shapes
    shapes[idx..]
        .iter()
        .map(|r| {
            r[0]
                .iter()
                .flatten()
                .filter(|&&c| c == '#')
                .count() as i32
        })
        .sum()
}
