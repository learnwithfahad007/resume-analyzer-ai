import json
import re


# Load skills database
with open('skills_db.json', 'r') as f:
    SKILLS_DB = json.load(f)


def extract_text_from_file(uploaded_file):
    """
    Extract text from PDF or text file.
    """
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(uploaded_file)
        pages = [p.extract_text() or '' for p in reader.pages]
        return '\n'.join(pages)
    except Exception:
        uploaded_file.seek(0)
        return uploaded_file.read().decode('utf-8', errors='ignore')


def extract_skills(text):
    """
    Extract skills from text based on SKILLS_DB.
    """
    text_low = text.lower()
    found = set()

    for skill in SKILLS_DB:
        if skill.lower() in text_low:
            found.add(skill)

    return sorted(found)


def ats_score(skills_found, target_skills):
    """
    Calculate ATS score based on matched skills.
    """
    if not target_skills:
        return 0

    matched = sum(1 for s in target_skills if s in skills_found)
    return round(100 * matched / len(target_skills))
