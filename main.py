
from src.analysis import analyze_mbox_files
from src.visualization import plot_yearly_statistics
from src.utils import all_mbox_files


def main(mbox_folder: str) -> None:
    """Analyze email threads from mbox files with parallel processing."""
    # Collect all mbox files
    mbox_files = all_mbox_files(mbox_folder)
    threads_by_year, emails_by_year = analyze_mbox_files(mbox_files)
    
    print("\nThread counts by year:")
    for year, count in sorted(threads_by_year.items()):
        print(f"{year}: {count} threads")
        
    print("\nEmail counts by year:")
    for year, count in sorted(emails_by_year.items()):
        print(f"{year}: {count} emails")
    
    # Create visualizations
    plot_yearly_statistics(threads_by_year, emails_by_year)



if __name__ == "__main__":
    print("Starting analysis...")
    # Define the path to the folder containing your mbox files
    mbox_folder = './data/pgsql-admin/'
    main(mbox_folder)