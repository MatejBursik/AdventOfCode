mod txt_reader;
use txt_reader::txt_reader;

#[derive(Debug, Clone)]
pub struct Box {
    pub id: usize,
    pub x: i32,
    pub y: i32,
    pub z: i32
}

impl Box {
    pub fn new(id: usize, x: i32, y: i32, z: i32) -> Self {
        Self {id, x, y, z}
    }
}

#[derive(Debug, Clone)]
struct Circuit {
    connections: Vec<Box>
}

fn distance(a: &Box, b: &Box) -> f64 {
    let dx = (a.x - b.x) as f64;
    let dy = (a.y - b.y) as f64;
    let dz = (a.z - b.z) as f64;

    (dx * dx + dy * dy + dz * dz).sqrt()
}

fn find_circuit_index(circuits: &Vec<Circuit>, box_id: usize) -> Option<usize> {
    for (i, c) in circuits.iter().enumerate() {
        if c.connections.iter().any(|b| b.id == box_id) {
            return Some(i);
        }
    }

    None
}

fn part_1(input: &Vec<String>) -> i32 {
    let mut boxes: Vec<Box> = Vec::new();

    for (i, line) in input.iter().enumerate() {
        let coords: Vec<i32> = line
            .split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect();

        boxes.push(Box::new(i, coords[0], coords[1], coords[2]));
    }

    // One box per circuit
    let mut circuits: Vec<Circuit> = boxes
        .iter()
        .map(|b| Circuit {connections: vec![b.clone()]})
        .collect();

    // Precompute all pairs
    let mut pairs: Vec<(usize, usize, f64)> = Vec::new();

    for i in 0..boxes.len() {
        for j in (i + 1)..boxes.len() {
            let d = distance(&boxes[i], &boxes[j]);
            pairs.push((i, j, d));
        }
    }

    // Sort by distance
    pairs.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap());

    for k in 0..1000 {
        let (id_1, id_2, _) = pairs[k];

        let c_1 = find_circuit_index(&circuits, id_1).unwrap();
        let c_2 = find_circuit_index(&circuits, id_2).unwrap();

        // If already in same circuit, nothing happens
        if c_1 == c_2 {
            continue;
        }

        // Remove the higher index to avoid shifting issues and merge
        let (low, high) = if c_1 < c_2 {
            (c_1, c_2)
        } else {
            (c_2, c_1)
        };

        let other = circuits.remove(high);
        circuits[low].connections.extend(other.connections);
    }

    circuits.sort_by_key(|c| c.connections.len());
    circuits.reverse();

    (circuits[0].connections.len() * circuits[1].connections.len() * circuits[2].connections.len()) as i32
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut boxes: Vec<Box> = Vec::new();

    for (i, line) in input.iter().enumerate() {
        let coords: Vec<i32> = line
            .split(',')
            .map(|x| x.parse::<i32>().unwrap())
            .collect();

        boxes.push(Box::new(i, coords[0], coords[1], coords[2]));
    }

    // One box per circuit
    let mut circuits: Vec<Circuit> = boxes
        .iter()
        .map(|b| Circuit {connections: vec![b.clone()]})
        .collect();

    // Precompute all pairs
    let mut pairs: Vec<(usize, usize, f64)> = Vec::new();

    for i in 0..boxes.len() {
        for j in (i + 1)..boxes.len() {
            let d = distance(&boxes[i], &boxes[j]);
            pairs.push((i, j, d));
        }
    }

    // Sort by distance
    pairs.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap());

    let mut last_pair = (0usize, 0usize);

    for (id_1, id_2, _) in pairs {
        let c_1 = find_circuit_index(&circuits, id_1).unwrap();
        let c_2 = find_circuit_index(&circuits, id_2).unwrap();

        // If already in same circuit, nothing happens
        if c_1 == c_2 {
            continue;
        }

        // Remove the higher index to avoid shifting issues and merge
        let (low, high) = if c_1 < c_2 {
            (c_1, c_2)
        } else {
            (c_2, c_1)
        };

        let other = circuits.remove(high);
        circuits[low].connections.extend(other.connections);

        last_pair = (id_1, id_2);

        // Stop when fully connected
        if circuits.len() == 1 {
            break;
        }
    }

    boxes[last_pair.0].x as i64 * boxes[last_pair.1].x as i64
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: multiply the length of the three longest circuits
    println!("Part 1 answer: {}", part_1(&lines));

    // P2: multiply the 'x' coordinates of the last pair of unconnected junction boxes
    println!("Part 2 answer: {}", part_2(&lines));
}
