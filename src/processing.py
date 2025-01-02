from datetime import datetime
import email.utils
import mailbox
import pandas as pd


def process_single_message(msg: mailbox.mboxMessage) -> dict:
    """
    Process a single email message and extract relevant information.
    
    Args:
        msg: An email message from the mbox file
        
    Returns:
        Dictionary containing message details
    """
    # Extract message ID
    msg_id = msg.get('Message-ID', '').strip().strip('<>')
    if not msg_id:
        return None
        
    # Extract date
    date_str = msg.get('Date')
    if date_str:
        try:
            # Parse the email date
            date_tuple = email.utils.parsedate_tz(date_str)
            if date_tuple:
                date = datetime(*date_tuple[:6])
                year = date.year
            else:
                return None
        except Exception:
            return None
    else:
        return None
        
    # Get References and In-Reply-To
    references = msg.get('References', '')
    in_reply_to = msg.get('In-Reply-To', '').strip().strip('<>')
    
    # Get all ancestors
    ancestors = set()
    if references:
        ancestors.update(ref.strip().strip('<>') for ref in references.split())
    if in_reply_to and in_reply_to not in ancestors:
        ancestors.add(in_reply_to)
    
    return {
        'message_id': msg_id,
        'year': year,
        'ancestors': ancestors
    }

def process_mbox_file(file_path: str) -> pd.DataFrame:
    """
    Process a single mbox file and return its data as a DataFrame.
    
    Args:
        file_path: Path to the mbox file
        
    Returns:
        DataFrame containing message information
    """
    try:
        mbox = mailbox.mbox(file_path)
        messages_data = []
        
        for message in mbox:
            msg_data = process_single_message(message)

            if msg_data:
                messages_data.append(msg_data)
        
        return pd.DataFrame(messages_data)
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on failure

