# AutoFL

# Environmental Setup
## Python Dependencies
Compatible with Python >= 3.10

Install the required dependencies using the following command:

```shell
python -m pip install pandas python-dotenv tqdm markdown2 tiktoken openai javalang-ext scipy numpy matplotlib
```

## OpenAI API Setup
Before using AutoFL, set up your OpenAI API credentials by creating a `.env` file with the following content:

```shell
OPENAI_API_KEY={YOUR_API_KEY}
OPENAI_ORG_KEY{YOUR_ORG_KEY} # Optional
```
Replace `{YOUR_API_KEY}` with your OpenAI API key and `{YOUR_ORG_KEY}` with your organization's API key.

# Generate Data for Reproduction

## 1. Generate FL Results Files

The minimized FL results are currently located within the directory `combined_fl_results`.

To obtain comprehensive FL results files, please execute the following command:
```shell
sh compute_scores.sh
```
Running this command will generate complete score data within the `combined_fl_results` directory, utilizing the raw data sourced from the `results` directory.

## 2. ... #FIXME

# General Usage

## Run AutoFL

To run AutoFL, use the following command:
```shell
sh runner.sh {expr_label} {num_repetitions} {dataset}
```

Replace `{expr_label}` with a label for your experiment, `{num_repetitions}` with the number of repetitions (`R` in the paper), and `{dataset}` with the dataset you want to use (`defects4j` or `bugsinpy`).

## Compute Scores
```shell
python compute_score.py {result_directories} -l {java|python} -a -v -o {json_output_file}
```

`{result_directories}` should be the directories containing your AutoFL result files.
- `-l` specifies the language (either `java` or `python`).
- `-a` enables the use of auxiliary scores to break ties.
- `-v` enables verbose mode.
- `-o` specifies the path to the JSON output file.

## Examples

- Defects4J
    ```shell
    sh runner.sh my_d4j_autofl_ 5 defects4j
    python compute_score.py results/my_d4j_autofl_*/gpt-3.5-turbo-0613 -l java -a -v -o d4j_scores.json
    ```
- BugsInPy
    ```shell
    sh runner.sh my_bip_autofl_ 5 bugsinpy
    python compute_score.py results/my_bip_autofl_*/gpt-3.5-turbo-0613 -l python -a -v -o bip_scores.json
    ```