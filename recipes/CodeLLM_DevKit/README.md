# CodeLLM-Devkit: A Python library for seamless interaction with CodeLLMs

[Codellm-devkit](https://github.com/IBM/codellm-devkit/tree/main) (CLDK) is a multilingual software program analysis framework that bridges the gap between traditional static analysis tools and Large Language Models (LLMs) specialized for code (CodeLLMs). Codellm-devkit allows developers to streamline the process of transforming raw code into insights by providing a unified interface for integrating outputs from various analysis tools and preparing them for effective use by CodeLLMs.

Codellm-devkit simplifies the complex process of analyzing codebases that span multiple programming languages, making it easier to extract meaningful insights and drive LLM-based code analysis. CLDK achieves this through an open-source Python library that abstracts the intricacies of program analysis and LLM interactions. The unified interface integrates outputs from various analysis tools and prepares them for use by CodeLLMs.

For more details, please refer to [CLDK GitHub repository](https://github.com/IBM/codellm-devkit/tree/main).

Here are the example recipes in this directory:

* [Code Summarization](./code_summarization.ipynb) - Summarize what a Java method does.
* [Generate Unit Tests](./generate_unit_tests.ipynb) - Generate unit tests for Java code.
* [Validating Code](./validating_code_translation.ipynb) - Translate Java code to Python and analyze it for correctness.

> **TIP:** Please start with the [Code Summarization](./code_summarization.ipynb) tutorial, as it provides set up instructions that won't be repeated in the other notebooks.

The recipes download Java example code to a temporary directory `./temp`. The analysis will be saved in the `./analysis` directory. When you are finished with these recipes, you can safely delete these directories, e.g.,

```shell
rm -rf temp
rm -rf analysis
```
