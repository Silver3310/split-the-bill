# Documentation for `split_the_bill.py`

The `split_the_bill.py` script is designed to process and analyze financial transactions between a group of members to determine how much each person owes or is owed after various expenses. The script processes a text file containing the entries of expenses shared among members, and it outputs a detailed report of all transactions and final balances.

## Table of Contents

1. [Overview](#overview)
2. [Functions Description](#functions-description)
    - [show_input_data](#show_input-data)
    - [parse_input_data](#parse_input-data)
    - [calculate_debts](#calculate_debts)
    - [summarize_debts](#summarize_debts)
    - [redistribute_debts](#redistribute_debts)
3. [Usage](#usage)
4. [Example](#example)

## Overview

This script defines several functions to handle different parts of the bill splitting process, including reading and parsing data, calculating debts, and redistributing balances to simplify debt settlement. The main part of the script orchestrates the calling of these functions using an input file named `input.txt` and outputs the results into a file named `report.txt`.

## Functions Description

### `show_input_data`

- **Purpose**: Displays the content of the input file.
- **Parameters**:
  - `input_text`: A file object for reading input data.
  - `output_text`: A file object for writing the output.
- **Outputs**: Writes the content of the input file to the output file.

### `parse_input_data`

- **Purpose**: Parses the input data to construct a structured dictionary reflecting each member's payments and the corresponding debtors.
- **Parameters**:
  - `input_text`: A file object for reading input data.
- **Returns**: A dictionary mapping each member to their respective payments and debtors.

### `calculate_debts`

- **Purpose**: Calculates the debts based on the structured data obtained from parsing.
- **Parameters**:
  - `members_data_dict`: A dictionary containing structured member data.
  - `output_text`: A file object for writing the output.
- **Returns**: A dictionary of members along with their respective positive and negative balances.

### `summarize_debts`

- **Purpose**: Summarizes the total amount each member owes or is owed.
- **Parameters**:
  - `members_debts_dict`: A dictionary containing each member's debts.
  - `output_text`: A file object for writing the output.
- **Returns**: Two dictionaries: one for members who need to pay and another for members who need to receive money.

### `redistribute_debts`

- **Purpose**: Simplifies the process of settling debts by redistributing the amounts between payers and receivers.
- **Parameters**:
  - `senders_dict`: Dictionary of members who owe money.
  - `receivers_dict`: Dictionary of members who are owed money.
  - `output_text`: A file object for writing the output.

## Usage

1. Ensure the `input.txt` file is in the same directory as the script and is formatted correctly.
2. Run the script. It will read `input.txt`, process the data, and write the results to `report.txt`.

## Example

**Input (`input.txt`):**

```
АлексейЕ
300, Илья, Вадим
АлексейТ
200, Илья
```

**Output (`report.txt`):**

```
----------ВХОДНЫЕ ДАННЫЕ----------
АлексейЕ
300, Илья, Вадим
АлексейТ
200, Илья
----------------------------------

------РАСПРЕДЕЛЕНИЕ ДОЛГОВ--------
АлексейЕ:
Счёт #1: АлексейЕ заплатил 300 за Илья, Вадим
Всего АлексейЕ заплатил 300
...
```

This script is invaluable for groups sharing expenses, ensuring transparency and simplicity in managing shared financial responsibilities.
