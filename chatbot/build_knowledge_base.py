"""
Builds the knowledge base text file from all markdown content.
Combines course description, glossary, all chapters, and learning graph
into a single file for the chatbot's context.

Usage: python build_knowledge_base.py
"""

from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"
OUTPUT_PATH = Path(__file__).parent / "knowledge_base.txt"

def build():
    sections = []

    # Course description
    course_desc = DOCS_DIR / "course-description.md"
    if course_desc.exists():
        sections.append("# COURSE DESCRIPTION\n\n" + course_desc.read_text(encoding="utf-8"))

    # Glossary
    glossary = DOCS_DIR / "glossary" / "index.md"
    if glossary.exists():
        sections.append("# GLOSSARY\n\n" + glossary.read_text(encoding="utf-8"))

    # Chapters (sorted by number)
    chapters_dir = DOCS_DIR / "chapters"
    if chapters_dir.exists():
        chapter_dirs = sorted(chapters_dir.iterdir())
        for chapter_dir in chapter_dirs:
            index_file = chapter_dir / "index.md"
            if index_file.exists():
                content = index_file.read_text(encoding="utf-8")
                if len(content.strip()) > 100:  # skip placeholder stubs
                    sections.append(f"# CHAPTER {chapter_dir.name}\n\n" + content)

    # Learning graph
    learning_graph = DOCS_DIR / "learning-graph" / "index.md"
    if learning_graph.exists():
        sections.append("# LEARNING GRAPH\n\n" + learning_graph.read_text(encoding="utf-8"))

    # Write combined output
    combined = "\n\n---\n\n".join(sections)
    OUTPUT_PATH.write_text(combined, encoding="utf-8")

    word_count = len(combined.split())
    print(f"Knowledge base built: {OUTPUT_PATH}")
    print(f"Total words: {word_count:,}")
    print(f"Total sections: {len(sections)}")

if __name__ == "__main__":
    build()
