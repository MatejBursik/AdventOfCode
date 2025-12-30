use std::collections::HashSet;
use std::collections::HashMap;

mod txt_reader;
use txt_reader::txt_reader;

fn dfs(node: &str, graph: &HashMap<String, Vec<String>>, visited: &mut HashSet<String>) -> i32 {
    if node == "out" {
        return 1;
    }

    // Prevent looping
    if visited.contains(node) {
        return 0;
    }

    visited.insert(node.to_string());

    let mut total_paths = 0;

    if let Some(neighbors) = graph.get(node) {
        for next in neighbors {
            total_paths += dfs(next, graph, visited);
        }
    }

    visited.remove(node);

    total_paths
}

fn part_1(input: &Vec<String>) -> i32 {
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();

    for line in input {
        let halves: Vec<&str> = line.split(':').collect();

        graph.insert(
            halves[0].to_string(),
            halves[1].split(' ').skip(1).map(|x| x.to_string()).collect()
        );
    }

    let mut visited = HashSet::new();

    // Count paths
    dfs("you", &graph, &mut visited)
}

fn dfs_memo(node: &str, graph: &HashMap<String, Vec<String>>, visited: &mut HashSet<String>, memo: &mut HashMap<(String, bool, bool), i64>, dac: bool, fft: bool) -> i64 {
    let has_dac = dac || node == "dac";
    let has_fft = fft || node == "fft";

    if node == "out" {
        return if has_dac && has_fft { 1 } else { 0 };
    }

    // Cache state (memoization)
    let key = (node.to_string(), has_dac, has_fft);
    if let Some(&cached) = memo.get(&key) {
        return cached;
    }

    // Prevent looping
    if visited.contains(node) {
        return 0;
    }

    visited.insert(node.to_string());

    let mut total = 0;

    if let Some(neighbors) = graph.get(node) {
        for next in neighbors {
            total += dfs_memo(next, graph, visited, memo, has_dac, has_fft);
        }
    }

    visited.remove(node);
    memo.insert(key, total);

    total
}

fn part_2(input: &Vec<String>) -> i64 {
    let mut graph: HashMap<String, Vec<String>> = HashMap::new();

    for line in input {
        let halves: Vec<&str> = line.split(':').collect();

        graph.insert(
            halves[0].to_string(),
            halves[1].split(' ').skip(1).map(|x| x.to_string()).collect()
        );
    }

    let mut visited = HashSet::new();
    let mut memo = HashMap::new();

    // Count paths
    dfs_memo("svr", &graph, &mut visited, &mut memo, false, false)
}

fn main() {
    let input = txt_reader("input.txt");
    let lines: Vec<String> = input.unwrap_or_default();

    // P1: count how many different paths lead from 'you' to 'out'
    println!("Part 1 answer: {}", part_1(&lines));

    // count how many different paths that from 'svr' to 'out' and pass through 'dac' and 'fft'
    println!("Part 2 answer: {}", part_2(&lines));
}
