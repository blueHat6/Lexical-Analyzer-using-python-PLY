# Lexical Analyzer for an R-script-like Language  

This repository contains the implementation of a **Lexical Analyzer** for a custom programming language inspired by R-script. The analyzer processes source code and tokenizes its components, such as keywords, identifiers, literals, operators, and delimiters.  

## Features  
The Lexical Analyzer is designed to handle the following constructs:  
1. **Simple Statements**  
   - Basic operations such as variable assignments (`x <- 5`) or function calls (`print(x)`).  
2. **Simple Arithmetic Expressions**  
   - Arithmetic operations like addition, subtraction, multiplication, and division (`x + y * z`).  
3. **Simple Conditional IF with Block**  
   - Conditional statements with a block of instructions:
     ```r
     if (x > 0) {
         print("Positive")
     }
     ```  
4. **Simple Looping with Conditional IF Block**  
   - Loop constructs with embedded conditional blocks:
     ```r
     for (i in 1:10) {
         if (i %% 2 == 0) {
             print(i)
         }
     }
     ```  

## How It Works  
1. **Input Source Code**  
   - The analyzer reads source code written in the R-script-like syntax.  
2. **Tokenization**  
   - Scans the input and converts it into tokens representing keywords, variables, operators, etc.  
3. **Error Handling**  
   - Detects and reports unrecognized or invalid tokens with detailed error messages.  

## Usage  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/lexical-analyzer-r-script-like.git
