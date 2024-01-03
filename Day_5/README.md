# Password Generator Project in Python

## Introduction
Are you having difficulty creating a truly strong password? Don't worry anymore, this program will help you create a secure password.

## Usage
To use the Password Generator, run the script in a Python environment. The program will prompt you to provide the following information:

- Number of letters you want in your password.
- Number of symbols you want in your password.
- Number of numbers you want in your password.

Once you input these values, the program will generate and display a random password that meets your criteria.

## Code Explanation
The code utilizes lists of letters, numbers, and symbols to create a pool of characters for password generation. The `random.choice()` function is used to randomly select characters from these lists, and the password is constructed by appending the chosen characters to a password list.

After constructing the password list, the `random.shuffle()` function is used to shuffle the characters randomly, providing an additional layer of security. Finally, the shuffled characters are concatenated into a string to form the final password, which is then displayed to the user.

## How to use?
1. Clone the repository:

   ```bash
   https://github.com/123porAlan/100_days_of_code.git
2. Go to the Day_5 folder
3. Run the file: python main.py
