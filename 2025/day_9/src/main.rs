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

fn point_in_polygon(point: (i64, i64), polygon: &Vec<(i64, i64)>) -> bool {    
    let (px, py) = point;
    let n = polygon.len();
    let mut inside = false;
    
    // Iterate through each edge of the polygon
    for i in 0..n {
        let (x1, y1) = polygon[i];
        let (x2, y2) = polygon[(i + 1) % n];
        
        // Check if the horizontal ray intersects with this edge
        if (y1 > py) != (y2 > py) {
            let x_intersection = x1 + (py - y1) * (x2 - x1) / (y2 - y1);
            
            // If the intersection is to the right of the point, toggle inside/outside
            if px < x_intersection {
                inside = !inside; // FIX: I dont know about this
            }
        }
    }
    
    inside
}

fn bresenham_line(x0: i64, y0: i64, x1: i64, y1: i64) -> Vec<(i64, i64)> {
    let mut points = Vec::new();

    let dx = (x1 - x0).abs();
    let dy = -(y1 - y0).abs();
    let sx = if x0 < x1 { 1 } else { -1 };
    let sy = if y0 < y1 { 1 } else { -1 };
    let mut err = dx + dy;

    let mut x = x0;
    let mut y = y0;

    loop {
        points.push((x, y));

        if x == x1 && y == y1 { break; }

        let e2 = 2 * err;
        if e2 >= dy {
            err += dy;
            x += sx;
        }

        if e2 <= dx {
            err += dx;
            y += sy;
        }
    }

    points
}

fn fill_in_polygon(points: &Vec<(i64, i64)>) -> Vec<(i64, i64)> {
    let mut collection: Vec<(i64, i64)> = Vec::new();
    
    for i in 0..points.len() {
        let start = points[i];
        let end = points[(i + 1) % points.len()]; // wrap around to first point
        let line_points = bresenham_line(start.0, start.1, end.0, end.1);
        collection.extend(line_points);
    }

    collection.dedup();
    collection
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut area: i64 = 0;
    let mut tiles: Vec<(i64, i64)> = Vec::new();
    
    for line in input {
        let (a, b) = line.split_once(',').unwrap();
        tiles.push((a.parse::<i64>().unwrap(), b.parse::<i64>().unwrap()));
    }

    let polygon = fill_in_polygon(&tiles);

    for (x_1, y_1) in &tiles {
        for (x_2, y_2) in &tiles {
            // Skip if area is smaller, not worth calculating
            let dx = (x_1 - x_2 + 1).abs();
            let dy = (y_1 - y_2 + 1).abs();

            if !(dx * dy > area) {
                continue;
            }

            let rect_point = vec![
                (*x_1, *y_1),
                (*x_1, *y_2),
                (*x_2, *y_1),
                (*x_2, *y_2)
            ];
            
            let mut all_inside = true;
            
            // Check if rectangle is inside the polygon
            for (x, y) in rect_point {
                if !point_in_polygon((x, y), &polygon) { // FIX: point_in_polygon
                    all_inside = false;
                    break;
                }
            }

            if all_inside {
                if dx * dy > area {
                    area = dx * dy;
                }
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

    // P2: largest area between any two red tiles inside the polygon, 4521497579 too high
    println!("Part 2 answer: {}", part_2(&lines));
}
