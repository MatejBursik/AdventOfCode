use std::fs::File;
use std::io::{BufRead, BufReader, Result};

pub fn txt_reader(path: &str) -> Result<Vec<String>> {
    let file = File::open(path)?;
    let reader = BufReader::new(file);
    let lines = reader.lines().collect::<Result<Vec<_>>>()?;

    Ok(lines)
}