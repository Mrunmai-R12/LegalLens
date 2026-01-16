import re
from typing import List, Dict

def clause_chunk(text: str) -> List[Dict]:
    pattern = r"(\d+\.\d+[\s\S]*?)(?=\d+\.\d+|$)"
    clauses = re.findall(pattern, text)

    return [
        {
            "text": clause.strip(),
            "metadata": {"clause": clause.split()[0]}
        }
        for clause in clauses
    ]
