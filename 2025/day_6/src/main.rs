mod txt_reader;
use txt_reader::txt_reader;

fn transpose_i64(matrix: &Vec<Vec<i64>>) -> Vec<Vec<i64>> {
    (0..matrix[0].len())
        .map(|c| matrix.iter().map(|row| row[c]).collect())
        .collect()
}

fn part_1(mut input: Vec<String>) -> i64 {
    let operators: Vec<String> = input
        .pop()
        .unwrap()
        .split_whitespace()
        .map(str::to_string)
        .collect();

    let mut number_matrix: Vec<Vec<i64>> = input
        .into_iter()
        .map(|line| {
            line.split_whitespace()
                .map(|s| s.parse::<i64>().unwrap())
                .collect()
        })
        .collect();

    number_matrix = transpose_i64(&number_matrix);

    let mut total: i64 = 0;

    for (i, o) in operators.iter().enumerate() {
        if o == "+" {
            total += number_matrix[i].iter().sum::<i64>()
        } else if o == "*" {
            total += number_matrix[i].iter().product::<i64>()
        }
    }

    total
}

fn transpose_char(matrix: &Vec<Vec<char>>) -> Vec<Vec<char>> {
    (0..matrix[0].len())
        .map(|c| matrix.iter().map(|row| row[c]).collect())
        .collect()
}

fn part_2(input: Vec<String>) -> i64 {
    // pad lines so columns line up
    let width = input.iter().map(|s| s.len()).max().unwrap_or(0);
    let rows = input.len();

    let grid: Vec<Vec<char>> = input
        .iter()
        .map(|line| {
            let mut v: Vec<char> = line.chars().collect();
            v.resize(width, ' ');
            v
        })
        .collect();

    let columns: Vec<Vec<char>> = transpose_char(&grid);

    // split columns into groups separated by all-space columns
    let mut column_groups: Vec<Vec<Vec<char>>> = Vec::new();
    let mut current_group: Vec<Vec<char>> = Vec::new();
    
    for col in columns {
        if col.iter().all(|&ch| ch == ' ') {
            if !current_group.is_empty() {
                column_groups.push(current_group);
                current_group = Vec::new();
            }
        } else {
            current_group.push(col);
        }
    }
    
    if !current_group.is_empty() {
        column_groups.push(current_group);
    }
    
    column_groups.reverse(); // process groups from right to left

    let mut total: i64 = 0;

    for group in &column_groups {
        // get operator from the bottom
        let operator = group
            .iter()
            .filter_map(|col| {
                let ch = col[rows - 1];
                (ch == '+' || ch == '*').then_some(ch)
            })
            .next()
            .unwrap_or('+');

        // extract numbers from each column (ignore operator)
        let numbers: Vec<i64> = group
            .iter()
            .filter_map(|col| {
                let s: String = col[..rows - 1]
                    .iter()
                    .filter(|c| !c.is_whitespace())
                    .collect();

                if s.is_empty() {
                    None
                } else {
                    s.parse::<i64>().ok()
                }
            })
            .collect();

        total += match operator {
            '+' => numbers.iter().sum(),
            '*' => numbers.iter().product(),
            _ => 0
        };
    }

    total
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: total of all operations by column (numerically separated columns)
    println!("Part 1 answer: {}", part_1(lines.clone()));

    // P2: total of all operations by column (separated be character columns)
    println!("Part 2 answer: {}", part_2(lines.clone()));
}
