# Command Line-Based Password Generator

## Overview
This python application allows users to generate secure passwords by specifying the desired length. The generated passwords are a mix of letters, digits, and special characters, ensuring robust security.

## Features
- **Customizable Length** : Users can specify the length of the password .
- **High Security** : Combines uppercase and lowercase letters, digits, and special characters.
- **Command Line Interface** : Easy to use via the command line.

Usage
1. Run the password generator script .
2. Enter the desired password  length when prompted.
3. Receive your generated passward.

How It Works
- random.sample(): Ensures a random selection of characters without repetition.
- string.punctuation: Provides a set of special characters.
- string.ascii_letters: Provides a set of uppercase and lowercase letters.
- string.digits: Provides a set of digits.
  
