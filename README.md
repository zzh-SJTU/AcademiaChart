# Is GPT-4V (ision) All You Need for Automating Academic Data Visualization? Exploring Vision-Language Models’ Capability in Reproducing Academic Charts

🔍 This repository contains the official code for the EMNLP 2024 Findings paper titled ["Is GPT-4V (ision) All You Need for Automating Academic Data Visualization? Exploring Vision-Language Models’ Capability in Reproducing Academic Charts"](https://aclanthology.org/2024.findings-emnlp.485/).

### Authors
- **Zhehao Zhang** - [Homepage](https://zzh-sjtu.github.io/zhehaozhang.github.io/)
- **Weicheng Ma**
- **Soroush Vosoughi**

---

## 🌟 Abstract

<details><summary>Click to expand</summary>
  
Data visualization plays a critical role in academic research by presenting complex information in an accessible format. However, crafting high-quality visualizations requires expertise in both data management and graphic design. This paper explores the use of Vision-Language Models (VLMs) to automate the creation of data visualizations by generating code templates based on existing charts. As the first systematic investigation of this task, we introduce **AcademiaChart**, a dataset of 2525 high-resolution data visualization figures with captions from AI conferences, sourced directly from original code. Our experiments with six state-of-the-art VLMs reveal that closed-source VLMs like GPT-4-V are effective in reproducing charts, while open-source models are limited to simpler charts. Notably, Chain-of-Thought (CoT) prompting enhances GPT-4-V's performance, though it has limited impact on other models. These findings highlight the potential of VLMs in automating data visualization while pinpointing areas for improvement for broader applicability.

</details>

---

## 📂 File Structure

To download the test data used in this paper, please use the provided [Google Drive link](https://drive.google.com/file/d/19jmv7SmlT4QHt1J_pF57zc6dl43jCkLZ/view?usp=sharing) and place the downloaded files in the same directory as `dataset_file.json`, which serves as the index. Please note that the downloaded figures are raw images; those not indexed in `dataset_file.json` may include non-data visualization figures that fall outside the scope of this work. You may need to filter these figures according to the guidelines described in Section 4.

### Key Files
1. **Dataset JSON File (`dataset_file.json`)**:
   - Contains structured metadata for each figure in the dataset. Each entry includes:
     - `figure_path`: Relative path to the figure within the dataset.
     - `caption`: Figure caption.
     - `source`: Source file for the figure.
     - `arxiv_id`: Identifier linking the figure to its original publication.
     - `type`: Type of figure (e.g., Line Chart, Bar Graph).

2. **`arxiv_source_downloader.py`**:
   - Python script to download LaTeX source code from arXiv. Modify `search_url` and `output_folder` in the main function as needed.

3. **`arxiv_figure_extractor.py`**:
   - Script to locate and extract figure paths and captions from source code using regular expressions, saving relevant metadata.

### Model Inference and Testing
For model inference details, including prompt and hyperparameter settings, please refer to **Appendix A.2** and **A.3** in the paper.

---

## 📞 Contact Information

For questions or collaboration inquiries, please reach out to:

- **Lead Author**: Zhehao Zhang - [zhehao.zhang.gr@dartmouth.edu]

---

## 📖 Citation

If this work contributes to your research, please consider citing our paper:

```bibtex
@inproceedings{zhang-etal-2024-gpt,
    title = "Is {GPT}-4{V} (ision) All You Need for Automating Academic Data Visualization? Exploring Vision-Language Models{'} Capability in Reproducing Academic Charts",
    author = "Zhang, Zhehao  and
      Ma, Weicheng  and
      Vosoughi, Soroush",
    editor = "Al-Onaizan, Yaser  and
      Bansal, Mohit  and
      Chen, Yun-Nung",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2024",
    month = nov,
    year = "2024",
    address = "Miami, Florida, USA",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.findings-emnlp.485",
    pages = "8271--8288",
    abstract = "While effective data visualization is crucial to present complex information in academic research, its creation demands significant expertise in both data management and graphic design. We explore the potential of using Vision-Language Models (VLMs) in automating the creation of data visualizations by generating code templates from existing charts. As the first work to systematically investigate this task, we first introduce AcademiaChart, a dataset comprising 2525 high-resolution data visualization figures with captions from a variety of AI conferences, extracted directly from source codes. We then conduct large-scale experiments with six state-of-the-art (SOTA) VLMs, including both closed-source and open-source models. Our findings reveal that SOTA closed-source VLMs can indeed be helpful in reproducing charts. On the contrary, open-source ones are only effective at reproducing much simpler charts but struggle with more complex ones. Interestingly, the application of Chain-of-Thought (CoT) prompting significantly enhances the performance of the most advanced model, GPT-4-V, while it does not work as well for other models. These results underscore the potential of VLMs in data visualization while also highlighting critical areas that need improvement for broader application.",
}
```
