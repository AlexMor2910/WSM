# WSMVideogameClassifier

This project provides a command-line tool to evaluate and score video games based on a predefined classification of play personalities using a custom Weighted Sum Model (WSM). It reads Excel files with training and evaluation data, computes frequency-based weights, applies them to score each game, and outputs the results in a readable text format.

## Main Class: `WSMVideogameClassifier`

### Purpose

Encapsulates all core functionality to process training data, compute scores for video games based on player preferences, and save the results to a `.txt` file.

### Constructor

```python
__init__(self, c1_train_file: str, c1_results_file: str)
```

Initializes the classifier with two file paths:

- `train_file`: Excel file containing games and playstyle classifications (used to compute weights).
- `results_file`: Excel file with games to be scored (can be the same as `train_file`).

---

### Private Methods

#### `__f_frequency_calculation(f1_df)`

- **Purpose**: Calculates the frequency (as weights) of each playstyle category in the training dataset.
- **Input**: A pandas DataFrame with one column for game names and subsequent columns for playstyles.
- **Returns**: A list of category weights, one per playstyle.
- **Raises**: ValueError if the DataFrame is empty or lacks sufficient columns.

#### `__f_score_calculation(f2_df, f2_frequency_per_category)`

- **Purpose**: Applies WSM by computing a weighted score for each game using the frequency values.
- **Input**:
  - `f2_df`: DataFrame with games to evaluate.
  - `f2_frequency_per_category`: List of weights.
- **Returns**: List of scores (0 to 10) for each game.
- **Raises**: ValueError on shape mismatch or computation error.

#### `__f_write_file(f3_str, f3_df, f3_results)`

- **Purpose**: Writes the results to a text file sorted by score.
- **Input**:
  - `f3_str`: Filename (used to derive output filename).
  - `f3_df`: Original DataFrame with game names.
  - `f3_results`: List of scores.
- **Returns**: None (writes file to disk).
- **Raises**: ValueError or OSError on invalid input or write failure.

---

### Public Method

#### `f_main_pipeline()`

- **Purpose**: Main execution flow.
- **Steps**:
  1. Reads the training file and computes frequency weights.
  2. Checks if the same file is used for both training and scoring.
  3. If not, reads a separate results file.
  4. Computes scores and writes the results.
- **Handles**: File not found, permission, value, and general exceptions with error messages.

---

## CLI Entry Point

When executed as a script, the CLI takes two arguments:

```bash
python script.py <train_file.xlsx> <results_file.xlsx>
```

- Executes the `f_main_pipeline()` using the given file paths.

---

## Example Output

Outputs a text file named like `Results <input_file_name>.txt`, listing each game and its score out of 10 based on the WSM.

---

## Dependencies

- `pandas`
- `numpy`
- `os`
- `argparse`

---

## Notes

- Files must be `.xlsx` format with game names in the first column and binary playstyle indicators in the rest.
- Scores reflect the alignment of each game with the most frequent playstyles in the training set.

