# Learning Graph

Interactive visualization of 270 interconnected OMS concepts across 14 clinical categories.

[Open Full-Screen Graph Viewer](graph-viewer.html){.md-button .md-button--primary target="_blank"}

<iframe src="graph-viewer.html" width="100%" height="600" style="border: 1px solid rgba(78,205,196,0.15); border-radius: 14px; margin: 1.5em 0;"></iframe>

Foundational concepts appear on the left with no prerequisites.
Advanced concepts on the right require mastery of all upstream dependencies.
Click a node for details. Double-click to highlight its connections. Search to filter.

## Course Description

We use the [Course Description](../course-description.md) as
the source document for the concepts that are included in this course.
The course description uses the 2001 Bloom taxonomy to order learning objectives.

## List of Concepts

The textbook contains [270 Concepts](./concept-list.md) organized across 14 taxonomy categories
covering clinical surgery, surgical technology, practice operations, and professional development.

## Concept Dependency List

The learning graph is a Directed Acyclic Graph (DAG) with 270 nodes and 457 edges.
We provide the DAG in two formats: a [CSV file](learning-graph.csv) and a
[JSON file](learning-graph.json) that uses the vis-network JavaScript library format.

## Analysis & Documentation

### Course Description Quality Assessment

- Quality score: **96/100**
- All six Bloom's Taxonomy levels represented with 5+ outcomes each
- 20 chapters covering full-scope OMS practice

[View the Course Description Quality Assessment](course-description-assessment.md)

### Learning Graph Quality Validation

- Graph structure validation - all concepts connected
- DAG validation (no cycles detected)
- 29 foundational entry points
- Indegree distribution analysis
- Longest dependency chains

[View the Learning Graph Quality Validation](quality-metrics.md)

### Concept Taxonomy

14 categories organizing the 270 concepts by clinical and operational domain:

- Anatomy, Imaging, Anesthesia, Pharmacology
- Dentoalveolar, Implants, Trauma, Orthognathic, TMJ, Pathology
- Advanced Clinical, Surgical Technology, Practice Operations, Frontiers

[View the Concept Taxonomy](concept-taxonomy.md)

### Taxonomy Distribution

Statistical breakdown of concepts by category with balance verification.

[View the Taxonomy Distribution Report](./taxonomy-distribution.md)
