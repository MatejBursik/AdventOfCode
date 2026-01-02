mod txt_reader;
use txt_reader::txt_reader;

fn part_1(input: &Vec<String>) -> i64 {
    let mut area: i64 = 0;
    let mut tiles: Vec<(i64, i64)> = Vec::new();
    
    for line in input {
        let (a, b) = line.split_once(',').unwrap();
        tiles.push((a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()));
    }

    for (x_1, y_1) in &tiles {
        for (x_2, y_2) in &tiles {
            let dx = (x_1 - x_2 + 1).abs();
            let dy = (y_1 - y_2 + 1).abs();

            if dx * dy > area {
                area = dx * dy;
            }
        }
    }

    area
}

fn is_point_inside_polygon(point: (i64, i64), polygon: &[(i64, i64)]) -> bool {
    let (x, y) = point;
    let mut inside = false;

    for i in 0..polygon.len() {
        let (x1, y1) = polygon[i];
        let (x2, y2) = polygon[(i + 1) % polygon.len()];

        if ((y1 > y) != (y2 > y)) && (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1) {
            inside = !inside;
        }
    }

    inside
}

fn is_on_polygon_edge(point: (i64, i64), polygon: &[(i64, i64)]) -> bool {
    let (px, py) = point;
    
    for i in 0..polygon.len() {
        let (x1, y1) = polygon[i];
        let (x2, y2) = polygon[(i + 1) % polygon.len()];
        
        // Check if point is on this edge
        if x1 == x2 && px == x1 {
            if py >= y1.min(y2) && py <= y1.max(y2) {
                return true;
            }

        } else if y1 == y2 && py == y1 {
            if px >= x1.min(x2) && px <= x1.max(x2) {
                return true;
            }
        }
    }
    
    false
}

fn is_tile_valid(point: (i64, i64), polygon: &[(i64, i64)]) -> bool {
    is_on_polygon_edge(point, polygon) || is_point_inside_polygon(point, polygon)
}

fn is_rectangle_valid(min_x: i64, max_x: i64, min_y: i64, max_y: i64, polygon: &[(i64, i64)]) -> bool {
    // Check all four corners
    if !is_tile_valid((min_x, min_y), polygon) { return false; }
    if !is_tile_valid((max_x, min_y), polygon) { return false; }
    if !is_tile_valid((min_x, max_y), polygon) { return false; }
    if !is_tile_valid((max_x, max_y), polygon) { return false; }
    
    // Check all edges of the rectangle
    // - Top and Bottom edges
    for x in min_x..=max_x {
        if !is_tile_valid((x, min_y), polygon) { return false; }
        if !is_tile_valid((x, max_y), polygon) { return false; }
    }
    
    // - Left and Right edges
    for y in min_y..=max_y {
        if !is_tile_valid((min_x, y), polygon) { return false; }
        if !is_tile_valid((max_x, y), polygon) { return false; }
    }
    
    // Sample interior points to verify they are all inside
    let sample_step = ((max_x - min_x).max(max_y - min_y) / 20).max(1);
    
    let mut y = min_y + 1;
    while y < max_y {
        let mut x = min_x + 1;
        while x < max_x {
            if !is_tile_valid((x, y), polygon) {
                return false;
            }
            x += sample_step;
        }
        y += sample_step;
    }
    
    true
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut area: i64 = 0;
    let mut red_tiles: Vec<(i64, i64)> = Vec::new();

    for line in input {
        let (a, b) = line.split_once(',').unwrap();
        red_tiles.push((a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()));
    }

    for i in 0..red_tiles.len() {
        for j in i + 1..red_tiles.len() {
            let (x1, y1) = red_tiles[i];
            let (x2, y2) = red_tiles[j];

            let min_x = x1.min(x2);
            let max_x = x1.max(x2);
            let min_y = y1.min(y2);
            let max_y = y1.max(y2);

            let current_area = (max_x - min_x + 1) * (max_y - min_y + 1);
            
            // Skip validity check if the new area is not larger than the current highest area 
            if current_area <= area {
                continue;
            }

            // Check if rectangle is valid
            if is_rectangle_valid(min_x, max_x, min_y, max_y, &red_tiles) {
                area = current_area;
            }
        }
    }

    area
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: largest area between any two red tiles
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: largest area between any two red tiles inside the polygon
    println!("Part 2 answer: {}", part_2(&lines));
}
