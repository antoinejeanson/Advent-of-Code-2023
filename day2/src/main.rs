use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into a vector
}

fn part_1() {
    let lines = read_lines("input.txt");
    
    for line in lines {

        // Get the game number
        let game_number_str: Vec<&str> = line.split(" ").collect();
        let game_number: i32 = game_number_str[1].replace(":", "").parse().unwrap();
        println!("{}", game_number);

        // Get a vector of draws
        let draws_str: Vec<&str> = line.split(";").collect();
        println!("{:?}", draws_str);
    }   
}

fn main() {
    part_1();
}
