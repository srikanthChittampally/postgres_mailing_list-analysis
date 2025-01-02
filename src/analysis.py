from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Tuple

import pandas as pd
from src.processing import process_mbox_file


def analyze_mbox_files(file_paths: list) -> Tuple[Dict[int, int], Dict[int, int]]:
    """
    Analyze multiple mbox files in parallel and generate thread and email counts by year.
    
    Args:
        file_paths: List of paths to mbox files
        
    Returns:
        Tuple of (threads_by_year, emails_by_year) dictionaries
    """
   
    
    # Process all mbox files in parallel
    with ThreadPoolExecutor() as executor:
        try:
            # Get DataFrames for all files
            dfs = list(executor.map(process_mbox_file, file_paths))
        except Exception as e:
            print(f"Error during parallel processing: {e}")
            dfs = []  # Return an empty list in case of error
    
    # Combine all DataFrames (ensure the result is not empty)
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
    else:
        combined_df = pd.DataFrame()  # Empty DataFrame if there's an error
    
    if not combined_df.empty:
        all_messages = set(combined_df['message_id'])
        
        # Determine root messages
        def is_root(row):
            return not any(ancestor in all_messages for ancestor in row['ancestors'])
        
        # Add root column
        combined_df['is_root'] = combined_df.apply(is_root, axis=1)
        
        # Calculate threads by year
        threads_by_year = combined_df[combined_df['is_root']].groupby('year').size().to_dict()
        
        # Calculate total emails by year
        emails_by_year = combined_df.groupby('year').size().to_dict()
        
        return threads_by_year, emails_by_year
    else:
        print("No data to process.")
        return {}, {}