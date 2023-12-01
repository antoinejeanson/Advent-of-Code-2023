use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}

fn part_1() -> i32 {
    let lines = read_lines("input.txt");

    let mut sum = 0;

    for line in &lines {

        let mut numbers = Vec::new();

        // Parse characters
        for character in line.chars() {
            if character.is_numeric() {
                // This is a number
                numbers.push(character);
            }
        }

        // Make a number from the first and last characters

        let mut number_string = String::new();
        number_string.push(numbers[0]);
        number_string.push(numbers[numbers.len() - 1]);

        let number: i32 = number_string.parse().unwrap();
        sum += number
    }

    sum
}


fn part_2() -> i32 {
    let lines = read_lines("input.txt");

    let mut sum = 0;

    let values_to_replace = [["one", "o1e"], ["two", "t2o"], ["three", "t3e"], ["four", "f4r"], ["five", "f5e"], ["six", "s6x"], ["seven", "s7n"], ["eight", "e8t"], ["nine", "n9e"]];

    for line in &lines {
        let mut line_replaced = String::from(line);
        println!("{}", line_replaced);
        for v in values_to_replace {
            line_replaced = line_replaced.replace(v[0], v[1]);
            println!("{}", line_replaced);
        }

        let mut numbers = Vec::new();

        // Parse characters
        for character in line_replaced.chars() {
            if character.is_numeric() {
                // This is a number
                numbers.push(character);
                println!("{}", character);
            }
        }

        

        // Make a number from the first and last characters

        let mut number_string = String::new();
        number_string.push(numbers[0]);
        number_string.push(numbers[numbers.len() - 1]);
        println!("{}", number_string);

        let number: i32 = number_string.parse().unwrap();
        sum += number;

        println!();
    }

    sum
}


fn main() {
    println!("Part 1 sum: {}", part_1());
    println!("Part 2 sum: {}", part_2());
}
