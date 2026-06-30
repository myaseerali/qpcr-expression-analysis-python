# qPCR Gene Expression Analysis Pipeline

A Python-based bioinformatics pipeline for analyzing qPCR gene expression data using the comparative Ct method (**2^-ΔΔCt**) to identify differential gene expression across tuberculosis study groups.

---

## Abstract

Quantitative PCR (qPCR) is widely used to measure gene expression levels in biological samples. This project implements a complete computational pipeline for processing and analyzing qPCR data from tuberculosis-related samples.

The pipeline performs:

- Data loading and preprocessing
- Technical replicate quality control
- Mean Ct calculation
- ΔCt calculation
- ΔΔCt calculation
- Fold change analysis
- Statistical testing
- Data visualization
- Final report generation
- CSV export of results

This project demonstrates how computational analysis can be integrated with molecular diagnostics to derive biologically meaningful insights from laboratory-generated data.

---

## Biological Background

Tuberculosis (TB), caused by *Mycobacterium tuberculosis*, remains a major global health challenge. Immune-related genes can show different expression patterns depending on disease state.

This project evaluates expression of key immune-response genes:

### Target Genes

- **IFNG (Interferon Gamma)**  
  Important cytokine in anti-TB immune response.

- **IL2RA (Interleukin 2 Receptor Alpha)**  
  Associated with T-cell activation.

- **TNFA (Tumor Necrosis Factor Alpha)**  
  Critical inflammatory mediator in TB infection.

### Housekeeping Gene

- **GAPDH**  
  Used for normalization because of stable expression.

---

## Study Groups

The dataset contains samples from three groups:

- **Control** — healthy individuals  
- **Latent TB** — infected but asymptomatic  
- **Active TB** — active disease state  

---

## Methodology

### 1. Mean Ct Calculation

Technical replicates are averaged:

\[
Mean\ Ct = \frac{Replicate_1 + Replicate_2 + Replicate_3}{3}
\]

---

### 2. Delta Ct (ΔCt)

Target gene Ct is normalized using housekeeping gene:

\[
\Delta Ct = Ct_{target} - Ct_{GAPDH}
\]

---

### 3. Delta Delta Ct (ΔΔCt)

Sample ΔCt compared with control group:

\[
\Delta \Delta Ct = \Delta Ct_{sample} - Mean\ \Delta Ct_{control}
\]

---

### 4. Fold Change

Relative gene expression:

\[
Fold\ Change = 2^{-\Delta\Delta Ct}
\]

Interpretation:

- **> 1** → Upregulated  
- **< 1** → Downregulated  
- **= 1** → No change  

---

## Features

### Data Processing
- CSV import
- Data cleaning
- Structured qPCR dataset loading

### Quality Control
- Technical replicate spread checking
- Outlier detection

### Analysis
- Mean Ct calculation
- ΔCt calculation
- ΔΔCt calculation
- Fold change computation

### Statistics
- Group-level summary
- Statistical testing (t-test)

### Visualization
- Fold change plots

### Reporting
- Final result tables
- CSV export

---

## Project Workflow

```text
Raw qPCR Data
      ↓
Data Loading
      ↓
Quality Control
      ↓
Mean Ct
      ↓
ΔCt Calculation
      ↓
ΔΔCt Calculation
      ↓
Fold Change Analysis
      ↓
Statistical Testing
      ↓
Visualization
      ↓
Final Report Export
```

---

## Project Structure

```bash
qpcr_expression_analysis_by_python/
│
├── data/
│   └── raw/
│       └── tb_qpcr_export.csv
│
├── results/
│   ├── fold_change_plot.png
│   ├── fold_change_results.csv
│   ├── group_summary.csv
│   ├── statistical_results.csv
│   └── final_report.csv
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── qc.py
│   ├── delta_ct.py
│   ├── fold_change.py
│   ├── statistics.py
│   ├── visualization.py
│   ├── plot_results.py
│   ├── report.py
│   └── export_results.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/myaseerali/qpcr-expression-analysis-python.git
```

Move into project:

```bash
cd qpcr-expression-analysis-python
```

Create virtual environment:

### Windows

```bash
python -m venv .venv
```

Activate environment:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
python src/main.py
```

---

## Example Results

Group summary from current dataset:

| Group | IFNG Fold Change | IL2RA Fold Change | TNFA Fold Change |
|---|---:|---:|---:|
| Control | 1.01 | 1.01 | 1.01 |
| Latent TB | 7.84 | 5.38 | 3.63 |
| Active TB | 42.30 | 30.87 | 29.60 |

---

## Biological Interpretation

Analysis suggests strong upregulation of immune-response genes in Active TB samples.

### Observations

- **IFNG** shows strongest upregulation (~42x)
- **IL2RA** significantly elevated (~31x)
- **TNFA** strongly increased (~30x)

These findings suggest enhanced immune activation in active disease compared with controls.

---

## Limitations

Current pipeline limitations:

- Small example dataset
- Basic visualization only
- Limited statistical testing
- No automated PDF reporting

---

## Future Improvements

Planned upgrades:

- Heatmaps
- Volcano plots
- PCA analysis
- Machine learning classification
- PDF report generation
- Command-line interface (CLI)
- Web dashboard

---

## Skills Demonstrated

This project demonstrates practical skills in:

- Python programming
- Pandas data analysis
- Scientific computing
- Molecular data interpretation
- Bioinformatics workflow design
- Git & GitHub version control

---

## Author

**Yasir Ali**  
Medical Laboratory Scientist  
MPhil in Molecular Pathology & Genetics  
Bioinformatics / Computational Biology Learner

---

## License

This project is for educational and research purposes.