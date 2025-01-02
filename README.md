
# Postgres Mailing List Analysis

This project analyzes and visualizes email thread activity in the Postgres mailing list before and after the introduction of large language models (LLMs) like ChatGPT. The goal is to observe any shifts in the communication dynamics, including thread counts, email activity, and how responses have evolved.

## Project Overview

- **Analysis Focus**: Analyze Postgres mailing list archives.
- **Key Insights**: Track email thread activity, the number of messages, and the change in thread behavior after the rise of LLMs.
- **Data Source**: mbox files containing the Postgres mailing list archives.

## Installation

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/email_analysis.git
   cd email_analysis
   ```

3. **Install dependencies**:
   ```bash
   poetry install
   ```

4. **Activate the virtual environment**:
   ```bash
   poetry shell
   ```

## Folder Structure

```
postgres_mailing_list-analysis/
│
├── data/                  # Contains mbox files categorized by mailing list and year
│   ├── pgsql-admin/       # mbox files for the pgsql-admin mailing list
│   │   ├── year_2020/     # mbox files for the year 2020
│   │   │   ├── file1.mbox
│   │   │   ├── file2.mbox
│   │   │   └── ...
│   │   ├── year_2021/     # mbox files for the year 2021
│   │   │   ├── file1.mbox
│   │   │   ├── file2.mbox
│   │   │   └── ...
│   │   └── year_2022/     # mbox files for the year 2022
│   │       ├── file1.mbox
│   │       ├── file2.mbox
│   │       └── ...
│   ├── pgsql-sql/         # mbox files for the pgsql-sql mailing list
│   │   ├── year_2020/
│   │   │   ├── file1.mbox
│   │   │   └── ...
│   │   ├── year_2021/
│   │   └── year_2022/
│   └── ...                # Other mailing lists like pgsql-hackers, etc.
│
├── src/                   # Source code for analysis and visualization
│   ├── analysis.py        # Email thread and year-based analysis logic
│   ├── processing.py      # Functions to process mbox files
│   ├── visualization.py   # Visualization of thread and email counts
│   └── utils.py           # Utility functions (e.g., for printing counts)
│
│
├── pyproject.toml         # Poetry configuration and dependencies
├── main.py                # Main entry point for running the project
└── README.md              # Project overview and setup instructions
```

## Running the Project

1. **Prepare your data**: Prepare your data: Place your mbox files in the `data/` folder. The data should be organized by mailing list and year, where each mailing list (like pgsql-admin, pgsql-sql, etc.) contains subfolders named by the year (e.g., year_2020, year_2021).

2. **Execute the analysis**:
   ```bash
   python main.py
   ```

This will analyze the data and generate visual plots showing thread counts and email activity over time.