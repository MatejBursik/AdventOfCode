mod txt_reader;
mod functions;

use txt_reader::txt_reader;
use functions::*;

fn dfs(grid: &mut Vec<Vec<bool>>, shapes: &Vec<Vec<Vec<Vec<char>>>>, idx: usize) -> bool {
    if idx == shapes.len() {
        return true;
    }

    // Prune if not enough empty cells left
    let empty = grid.iter().flatten().filter(|&&c| !c).count() as i32;
    let needed = remaining_area(shapes, idx);

    if needed > empty {
        return false;
    }

    let h = grid.len();
    let w = grid[0].len();

    for rot in &shapes[idx] {
        let sh = rot.len();
        let sw = rot[0].len();

        for y in 0..h - sh {
            for x in 0..w - sw {
                if can_place(grid, rot, x, y) {
                    set_shape(grid, rot, x, y, true);

                    if dfs(grid, shapes, idx + 1) {
                        return true;
                    }

                    set_shape(grid, rot, x, y, false);
                }
            }
        }
    }

    false
}

fn part_1(input: Vec<String>) -> i32 {
    let (presents, regions) = parse_input(&input);
    let mut count = 0;

    for region in regions {
        let mut expanded = Vec::new();

        for (id, num) in region.presents_required.iter().enumerate() {
            for _ in 0..*num {
                expanded.push(id as i32);
            }
        }

        // Sort by descending area
        expanded.sort_by_key(|id| {
            -(presents[id]
                .iter()
                .flatten()
                .filter(|&&c| c == '#')
                .count() as i32)
        });

        let mut grid = vec![vec![false; region.width]; region.height];
        let shapes = expanded.iter().map(|id| rotations(&presents[id])).collect();

        if dfs(&mut grid, &shapes, 0) {
            count += 1;
        }
    }
    

    count
}

fn part_2(input: Vec<String>) -> i32 {
    0
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: Count how many of the regions can fit all of the presents listed
    println!("Part 1 answer: {}", part_1(lines.clone()));

    // P2:
    println!("Part 2 answer: {}", part_2(lines.clone()));
}
